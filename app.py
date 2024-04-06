import os
from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
from crewai import Crew, Process, Agent
from tasks import CustomTasks
from agents import CustomAgents
import sys
import io
from loguru import logger
import zipfile
import tempfile
from tools.AgentTools import AgentTools


# Load environment variables from .env file
load_dotenv()

# Configure Loguru
logger.remove()  # Remove the default logger
logger.add(sys.stderr, colorize=False, format="<green>{time}</green> | <level>{level}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>")

# Function to capture terminal output
def get_terminal_output(user_input):
    # Redirect stdout to a buffer
    buffer = io.StringIO()
    sys.stdout = buffer

    # Run your code here (e.g., call the main() function)
    main(user_input)

    # Get the output from the buffer
    output = buffer.getvalue()

    # Reset stdout to its original value
    sys.stdout = sys.__stdout__

    return output

agents = CustomAgents()
tasks = CustomTasks(topic="Create production python code", section="Code Generation")

# Streamlit app
def main(user_interaction):
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
    iterations = st.sidebar.slider("Number of Iterations", min_value=15, max_value=100, value=15, step=10)
    logger.debug(f"Number of iterations set to {iterations}")

    user_interaction = st.text_area("Interact with the agents:")
    logger.debug(f"User interaction: {user_interaction}")

    if st.button("Generate Code"):
        logger.info("Code generation started")

        # Create Agents
        technical_consultant_manager = agents.technical_consultant_manager()
        initial_coder_agent = agents.initial_coder()
        senior_code_reviewer_agent = agents.senior_code_reviewer()
        tester_agent = agents.tester()

        # Create Tasks
        technical_consultation = tasks.technical_consultant_task(technical_consultant_manager, user_interaction)
        code_generation = tasks.initial_coder_task(initial_coder_agent, technical_consultation.expected_output, user_interaction)
        code_review = tasks.senior_code_reviewer_task(senior_code_reviewer_agent, code_generation.expected_output, technical_consultation.expected_output, user_interaction)
        testing = tasks.tester_task(tester_agent, code_generation.expected_output, technical_consultation.expected_output, user_interaction)
        code_review.context = [technical_consultation, code_generation]
        testing.context = [technical_consultation, code_generation, code_review]

        # Create Crew
        crew = Crew(
            agents=[
                technical_consultant_manager,
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
            manager_llm=ChatOpenAI(temperature=0, model="gpt-4"),
            process=Process.hierarchical,
            tools=AgentTools().tools(),
            memory=True,
        )

        # Run the crew
        result = crew.kickoff()
        logger.info(f"Code generation completed: {result}")

        # Display generated code
        st.header("Generated Code")
        result = st.code(result, language="python")
        logger.debug(f"Generated code displayed: {result}")

        # Display agent streaming output
        # agent_output.text_area("Agent Output", result, height=200)
        # logger.debug(f"Agent output displayed: {result}")

        # Display generated files
        project_dir = f"./workdir/"
        if os.path.exists(project_dir):
            st.header("Generated Files")
            files = os.listdir(project_dir)
            for file_name in files:
                file_path = os.path.join(project_dir, file_name)
                with open(file_path, "r") as file:
                    file_content = file.read()
                    st.subheader(file_name)
                    st.code(file_content, language="python")

                # Download individual file
                with open(file_path, "rb") as file:
                    download_button = st.download_button(
                        label=f"Download {file_name}",
                        data=file,
                        file_name=file_name,
                        mime="text/plain"
                    )

            # Download all files as a zip
            with tempfile.SpooledTemporaryFile() as tmp:
                with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zip_file:
                    for file_name in files:
                        file_path = os.path.join(project_dir, file_name)
                        zip_file.write(file_path, file_name)
                tmp.seek(0)
                download_button = st.download_button(
                    label="Download All Files (ZIP)",
                    data=tmp,
                    file_name="generated_files.zip",
                    mime="application/zip"
                )

                # User interaction with agents
                if user_interaction:
                    # Pass the user interaction to the relevant agent or task
                    # and update the agent streaming output
                    # (Implement the logic based on your specific requirements)
                    logger.debug(f"User interaction processed: {user_interaction}")

if __name__ == "__main__":
    main("")