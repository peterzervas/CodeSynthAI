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
                Make sure to consider the following user input:
                {user_input}
                Focus on identifying the key functionalities and constraints of the project. Provide a detailed and well-structured set of technical specifications.
                """
            ),
            expected_output = dedent(
                f"""
                A set of clear and concise technical specifications that accurately capture the user's requirements for the {user_input} project.
                The specifications should cover the key functionalities, constraints, and any additional considerations mentioned in the user input.
                The technical specifications should include the following sections:
                1. Introduction
                - Purpose and scope of the project
                - High-level overview of the system
                2. Functional Requirements
                - Detailed description of each functional requirement
                - User stories or use cases to illustrate the functionalities
                - Input and output formats for each functionality
                3. Non-Functional Requirements
                - Performance requirements (e.g., response time, throughput)
                - Scalability requirements
                - Security requirements
                - Usability and accessibility requirements
                4. System Architecture
                - Overview of the system architecture
                - Description of major components and their interactions
                - Data flow and processing pipeline
                5. Constraints and Assumptions
                - Technical constraints (e.g., compatible platforms, programming languages)
                - Business constraints (e.g., budget, timeline)
                - Any assumptions made during the specification process
                6. Glossary
                - Definition of key terms and acronyms used in the specifications
                The technical specifications should be well-organized, unambiguous, and provide sufficient detail for the development team to begin the implementation phase.
                """
            ),
            agent=agent,
        )

    def initial_coder_task(self, agent, technical_specifications, user_input):
        logger.debug(f"Technical specifications: {technical_specifications}")
        logger.debug(f"User input: {user_input}")
        return Task(
        description = dedent(
            f"""
            As the Initial Coder, your task is to generate clean, efficient, and well-documented Python code based on the technical specifications.
            {self.__tip_section()}
            Use the following technical specifications:
            {technical_specifications}
            Ensure that the Python code follows best practices and coding standards. Provide comments and docstrings to enhance code readability and maintainability.
            """
        ),
        expected_output = dedent(
            f"""
            A clean, efficient, and well-documented Python code implementation that adheres to the provided technical specifications for the {user_input} project based on the following specifications:
            {technical_specifications}
            The Python code should exhibit the following characteristics:
            1. Code Quality
            - Follow PEP 8 style guide and Python best practices
            - Use meaningful variable and function names that accurately describe their purpose
            - Keep the code modular and organize it into logical sections
            - Handle edge cases and potential errors gracefully
            2. Efficiency
            - Optimize code for performance, considering time and space complexity
            - Utilize appropriate data structures and algorithms to achieve efficient execution
            - Minimize redundant computations and unnecessary resource usage
            3. Documentation
            - Provide a docstring for each function and class, describing its purpose, parameters, and return values
            - Include inline comments to clarify complex or non-obvious code segments
            - Maintain a README file that provides an overview of the project, installation instructions, and usage examples
            4. Readability and Maintainability
            - Use consistent indentation and formatting throughout the codebase
            - Break down larger functions or classes into smaller, more manageable units
            - Use descriptive and meaningful names for variables, functions, and classes
            - Avoid excessive nesting and keep the code flow simple and intuitive
            The generated Python code should be thoroughly tested to ensure it meets the specified requirements and functions as expected. Include appropriate unit tests to verify the correctness of critical components.
            The Python code should be organized into the following files:
            - `main.py`: The entry point of the application
            - `utils.py`: Helper functions and utility modules
            - `config.py`: Configuration settings and constants
            - `requirements.txt`: List of dependencies and their versions
            - `README.md`: Project documentation and usage instructions
            Ensure that the generated Python code is compatible with the specified Python version and any additional dependencies or frameworks mentioned in the technical specifications.
            Use the REPL tool to run and test your code.
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
                Use the REPL tool to run and test your code.
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
                Use the REPL tool to run and test your code.
                """
            ),
            expected_output=dedent(
                f"""
                A set of comprehensive test cases and their execution results for the {generated_code} based from {technical_specifications} & {user_input}.
                The test cases should cover different scenarios, edge cases, and potential bugs to ensure the code's correctness and reliability.
                Detailed feedback and bug reports should be provided based on the test execution results.
                Upon successful completion of the testing phase, you will present the final, validated code as the output.
                """
            ),
            agent=agent,
        )