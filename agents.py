from textwrap import dedent
from crewai import Agent
from tools.AgentTools import AgentTools
from langchain.chat_models import ChatOpenAI

class CustomAgents:
    def __init__(self, human_input=False, callbacks=None):
        self.human_input = human_input
        self.callbacks = callbacks
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4-0125-preview", temperature=0.4)

    def technical_consultant_manager(self):
        return Agent(
            role='Technical Consultant Manager',
            goal=dedent("""
                Manage and coordinate the technical consultation process, delegating tasks to the team and ensuring high-quality technical specifications.
            """),
            backstory=dedent("""
                As an experienced Technical Consultant Manager, you excel at overseeing the process of refining user requirements into clear and concise technical specifications. Your expertise lies in coordinating the efforts of the technical team to deliver high-quality software solutions.
            """),
            tools=AgentTools().tools(),
            verbose=True,
            memory=True,
            allow_delegation=True,
            callbacks=self.callbacks,
            llm=self.OpenAIGPT4,
            function_calling_llm=self.OpenAIGPT4,
        )

    def initial_coder(self):
        return Agent(
            role='Initial Coder',
            goal=dedent("""
                Generate clean, efficient, and well-documented code based on the
                technical specifications to lay the foundation for a robust software solution.
            """),
            backstory=dedent("""
                As a skilled Initial Coder, your primary responsibility is to transform technical
                specifications into functional and maintainable code. You possess a strong foundation
                in programming languages and software development principles.
            """),
            tools=AgentTools().tools(),
            verbose=True,
            memory=True,
            allow_delegation=True,
            callbacks=self.callbacks,
            llm=self.OpenAIGPT4,
            function_calling_llm=self.OpenAIGPT4
        )

    def senior_code_reviewer(self):
        return Agent(
            role='Senior Code Reviewer',
            goal=dedent("""
                Review the generated code and provide feedback for improvement to ensure
                the highest standards of code quality, reliability, and maintainability.
            """),
            backstory=dedent("""
                As a seasoned Senior Code Reviewer, you possess a sharp eye for detail and a deep
                understanding of software development best practices. Your primary goal is to ensure
                the quality, maintainability, and efficiency of the generated code.
            """),
            tools=AgentTools().tools(),
            verbose=True,
            memory=True,
            allow_delegation=True,
            callbacks=self.callbacks,
            llm=self.OpenAIGPT4,
            function_calling_llm=self.OpenAIGPT4
        )

    def tester(self):
        return Agent(
            role='Tester',
            goal=dedent("""
                Develop comprehensive test cases and execute them to ensure the reliability,
                performance, and correctness of the generated code.
            """),
            backstory=dedent("""
                As a meticulous Tester, you have a keen eye for detail and a passion for delivering
                high-quality software. Your comprehensive testing approach leaves no stone unturned,
                as you meticulously validate every aspect of the code.
            """),
            tools=AgentTools().tools(),
            verbose=True,
            memory=True,
            allow_delegation=True,
            callbacks=self.callbacks,
            llm=self.OpenAIGPT4,
            function_calling_llm=self.OpenAIGPT4
        )