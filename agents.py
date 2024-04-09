import os
from dotenv import load_dotenv
from textwrap import dedent
from crewai import Agent
from tools.AgentTools import AgentTools
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from utils import print_agent_output

# Load environment variables from .env file
load_dotenv()

# Load Anthropic API key from environment variable
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")

class CustomAgents:
    def __init__(self, human_input=False, callbacks=None):
        self.human_input = human_input
        self.callbacks = callbacks

    def get_llm(self, api_choice, model_choice):
        if api_choice == "OpenAI":
            return ChatOpenAI(model_name=model_choice, temperature=0.7)
        else:
            return ChatAnthropic(model=model_choice, anthropic_api_key=ANTHROPIC_API_KEY)

    def get_manager_llm(self, api_choice, model_choice):
        if api_choice == "OpenAI":
            return ChatOpenAI(model_name="gpt-4", temperature=0.4)
        else:
            return ChatAnthropic(model="claude-3-sonnet-20240229", anthropic_api_key=ANTHROPIC_API_KEY)

    def technical_consultant(self, api_choice, model_choice):
        agent = Agent(
            role='Technical Consultant',
            goal='Refine user requirements into clear and concise technical specifications',
            tools=AgentTools().tools(),
            backstory=dedent("""
            As a Technical Consultant, your expertise lies in understanding user requirements and translating them into actionable technical specifications.
            Your insights will guide the development team to deliver a high-quality software solution that meets the user's needs.
            """),
            verbose=True,
            memory=True,
            allow_delegation=True,
            callbacks=self.callbacks,
            llm=self.get_llm(api_choice, model_choice),
            max_iter=35,
            step_callback=lambda x: print_agent_output(x, "Technical Consultant")
        )
        
        return agent

    def initial_coder(self, api_choice, model_choice):
        agent = Agent(
            role='Initial Coder',
            goal='Generate clean, efficient, and well-documented code based on the technical specifications',
            tools=AgentTools().tools(),
            backstory=dedent("""
            As an Initial Coder, your responsibility is to transform the technical specifications into functional and maintainable code.
            Your coding skills and attention to detail will lay the foundation for a robust software solution.
            """),
            verbose=True,
            memory=True,
            allow_delegation=False,
            callbacks=self.callbacks,
            llm=self.get_llm(api_choice, model_choice),
            max_iter=35,
            step_callback=lambda x: print_agent_output(x, "Initial Coder")
        )
        
        return agent

    def senior_code_reviewer(self, api_choice, model_choice):
        agent = Agent(
            role='Senior Code Reviewer',
            goal='Review the generated code and provide feedback for improvement',
            tools=AgentTools().tools(),
            backstory=dedent("""
            As a Senior Code Reviewer, your task is to ensure the quality and integrity of the generated code.
            Your expertise in identifying potential issues, suggesting optimizations, and enforcing coding best practices will elevate the code to the highest standards.
            """),
            verbose=True,
            memory=True,
            allow_delegation=False,
            callbacks=self.callbacks,
            llm=self.get_llm(api_choice, model_choice),
            max_iter=35,
            step_callback=lambda x: print_agent_output(x, "Senior Code Reviewer")
        )
        
        return agent

    def tester(self, api_choice, model_choice):
        agent = Agent(
            role='Tester',
            goal='Develop comprehensive test cases and execute them against the generated code',
            tools=AgentTools().tools(),
            backstory=dedent("""
            As a Tester, your mission is to thoroughly validate the functionality and reliability of the generated code.
            """),
            verbose=True,
            memory=True,
            allow_delegation=True,
            callbacks=self.callbacks,
            llm=self.get_llm(api_choice, model_choice),
            max_iter=35,
            step_callback=lambda x: print_agent_output(x, "Tester")
        )
        
        return agent