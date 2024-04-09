import os
import subprocess
from langchain.agents import tool

class AgentTools:
    @tool
    def create_python_file(file_name: str, content: str):
        """
        Create a new Python file in the 'workdir/projects' directory with the given file name and content.
        Example:
        - file_name: 'example.py'
        - content: 'print("Hello, World!")'
        """
        file_path = os.path.join("workdir", "projects", file_name)
        file_path = os.path.normpath(file_path)
        with open(file_path, "w") as file:
            file.write(content)
        return f"Python file '{file_name}' created successfully."

    @tool
    def create_markdown_file(file_name: str, content: str):
        """
        Create a new Markdown file in the 'workdir/projects' directory with the given file name and content.
        Example:
        - file_name: 'example.md'
        - content: '# Hello, World!'
        """
        file_path = os.path.join("workdir", "projects", file_name)
        file_path = os.path.normpath(file_path)
        with open(file_path, "w") as file:
            file.write(content)
        return f"Markdown file '{file_name}' created successfully."

    @tool
    def run_python_file(file_name: str):
        """
        Run a Python file in the 'workdir/projects' directory with the given file name.
        Example:
        - file_name: 'example.py'
        """
        file_path = os.path.join("workdir", "projects", file_name)
        file_path = os.path.normpath(file_path)
        try:
            subprocess.run(["python", file_path], check=True)
            return f"Python file '{file_name}' executed successfully."
        except FileNotFoundError as e:
            return f"Error: File '{file_name}' not found in the 'workdir/projects' directory. Please make sure the file exists."
        except subprocess.CalledProcessError as e:
            return f"Error executing Python file: {str(e)}"

    @tool
    def edit_python_file(file_name: str, content: str):
        """
        Edit the content of a Python file in the 'workdir/projects' directory with the given file name.
        Example:
        - file_name: 'example.py'
        - content: 'print("Hello, World! Updated.")'
        """
        file_path = os.path.join("workdir", "projects", file_name)
        file_path = os.path.normpath(file_path)
        with open(file_path, "w") as file:
            file.write(content)
        return f"Python file '{file_name}' edited successfully."

    @tool
    def read_python_file(file_name: str):
        """
        Read the content of a files in the 'workdir/projects' directory with the given file name.
        Example:
        - file_name: 'example.py'
        """
        file_path = os.path.join("workdir", "projects", file_name)
        file_path = os.path.normpath(file_path)
        try:
            with open(file_path, "r") as file:
                content = file.read()
            return content
        except FileNotFoundError as e:
            return f"Error: File '{file_name}' not found in the 'workdir/projects' directory. Please make sure the file exists."

    @tool
    def write_python_file(file_name: str, content: str):
        """
        Write content to a Python file in the 'workdir/projects' directory with the given file name.
        Example:
        - file_name: 'example.py'
        - content: 'print("Hello, World! Appended.")'
        """
        file_path = os.path.join("workdir", "projects", file_name)
        file_path = os.path.normpath(file_path)
        with open(file_path, "a") as file:
            file.write(content)
        return f"Content written to Python file '{file_name}' successfully."

    @tool
    def delete_python_file(file_name: str):
        """
        Delete a Python file in the 'workdir/projects' directory with the given file name.
        Example:
        - file_name: 'example.py'
        """
        file_path = os.path.join("workdir", "projects", file_name)
        file_path = os.path.normpath(file_path)
        try:
            os.remove(file_path)
            return f"Python file '{file_name}' deleted successfully."
        except FileNotFoundError as e:
            return f"Error: File '{file_name}' not found in the 'workdir/projects' directory. Please make sure the file exists."
    
    @tool
    def list_project_files():
        """
        List all the files in the 'workdir/projects' directory.
        """
        project_dir = os.path.join("workdir", "projects")
        project_dir = os.path.normpath(project_dir)
        try:
            files = os.listdir(project_dir)
            if files:
                file_list = "\n".join(files)
                return f"Files in the 'workdir/projects' directory:\n{file_list}"
            else:
                return "No files found in the 'workdir/projects' directory."
        except FileNotFoundError as e:
            return "Error: 'workdir/projects' directory not found. Please make sure the directory exists."

    def tools(self):
        return [
            self.create_python_file,
            self.create_markdown_file,
            self.run_python_file,
            self.edit_python_file,
            self.read_python_file,
            self.write_python_file,
            self.delete_python_file,
            self.list_project_files
        ]