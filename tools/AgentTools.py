import os
from langchain.agents import tool
from langchain_experimental.utilities import PythonREPL

class AgentTools:
    @tool
    def python_repl(command: str) -> str:
        """Execute Python commands in a REPL environment.

        This tool allows you to run Python code within a REPL (Read-Eval-Print Loop)
        environment. It executes the provided command and returns the output as a string.

        Args:
            command (str): The Python command or code snippet to execute.

        Returns:
            str: The output of the executed Python command.

        Examples:
            >>> python_repl("print('Hello, World!')")
            "Hello, World!"

            >>> python_repl('''
            ... def greet(name):
            ...     return f"Hello, {name}!"
            ...
            ... print(greet("Alice"))
            ... ''')
            "Hello, Alice!"
        """
        python_repl = PythonREPL()
        return python_repl.run(command)

    @tool
    def create_python_project_files(project_name: str, main_content: str, utils_content: str, config_content: str, requirements_content: str, readme_content: str):
        """Create Python project files based on the provided content.

        Args:
            project_name (str): The name of the Python project.
            main_content (str): The content of the main.py file.
            utils_content (str): The content of the utils.py file.
            config_content (str): The content of the config.py file.
            requirements_content (str): The content of the requirements.txt file.
            readme_content (str): The content of the README.md file.

        Returns:
            str: A message indicating the success or failure of the project creation.
        """
        try:
            # Create the project directory
            project_dir = f"./workdir/{project_name}"
            os.makedirs(project_dir, exist_ok=True)

            # Create and write the main.py file
            with open(os.path.join(project_dir, "main.py"), "w") as file:
                file.write(main_content)

            # Create and write the utils.py file
            with open(os.path.join(project_dir, "utils.py"), "w") as file:
                file.write(utils_content)

            # Create and write the config.py file
            with open(os.path.join(project_dir, "config.py"), "w") as file:
                file.write(config_content)

            # Create and write the requirements.txt file
            with open(os.path.join(project_dir, "requirements.txt"), "w") as file:
                file.write(requirements_content)

            # Create and write the README.md file
            with open(os.path.join(project_dir, "README.md"), "w") as file:
                file.write(readme_content)

            return f"Python project '{project_name}' created successfully with the specified files."
        except Exception as e:
            return f"Error creating Python project: {str(e)}"

    def tools(self, *selected_tools):
        all_tools = [self.python_repl, self.create_python_project_files]
        return [tool for tool in all_tools if tool in selected_tools] if selected_tools else all_tools