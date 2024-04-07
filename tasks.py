import sys
from crewai import Task
from textwrap import dedent
from pydantic import BaseModel
from loguru import logger

logger.remove()  # Remove the default logger
logger.add(sys.stderr, colorize=False, format="<green>{time}</green> | <level>{level}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>")

class TechnicalSpecifications(BaseModel):
    specifications: str

class GeneratedCode(BaseModel):
    code: str

class CodeReview(BaseModel):
    review: str

class TestResults(BaseModel):
    test_cases: str
    feedback: str

class CustomTasks:
    def __init__(self, topic, section):
        self.topic = topic
        self.section = section
        logger.debug(f"Initialized CustomTasks with topic: {topic} and section: {section}")

    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def technical_consultant_task(self, agent, user_input):
        logger.debug(f"User input: {user_input}")
        return Task(
            description=dedent(
                f"""
                Before commenting that a file doesn't exist, use the 'list_project_files' tool to check the files in the 'workdir/projects' directory.
                As the Technical Consultant and Manger, your task is to refine the user requirements into clear and concise technical specifications.
                {self.__tip_section()}
                You must ensure, the team is procducing quality code in full.
                Make sure to consider the following user input: {user_input}
                Focus on identifying the key functionalities, constraints and understanding the project.
                Provide a detailed, well-structured set of technical specifications and guidance for the dev team.
                """
            ),
            expected_output=dedent(
                f"""
                A set of clear and concise technical specifications that accurately capture the user's requirements for the {user_input} project.
                The specifications should cover the key functionalities, constraints, and any additional considerations mentioned in the user input.
                """
            ),
            agent=agent,
            output_pydantic=TechnicalSpecifications
        )

    def initial_coder_task(self, agent, technical_specifications, user_input):
        logger.debug(f"Technical specifications: {technical_specifications}")
        logger.debug(f"User input: {user_input}")
        return Task(
            description=dedent(
                f"""
                Before commenting that a file doesn't exist, use the 'list_project_files' tool to check the files in the 'workdir/projects' directory.
                As the Initial Coder, your task is to generate clean, efficient, and well-documented code in full based on the technical specifications.
                {self.__tip_section()}
                Use the following technical specifications: {technical_specifications}
                Ensure that the code follows best practices and coding standards.
                Provide comments and documentation to enhance code readability and maintainability.
                Use the 'create_python_file' tool to create new Python files in the 'workdir/projects' directory.
                Use the 'create_markdown_file' tool to create new Markdown files in the 'workdir/projects' directory.
                Use the 'run_python_file' tool to run and test the Python code.
                Use the 'edit_python_file', 'read_python_file', 'write_python_file', and 'delete_python_file' tools to manipulate Python files in the 'workdir/projects' directory.
                Once the dev team and the tester have presented the functioning and requested code, end the chain and present to the user.
                """
            ),
            expected_output=dedent(
                f"""
                A clean, efficient, and well-documented code implementation that adheres to the provided technical specifications for the {user_input} & {technical_specifications} project.
                The code should follow best practices, include necessary comments, and be structured in a logical and maintainable manner.
                Once the dev team and the tester have presented the functioning and requested code, end the chain and present to the user.
                """
            ),
            agent=agent,
        )

    def senior_code_reviewer_task(self, agent, generated_code, technical_specifications, user_input):
        logger.debug(f"Generated code: {generated_code}")
        logger.debug(f"Technical specifications: {technical_specifications}")
        logger.debug(f"User input: {user_input}")
        return Task(
            description=dedent(
                f"""
                Before commenting that a file doesn't exist, use the 'list_project_files' tool to check the files in the 'workdir/projects' directory.
                Only review if the code is fully complete, if not send back to the coder to finish the code.
                As the Senior Code Reviewer, your task is to review the generated code and provide feedback and suggestions for improvement.
                {self.__tip_section()}
                Review the following generated code: {generated_code}
                Identify areas where the code can be optimized for performance, readability, and maintainability.
                Provide clear and actionable feedback to help improve the code quality.
                Use the 'read_python_file' tool to read the contents of Python files in the 'workdir/projects' directory.
                Use the 'edit_python_file' tool to suggest improvements and update the Python files in the 'workdir/projects' directory.
                Use the 'run_python_file' tool to test and run the Python code.
                """
            ),
            expected_output=dedent(
                f"""
                A comprehensive code review that provides constructive feedback and suggestions for improving the generated code for the {user_input} & {technical_specifications} project.
                The review should cover aspects such as code optimization, readability, maintainability, and adherence to best practices.
                """
            ),
            agent=agent,
        )

    def tester_task(self, agent, generated_code, technical_specifications, user_input):
        logger.debug(f"Generated code: {generated_code}")
        logger.debug(f"Technical specifications: {technical_specifications}")
        logger.debug(f"User input: {user_input}")
        return Task(
            description=dedent(
                f"""
                Before commenting that a file doesn't exist, use the 'list_project_files' tool to check the files in the 'workdir/projects' directory.
                Only test if the code is fully complete, if not send back to the devs to finish the code.
                As the Tester, your task is to develop comprehensive test cases and execute them against the generated code.
                {self.__tip_section()}
                Test the following generated code: {generated_code}
                Create test cases that cover various scenarios, edge cases, and potential bugs.
                Use the 'read_python_file' tool to read the contents of Python files in the 'workdir/projects' directory.
                Use the 'create_python_file' tool to create new test files in the 'workdir/projects' directory.
                Use the 'run_python_file' tool to execute the test cases and provide detailed feedback and bug reports.
                Even if you think you don't need to run the tests, you will run them.All tests create must be run.
                You must send the code back for review.
                """
            ),
            expected_output=dedent(
                """
                Final fully test and functioing requested python code:
                
                Please review the generated code files in the 'workdir/projects' to the dev team.
                """
            ),
            agent=agent,
        )