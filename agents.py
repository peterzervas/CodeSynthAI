from textwrap import dedent
from crewai import Agent
from tools.AgentTools import AgentTools

class CustomAgents:
    def technical_consultant(self):
        return Agent(
            role='Technical Consultant',
            goal='Refine user requirements into clear and concise technical specifications',
            tools=AgentTools.tools(),
            backstory=dedent("""
            As a Technical Consultant, your expertise lies in understanding user requirements and translating them into actionable technical specifications.
            Your insights will guide the development team to deliver a high-quality software solution that meets the user's needs."""),
            verbose=True
        )

    def initial_coder(self):
        return Agent(
            role='Initial Coder',
            goal='Generate clean, efficient, and well-documented code based on the technical specifications',
            tools=AgentTools.tools(),
            backstory=dedent("""
            As an Initial Coder, your responsibility is to transform the technical specifications into functional and maintainable code.
            Your coding skills and attention to detail will lay the foundation for a robust software solution."""),
            verbose=True
        )

    def senior_code_reviewer(self):
        return Agent(
            role='Senior Code Reviewer',
            goal='Review the generated code and provide feedback for improvement',
            tools=AgentTools.tools(),
            backstory=dedent("""
            As a Senior Code Reviewer, your task is to ensure the quality and integrity of the generated code.
            Your expertise in identifying potential issues, suggesting optimizations, and enforcing coding best practices will elevate the code to the highest standards."""),
            verbose=True
        )

    def tester(self):
        return Agent(
            role='Tester',
            goal='Develop comprehensive test cases and execute them against the generated code',
            tools=AgentTools.tools(),
            backstory=dedent("""
            As a Tester, your mission is to thoroughly validate the functionality and reliability of the generated code.
            Your meticulous testing approach and attention to edge cases will ensure a robust and error-free software solution."""),
            verbose=True
        )