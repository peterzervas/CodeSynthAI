import os
import uuid
from langchain.agents import tool
from langchain_experimental.utilities import PythonREPL

class AgentTools:
    @tool
    def python_repl(command: str) -> str:
        """Execute Python commands in a REPL environment."""
        python_repl = PythonREPL()
        return python_repl.run(command)
    
    @tool
    def create_python_project_files(file_name: str, file_content: str) -> str:
        """Create a Python file with the specified name and content in the project directory."""
        try:
            project_dir = f"./workdir"
            os.makedirs(project_dir, exist_ok=True)

            file_path = os.path.join(project_dir, file_name)
            with open(file_path, "w") as file:
                file.write(file_content)

            return f"Python file '{file_name}' created successfully in the project directory '{project_dir}'."
        except Exception as e:
            return f"Error creating Python file: {str(e)}"

    @tool
    def create_or_update_python_file(file_path: str, file_content: str) -> str:
        """Create or update a Python file with the specified content in the project directory."""
        try:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, "w") as file:
                file.write(file_content)
            return f"Python file '{file_path}' created or updated successfully."
        except Exception as e:
            return f"Error creating or updating Python file: {str(e)}"

    @tool
    def read_python_file(file_path: str) -> str:
        """Read the content of a Python file in the project directory."""
        try:
            with open(file_path, "r") as file:
                content = file.read()
            return content
        except Exception as e:
            return f"Error reading Python file: {str(e)}"


    def tools(self, *selected_tools):
        all_tools = [self.python_repl, self.create_python_project_files]
        return [tool for tool in all_tools if tool in selected_tools] if selected_tools else all_tools