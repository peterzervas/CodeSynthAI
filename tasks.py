from textwrap import dedent
from crewai import Task

class CustomTasks:
    def __init__(self, topic, section):
        self.topic = topic
        self.section = section

    def technical_consultant_task(self, agent, user_input):
        return Task(
            description=dedent(
                f"""
                As the Technical Consultant Manager, your task is to manage and coordinate the project development process.
                     
                Your responsibilities include:
                1. Refining the user requirements into clear and concise technical specifications.
                2. Coordinating the efforts of the development team (Initial Coder, Senior Code Reviewer, and Tester) to deliver a high-quality software solution.
                3. Ensuring that the project meets the user's expectations and requirements.
                
                User Input: {user_input}
                
                Your Final answer should include:
                1. A summary of the project's status and progress.
                2. Any important updates or decisions made during the development process.
                3. The next steps and recommendations for the project.
                """
            ),
            expected_output=dedent(
                f"""
                Project Status Summary:
                1. Technical specifications refined and documented.
                2. Initial code generated and reviewed by the Senior Code Reviewer.
                3. Code tested and verified by the Tester.
                
                Important Updates and Decisions:
                1. ...
                2. ...
                
                Next Steps and Recommendations:
                1. Proceed with the next phase of development.
                2. Address any identified issues or bugs.
                3. Prepare the project for deployment and handover to the customer.
                """
            ),
            agent=agent,
        )

    def initial_coder_task(self, agent, technical_specifications, user_input):
        return Task(
            description=dedent(
                f"""
                As the Initial Coder, your task is to generate clean, efficient, and well-documented Python code based on the technical specifications.   
                Technical Specifications: {technical_specifications}
                Ensure that the Python code follows best practices and coding standards. Provide comments and docstrings to enhance code readability and maintainability.
                Create as many files as required to build the project in the workdir. Organize the code into appropriate files and directories.  
                """
            ),
            expected_output=dedent(
                f"""
                A clean, efficient, and well-documented Python code implementation that adheres to the provided technical specifications for the {user_input} project based on the following specifications:
                {technical_specifications}
                """
            ),
            agent=agent,
        )

    def senior_code_reviewer_task(self, agent, generated_code, technical_specifications, user_input):
        return Task(
            description=dedent(
                f"""
                As the Senior Code Reviewer, your task is to review the generated code and provide feedback for improvement.
                Generated Code: {generated_code}
                Technical Specifications: {technical_specifications}
                Identify areas where the code can be optimized for performance, readability, and maintainability. Provide clear and actionable feedback to help improve the code quality.
                """
            ),
            expected_output=dedent(
                f"""
                A comprehensive code review that provides constructive feedback and suggestions for improving the generated code for the {user_input} project based on the technical specifications:
                {technical_specifications}
                """
            ),
            agent=agent,
        )

    def tester_task(self, agent, generated_code, technical_specifications, user_input):
        return Task(
            description=dedent(
                f"""
                As the Tester, your task is to develop test cases and execute them against the generated code.
                Generated Code: {generated_code}
                Technical Specifications: {technical_specifications}
                Create test cases that cover various scenarios, edge cases, and potential bugs. Provide detailed feedback and bug reports.
                Use the `python_repl` tool to test and run the Python code.
                Your Final answer must be the full requested Python code, only the Python code and nothing else, not the test code.
                """
            ),
            expected_output=dedent(
                f"""
                Test Results Summary:
                1. Number of test cases developed: X
                2. Number of test cases passed: Y
                3. Number of test cases failed: Z
                
                Identified Bugs and Issues:
                1. ...
                2. ...
                
                Recommendations for Improvement:
                1. ...
                2. ...
                
                Please review the generated code files in the project directory for more details.
                """
            ),
            agent=agent,
        )