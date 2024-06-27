import sys
from crewai import Task
from textwrap import dedent
from pydantic import BaseModel
from loguru import logger

logger.remove()
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

    def requirements_analyst_task(self, agent, user_input):
        logger.debug(f"User input: {user_input}")
        return Task(
            description=dedent(
                f"""
                Before commenting that a file doesn't exist, use the 'list_files' tool to check the files in the 'C:\\workdir\\projects' directory.
                As the Requirements Analyst, your task is to analyze the user requirements, identify potential ambiguities or gaps, and gather necessary clarifications to create a comprehensive and clear set of technical requirements.
                {self.__tip_section()}
                You must ensure the team is producing quality code in full.
                Make sure to consider the following user input: {user_input}
                Focus on understanding the project scope, identifying key functionalities, constraints, and performance criteria.
                Provide a detailed, well-structured set of technical requirements and guidance for the development team.
                """
            ),
            expected_output=dedent(
                f"""
                A comprehensive set of technical requirements that accurately capture the user's needs and expectations for the {user_input} project.
                The requirements should be clear, unambiguous, and cover all essential aspects of the project, including functional and non-functional requirements.
                """
            ),
            agent=agent,
            output_pydantic=TechnicalSpecifications
        )

    def code_generator_task(self, agent, technical_specifications, user_input):
        logger.debug(f"Technical specifications: {technical_specifications}")
        logger.debug(f"User input: {user_input}")
        return Task(
            description=dedent(
                f"""
                Before commenting that a file doesn't exist, use the 'list_files' tool to check the files in the 'C:\\workdir\\projects' directory.
                As the Code Generator, your task is to generate clean, efficient, and well-documented code based on the technical requirements.
                {self.__tip_section()}
                Use the following technical requirements: {technical_specifications}
                Ensure that the code follows best practices, design patterns, and coding standards.
                Provide meaningful comments and documentation to enhance code readability and maintainability.
                Use the 'create_directory' tool to create new directories for organizing the project files.
                Use the 'create_python_file' tool to create new Python files in the 'C:\\workdir\\projects' directory.
                Use the 'create_markdown_file' tool to create new Markdown files in the 'C:\\workdir\\projects' directory.
                Use the 'run_python_file' tool to run and test the Python code.
                Use the 'edit_file', 'read_file', 'append_to_file', and 'delete_file' tools to manipulate files in the 'C:\\workdir\\projects' directory.
                """
            ),
            expected_output=dedent(
                f"""
                A clean, efficient, and well-documented code implementation that adheres to the provided technical requirements for the {user_input} & {technical_specifications} project.
                The code should follow best practices, include necessary comments, and be structured in a logical and maintainable manner.
                """
            ),
            agent=agent,
        )

    def code_quality_assurance_task(self, agent, generated_code, technical_specifications, user_input):
        logger.debug(f"Generated code: {generated_code}")
        logger.debug(f"Technical specifications: {technical_specifications}")
        logger.debug(f"User input: {user_input}")
        return Task(
            description=dedent(
                f"""
                Before commenting that a file doesn't exist, use the 'list_files' tool to check the files in the 'C:\\workdir\\projects' directory.
                Only review if the code is fully complete; if not, send it back to the Code Generator to finish the code.
                As the Code Quality Assurance expert, your task is to review the generated code and provide feedback and suggestions for improvement.
                {self.__tip_section()}
                Review the following generated code: {generated_code}
                Identify areas where the code can be optimized for performance, readability, and maintainability.
                Provide clear and actionable feedback to help improve the code quality.
                Use the 'read_file' tool to read the contents of files in the 'C:\\workdir\\projects' directory.
                Use the 'edit_file' tool to suggest improvements and update the files in the 'C:\\workdir\\projects' directory.
                Use the 'format_code' tool to format the code according to the project's coding style guidelines.
                Use the 'lint_code' tool to identify potential issues, style violations, and code quality problems.
                """
            ),
            expected_output=dedent(
                f"""
                A comprehensive code review that provides constructive feedback and suggestions for improving the generated code for the {user_input} & {technical_specifications} project.
                The review should cover aspects such as code optimization, readability, maintainability, adherence to best practices, and potential issues identified by linting tools.
                """
            ),
            agent=agent,
        )

    def quality_assurance_engineer_task(self, agent, generated_code, technical_specifications, user_input):
        logger.debug(f"Generated code: {generated_code}")
        logger.debug(f"Technical specifications: {technical_specifications}")
        logger.debug(f"User input: {user_input}")
        return Task(
            description=dedent(
                f"""
                Before commenting that a file doesn't exist, use the 'list_files' tool to check the files in the 'C:\\workdir\\projects' directory.
                Only test if the code is fully complete; if not, send it back to the development team to finish the code.
                As the Quality Assurance Engineer, your task is to develop comprehensive test cases and execute them against the generated code.
                {self.__tip_section()}
                Test the following generated code: {generated_code}
                Create test cases that cover various scenarios, edge cases, and potential bugs.
                Use the 'read_file' tool to read the contents of files in the 'C:\\workdir\\projects' directory.
                Use the 'create_python_file' tool to create new test files in the 'C:\\workdir\\projects' directory.
                Use the 'run_tests' tool to execute the test cases and provide detailed feedback and bug reports.
                Even if you think you don't need to run the tests, you will run them. All tests created must be run.
                You must send the code back to the Code Quality Assurance expert for a final review.
                """
            ),
            expected_output=dedent(
                """
                Comprehensive test cases and test results for the generated code.
                The test cases should cover various scenarios, edge cases, and potential bugs to ensure the code's correctness and reliability.
                Detailed feedback and bug reports should be provided based on the test results.
                The code should be sent back to the Code Quality Assurance expert for a final review.
                """
            ),
            agent=agent,
        )