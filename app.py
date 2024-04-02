import os
import json
from dotenv import load_dotenv
import streamlit as st
from langchain.agents import initialize_agent, AgentType
from langchain_community.llms import OpenAI
from crewai import Crew
from tasks import CustomTasks
from agents import CustomAgents
from tools.AgentTools import AgentTools

# Load environment variables from .env file
load_dotenv()

# Set up Anthropic API key
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# Set up OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize CrewAI
tasks = CustomTasks(topic="AI-Powered Software Development", section="Code Generation")
agents = CustomAgents()

# Streamlit app
def main():
    st.set_page_config(page_title="AI-Powered Software Development", page_icon=":robot_face:", layout="wide")

    # Set dark mode theme
    dark_mode = st.sidebar.checkbox("Dark Mode", value=True)
    if dark_mode:
        st.markdown(
            """
            <style>
            body {
                color: white;
                background-color: #1c1c1c;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <style>
            body {
                color: black;
                background-color: white;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

    st.title("AI-Powered Software Development")

    # Sidebar
    st.sidebar.title("Settings")
    iterations = st.sidebar.slider("Number of Iterations", min_value=1, max_value=10, value=5, step=1)
    system_prompt_text = st.sidebar.text_area("System Prompt", value="You are a multi-agent software development system.", height=200)

    # Initialize agents
    technical_consultant_agent = agents.technical_consultant()
    initial_coder_agent = agents.initial_coder()
    senior_code_reviewer_agent = agents.senior_code_reviewer()
    tester_agent = agents.tester()

    # Initialize tools
    tools = AgentTools.tools()

    # Initialize the agent
    agent = initialize_agent(
        tools,
        OpenAI(temperature=0),
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        max_iterations=iterations,
    )

    # User input
    user_input = st.text_area("Enter your project requirements:")

    # Agent output stream
    agent_output = st.empty()

    if st.button("Generate Code"):
        try:
            # Technical Consultant interaction
            with st.spinner("Technical Consultant is refining your requirements..."):
                technical_consultant_task = tasks.technical_consultant_task(technical_consultant_agent, user_input)
                refined_requirements = agent.run(technical_consultant_task.description)
                
                # Capture the agent's output stream
                agent_output.text_area("Agent Output", value=agent.memory.buffer, height=200)
                
                # Add human input for Technical Consultant
                human_input_technical_consultant = st.text_input("Provide additional input for Technical Consultant (optional):")
                if human_input_technical_consultant:
                    refined_requirements += f"\nAdditional human input: {human_input_technical_consultant}"
                
        except Exception as e:
            st.error(f"Error during Technical Consultant interaction: {str(e)}")
            st.stop()
        
        st.success("Requirements refined!")
        st.write("Refined Requirements:")
        st.write(refined_requirements)

        if st.button("Confirm Requirements"):
            if st.button("Start Development"):
                # Development cycle
                iteration_logs = []
                for i in range(iterations):
                    # Initial Coder
                    with st.spinner("Initial Coder is generating code..."):
                        initial_coder_task = tasks.initial_coder_task(initial_coder_agent, refined_requirements)
                        generated_code = agent.run(initial_coder_task.description)
                        
                        # Capture the agent's output stream
                        agent_output.text_area("Agent Output", value=agent.memory.buffer, height=200)
                        
                        # Add human input for Initial Coder
                        human_input_initial_coder = st.text_input("Provide additional input for Initial Coder (optional):")
                        if human_input_initial_coder:
                            generated_code += f"\n# Additional human input: {human_input_initial_coder}"
                        
                    st.write("Generated Code:")
                    st.code(generated_code, language="python")

                    # Senior Code Reviewer
                    with st.spinner("Senior Code Reviewer is reviewing the code..."):
                        senior_code_reviewer_task = tasks.senior_code_reviewer_task(senior_code_reviewer_agent, generated_code)
                        code_review = agent.run(senior_code_reviewer_task.description)
                        
                        # Capture the agent's output stream
                        agent_output.text_area("Agent Output", value=agent.memory.buffer, height=200)
                        
                        # Add human input for Senior Code Reviewer
                        human_input_code_reviewer = st.text_input("Provide additional input for Senior Code Reviewer (optional):")
                        if human_input_code_reviewer:
                            code_review += f"\nAdditional human input: {human_input_code_reviewer}"
                        
                    st.write("Code Review:")
                    st.write(code_review)

                    # Tester
                    with st.spinner("Tester is testing the code..."):
                        tester_task = tasks.tester_task(tester_agent, generated_code)
                        test_results = agent.run(tester_task.description)
                        
                        # Capture the agent's output stream
                        agent_output.text_area("Agent Output", value=agent.memory.buffer, height=200)
                        
                        # Add human input for Tester
                        human_input_tester = st.text_input("Provide additional input for Tester (optional):")
                        if human_input_tester:
                            test_results += f"\nAdditional human input: {human_input_tester}"
                        
                    st.write("Test Results:")
                    st.write(test_results)

                    iteration_logs.append({
                        "iteration": i + 1,
                        "generated_code": generated_code,
                        "code_review": code_review,
                        "test_results": test_results,
                    })

                    if "passed" in test_results.lower():
                        st.success("Code passed all tests!")
                        break
                    else:
                        st.warning("Code failed tests. Iterating again...")

                if "passed" not in test_results.lower():
                    st.error(f"Unable to generate functional code within {iterations} iterations. Consider increasing the number of iterations or selecting a more advanced AI model.")

                # Display intermediate results and allow user intervention
                for log in iteration_logs:
                    st.write(f"Iteration {log['iteration']}")
                    st.write("Generated Code:")
                    st.code(log["generated_code"], language="python")
                    st.write("Code Review:")
                    st.write(log["code_review"])
                    st.write("Test Results:")
                    st.write(log["test_results"])

                    if not st.button("Continue to Next Iteration"):
                        st.stop()

                # Display the final generated code
                st.header("Final Generated Code")
                st.code(generated_code, language="python")

                # User feedback and code selection for vector store
                st.subheader("Provide Feedback and Select Code for Vector Store")
                user_feedback = st.radio("Feedback", ("👍 Thumbs Up", "👎 Thumbs Down"))
                if st.button("Submit Feedback and Add to Vector Store"):
                    # Prepare metadata
                    metadata = {
                        "user_requirements": refined_requirements,
                        "code_review_suggestions": code_review,
                        "test_results": test_results,
                    }

                    # Store code snippet with user feedback
                    AgentTools.store_code_snippet(generated_code, metadata)

                    st.success("Code snippet and feedback added to the vector store!")

                # Display the agent conversations
                st.header("Agent Conversations")
                st.text(agent.memory.buffer)

                # Save structured agent conversations for analysis
                agent_conversations = {
                    "technical_consultant": refined_requirements,
                    "iterations": iteration_logs,
                }

                with open("agent_conversations.json", "w") as f:
                    json.dump(agent_conversations, f, indent=2)
            else:
                st.stop()
        else:
            st.warning("Please confirm the requirements before starting the development.")

if __name__ == "__main__":
    main()