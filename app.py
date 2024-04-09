import os
import sys
import streamlit as st
from dotenv import load_dotenv
from loguru import logger
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

agents = CustomAgents(human_input=False, callbacks=None)
tasks = CustomTasks(topic="Create production python code", section="Code Generation")

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

    st.title("CodeSynthAI")

    # Sidebar
    st.sidebar.title("Settings")
    api_choice = st.sidebar.selectbox("Select API", ["OpenAI", "Anthropic"])
    if api_choice == "OpenAI":
        model_choice = st.sidebar.selectbox("Select OpenAI Model", ["gpt-3.5-turbo", "gpt-4"])
    else:
        model_choice = st.sidebar.selectbox("Select Anthropic Model", ["claude-3-haiku-20240307", "claude-3-sonnet-20240229", "claude-3-opus-20240229"])

    iterations = st.sidebar.slider("Number of Iterations", min_value=1, max_value=10, value=5, step=1)
    logger.debug(f"Number of iterations set to {iterations}")

    # User interaction input
    user_interaction = st.text_area("Interact with the agents:")
    logger.debug(f"User interaction: {user_interaction}")

    if st.button("Generate Code"):
        logger.info("Code generation started")

        # Create Agents
        technical_consultant_agent = agents.technical_consultant(api_choice, model_choice)
        initial_coder_agent = agents.initial_coder(api_choice, model_choice)
        senior_code_reviewer_agent = agents.senior_code_reviewer(api_choice, model_choice)
        tester_agent = agents.tester(api_choice, model_choice)

        # Create Tasks
        technical_consultation = tasks.technical_consultant_task(technical_consultant_agent, user_interaction)
        code_generation = tasks.initial_coder_task(initial_coder_agent, technical_consultation.expected_output, user_interaction)
        code_review = tasks.senior_code_reviewer_task(senior_code_reviewer_agent, code_generation.expected_output, technical_consultation.expected_output, user_interaction)
        testing = tasks.tester_task(tester_agent, code_generation.expected_output, technical_consultation.expected_output, user_interaction)
        code_review.context = [technical_consultation, code_generation]
        testing.context = [technical_consultation, code_generation, code_review]

        # Create Crew
        crew = Crew(
            agents=[
                technical_consultant_agent,
                initial_coder_agent,
                senior_code_reviewer_agent,
                tester_agent
            ],
            tasks=[
                technical_consultation,
                code_generation,
                code_review,
                testing
            ],
            manager_llm=agents.get_manager_llm(api_choice, model_choice),
            process=Process.hierarchical,
            tools=AgentTools().tools(),
            memory=True,
            max_iter=iterations,
            step_callback=lambda x: print_agent_output(x, "Crew Manager")
        )

        # Run the crew
        result = crew.kickoff()
        logger.info(f"Code generation completed: {result}")

        # Display generated code
        st.header("Generated Code")
        result = st.code(result, language="python")
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

        # User interaction with agents
        if user_interaction:
            # Pass the user interaction to the relevant agent or task
            # and update the agent streaming output
            # (Implement the logic based on your specific requirements)
            logger.debug(f"User interaction processed: {user_interaction}")

if __name__ == "__main__":
    main("")