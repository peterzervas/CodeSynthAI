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
            return ChatOpenAI(model_name="claude-3-5-sonnet-20240620", temperature=0.4)
        else:
            return ChatAnthropic(model="claude-3-5-sonnet-20240620", anthropic_api_key=ANTHROPIC_API_KEY)

    def requirements_analyst(self, api_choice, model_choice):
        agent = Agent(
            role='Requirements Analyst',
            goal='Analyze user requirements, identify potential ambiguities or gaps, and gather necessary clarifications to create a comprehensive and clear set of technical requirements',
            tools=AgentTools().tools(),
            backstory=dedent("""
            As a Requirements Analyst, your expertise lies in understanding user needs, asking the right questions, and translating them into well-defined technical requirements that guide the development process.
            """),
            verbose=True,
            memory=True,
            allow_delegation=True,
            callbacks=self.callbacks,
            llm=self.get_llm(api_choice, model_choice),
            max_iter=5,
            step_callback=lambda x: print_agent_output(x, "Requirements Analyst")
        )
        
        return agent

    def code_generator(self, api_choice, model_choice):
        agent = Agent(
            role='Code Generator',
            goal='Generate code based on the technical requirements, focusing on functionality, readability, and adherence to coding best practices',
            tools=AgentTools().tools(),
            backstory=dedent("""
            As a Code Generator, your primary responsibility is to transform the technical requirements into working code. Your coding skills, knowledge of design patterns, and attention to code quality ensure the generated code is efficient, maintainable, and aligned with the project's goals.
            """),
            verbose=True,
            memory=True,
            allow_delegation=True,
            callbacks=self.callbacks,
            llm=self.get_llm(api_choice, model_choice),
            max_iter=15,
            step_callback=lambda x: print_agent_output(x, "Code Generator")
        )
        
        return agent

    def code_quality_assurance(self, api_choice, model_choice):
        agent = Agent(
            role='Code Quality Assurance',
            goal='Review the generated code to ensure it meets the project\'s quality standards, follows best practices, and is free of potential issues or bugs',
            tools=AgentTools().tools(),
            backstory=dedent("""
            As a Code Quality Assurance expert, your task is to carefully examine the generated code, identify areas for improvement, and provide constructive feedback. Your keen eye for detail and deep understanding of code quality principles help elevate the codebase to the highest standards.
            """),
            verbose=True,
            memory=True,
            allow_delegation=True,
            callbacks=self.callbacks,
            llm=self.get_llm(api_choice, model_choice),
            max_iter=15,
            step_callback=lambda x: print_agent_output(x, "Code Quality Assurance")
        )
        
        return agent

    def quality_assurance_engineer(self, api_choice, model_choice):
        agent = Agent(
            role='Quality Assurance Engineer',
            goal='Develop comprehensive test cases based on the technical requirements and perform thorough testing to ensure the code meets the specified functionality and performance criteria',
            tools=AgentTools().tools(),
            backstory=dedent("""
            As a Quality Assurance Engineer, your mission is to verify the correctness, reliability, and performance of the generated code. You create test plans, design test cases, and execute them meticulously to identify any defects or deviations from the expected behavior.
            """),
            verbose=True,
            memory=True,
            allow_delegation=True,
            callbacks=self.callbacks,
            llm=self.get_llm(api_choice, model_choice),
            max_iter=5,
            step_callback=lambda x: print_agent_output(x, "Quality Assurance Engineer")
        )
        
        return agent