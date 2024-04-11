import os
import sys
import streamlit as st
from loguru import logger
from dotenv import load_dotenv
from crewai import Agent, Crew, Process
from crewai import Crew, Process
from agents import CustomAgents
from tasks import CustomTasks
from utils import print_agent_output
from tools.AgentTools import AgentTools

# Load environment variables from .env file
load_dotenv()

# Configure Loguru
logger.remove()
logger.add(sys.stderr, colorize=False, format="<green>{time}</green> | <level>{level}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>")

agents = CustomAgents(human_input=True, callbacks=None)
tasks = CustomTasks(topic="Create python code", section="Code Generation")

def main(user_input):
    st.set_page_config(page_title="CodeSynthAI", page_icon=":robot_face:", layout="wide")
    logger.info("Streamlit app started")

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

    st.title("CodeSynthAI Chatbot")

    # Sidebar
    st.sidebar.title("Settings")
    api_choice = st.sidebar.selectbox("Select API", ["OpenAI", "Anthropic"])
    if api_choice == "OpenAI":
        model_choice = st.sidebar.selectbox("Select OpenAI Model", ["gpt-3.5-turbo", "gpt-4-turbo-2024-04-09"])
    else:
        model_choice = st.sidebar.selectbox("Select Anthropic Model", ["claude-3-haiku-20240307", "claude-3-sonnet-20240229", "claude-3-opus-20240229"])

    iterations = st.sidebar.slider("Number of Iterations", min_value=1, max_value=10, value=5, step=1)
    logger.debug(f"Number of iterations set to {iterations}")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_interaction = st.chat_input("Interact with the agents:")
    if user_interaction:
        st.session_state.messages.append({"role": "user", "content": user_interaction})
        with st.chat_message("user"):
            st.markdown(user_interaction)

        logger.debug(f"User interaction: {user_interaction}")

        logger.info("Code generation started")

        # Create Agents
        requirements_analyst_agent = agents.requirements_analyst(api_choice, model_choice)
        code_generator_agent = agents.code_generator(api_choice, model_choice)
        code_quality_assurance_agent = agents.code_quality_assurance(api_choice, model_choice)
        quality_assurance_engineer_agent = agents.quality_assurance_engineer(api_choice, model_choice)

        # Create Tasks
        requirements_analysis = tasks.requirements_analyst_task(requirements_analyst_agent, user_interaction)
        code_generation = tasks.code_generator_task(code_generator_agent, requirements_analysis.expected_output, user_interaction)
        code_quality_assurance = tasks.code_quality_assurance_task(code_quality_assurance_agent, code_generation.expected_output, requirements_analysis.expected_output, user_interaction)
        quality_assurance_engineering = tasks.quality_assurance_engineer_task(quality_assurance_engineer_agent, code_generation.expected_output, requirements_analysis.expected_output, user_interaction)
        code_quality_assurance.context = [requirements_analysis, code_generation]
        quality_assurance_engineering.context = [requirements_analysis, code_generation, code_quality_assurance]

        def update_agent_output(agent_output):
            agent_name = agent_output["agent_name"]
            output = print_agent_output(agent_output["output"], agent_name)

            st.session_state.messages.append({"role": agent_name, "content": output})
            with st.chat_message(agent_name):
                st.markdown(output)

            st.experimental_rerun()

        # Create Crew
        crew = Crew(
            agents=[
                requirements_analyst_agent,
                code_generator_agent,
                code_quality_assurance_agent,
                quality_assurance_engineer_agent
            ],
            tasks=[
                requirements_analysis,
                code_generation,
                code_quality_assurance,
                quality_assurance_engineering
            ],
            manager_llm=agents.get_manager_llm(api_choice, model_choice),
            process=Process.hierarchical,
            tools=AgentTools().tools(),
            memory=True,
            max_iter=iterations,
            step_callback=update_agent_output,
            verbose=2
        )

        # Run the crew
        result = crew.kickoff()
        logger.info(f"Code generation completed: {result}")

        # Display generated code
        st.header("Generated Code")
        st.code(result, language="python")
        logger.debug(f"Generated code displayed: {result}")

        # User confirmation and code download
        if st.button("Confirm and Save Code"):
            logger.info("User confirmed and saved the code")

            # Save the generated code locally
            with open("generated_code.py", "w") as file:
                file.write(result)
            logger.debug("Generated code saved locally")

            # Provide a download link for the generated code
            with open("generated_code.py", "rb") as file:
                download_button = st.download_button(
                    label="Download Generated Code",
                    data=file,
                    file_name="generated_code.py",
                    mime="text/plain"
                )
            logger.debug("Download link provided for generated code")

        # Append the final result to the chat messages
        st.session_state.messages.append({"role": "assistant", "content": result})

if __name__ == "__main__":
    main("")