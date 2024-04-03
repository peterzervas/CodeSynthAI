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
            description = dedent(
                f"""
                As the Technical Consultant, your task is to refine the user requirements into clear and concise technical specifications.
                {self.__tip_section()}
                Make sure to consider the following user input: {user_input}
                Focus on identifying the key functionalities and constraints of the project.
                Provide a detailed and well-structured set of technical specifications.
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
                As the Initial Coder, your task is to generate clean, efficient, and well-documented code based on the technical specifications.
                {self.__tip_section()}
                Use the following technical specifications: {technical_specifications}
                Ensure that the code follows best practices and coding standards.
                Provide comments and documentation to enhance code readability and maintainability.
                """
            ),
            expected_output=dedent(
                f"""
                A clean, efficient, and well-documented code implementation that adheres to the provided technical specifications for the {user_input} & {technical_specifications} project.
                The code should follow best practices, include necessary comments, and be structured in a logical and maintainable manner.
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
                As the Senior Code Reviewer, your task is to review the generated code and provide feedback and suggestions for improvement.
                {self.__tip_section()}
                Review the following generated code: {generated_code}
                Identify areas where the code can be optimized for performance, readability, and maintainability.
                Provide clear and actionable feedback to help improve the code quality.
                """
            ),
            expected_output=dedent(
                f"""
                A comprehensive code review that provides constructive feedback and suggestions for improving the generated code for the {user_input} & {technical_specifications}  project.
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
                As the Tester, your task is to develop comprehensive test cases and execute them against the generated code.
                {self.__tip_section()}
                Test the following generated code: {generated_code}
                Create test cases that cover various scenarios, edge cases, and potential bugs.
                Use the Python REPL to execute the test cases and provide detailed feedback and bug reports.
                Your Final answer must be the full requested python code, only the python code and nothing else not the test code.
                """
            ),
            expected_output=dedent(
                f"""
                A set of comprehensive test cases and their execution results for the {generated_code} based from {technical_specifications} & {user_input}.
                The test cases should cover different scenarios, edge cases, and potential bugs to ensure the code's correctness and reliability.
                Detailed feedback and bug reports should be provided based on the test execution results.
                """
            ),
            agent=agent,
        )