import os
from langchain.agents import tool
from langchain_experimental.utilities import PythonREPL

class AgentTools:
    @tool
    def python_repl(command: str):
        """Execute Python commands in a REPL environment."""
        python_repl = PythonREPL()
        return python_repl.run(command)

    def tools(self):
        return [AgentTools.python_repl]