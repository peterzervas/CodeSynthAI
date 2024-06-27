import os
import subprocess
from langchain.agents import tool

class AgentTools:
    PROJECT_DIR = os.path.join("C:", "workdir", "projects")

    @tool
    def create_python_file(file_name: str, content: str) -> str:
        """
        Create a new Python file in the 'C:\workdir\projects' directory with the given file name and content.
        Example:
        - file_name: 'example.py'
        - content: 'print("Hello, World!")'
        """
        file_path = os.path.join(AgentTools.PROJECT_DIR, file_name)
        file_path = os.path.normpath(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            file.write(content)
        return f"Python file '{file_name}' created successfully in 'C:\workdir\projects'."

    @tool
    def create_markdown_file(file_name: str, content: str) -> str:
        """
        Create a new Markdown file in the 'C:\workdir\projects' directory with the given file name and content.
        Example:
        - file_name: 'example.md'
        - content: '# Hello, World!'
        """
        file_path = os.path.join(AgentTools.PROJECT_DIR, file_name)
        file_path = os.path.normpath(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            file.write(content)
        return f"Markdown file '{file_name}' created successfully in 'C:\workdir\projects'."

    @tool
    def run_python_file(file_name: str) -> str:
        """
        Run a Python file in the 'C:\workdir\projects' directory with the given file name.
        Example:
        - file_name: 'example.py'
        """
        file_path = os.path.join(AgentTools.PROJECT_DIR, file_name)
        file_path = os.path.normpath(file_path)
        try:
            result = subprocess.run(["python", file_path], capture_output=True, text=True, check=True)
            return f"Python file '{file_name}' executed successfully. Output:\n{result.stdout}"
        except FileNotFoundError as e:
            return f"Error: File '{file_name}' not found in 'C:\workdir\projects'. Please make sure the file exists."
        except subprocess.CalledProcessError as e:
            return f"Error executing Python file: {str(e)}. stderr:\n{e.stderr}"

    @tool
    def edit_file(file_name: str, content: str) -> str:
        """
        Edit the content of a file in the 'C:\workdir\projects' directory with the given file name.
        Example:
        - file_name: 'example.py'
        - content: 'print("Hello, World! Updated.")'
        """
        file_path = os.path.join(AgentTools.PROJECT_DIR, file_name)
        file_path = os.path.normpath(file_path)
        with open(file_path, "w") as file:
            file.write(content)
        return f"File '{file_name}' edited successfully in 'C:\workdir\projects'."

    @tool
    def read_file(file_name: str) -> str:
        """
        Read the content of a file in the 'C:\workdir\projects' directory with the given file name.
        Example:
        - file_name: 'example.py'
        """
        file_path = os.path.join(AgentTools.PROJECT_DIR, file_name)
        file_path = os.path.normpath(file_path)
        try:
            with open(file_path, "r") as file:
                content = file.read()
            return f"Content of file '{file_name}':\n{content}"
        except FileNotFoundError as e:
            return f"Error: File '{file_name}' not found in 'C:\workdir\projects'. Please make sure the file exists."

    @tool
    def append_to_file(file_name: str, content: str) -> str:
        """
        Append content to a file in the 'C:\workdir\projects' directory with the given file name.
        Example:
        - file_name: 'example.py'
        - content: '\nprint("Appended line.")'
        """
        file_path = os.path.join(AgentTools.PROJECT_DIR, file_name)
        file_path = os.path.normpath(file_path)
        with open(file_path, "a") as file:
            file.write(content)
        return f"Content appended to file '{file_name}' successfully in 'C:\workdir\projects'."

    @tool
    def delete_file(file_name: str) -> str:
        """
        Delete a file in the 'C:\workdir\projects' directory with the given file name.
        Example:
        - file_name: 'temp.txt'
        """
        file_path = os.path.join(AgentTools.PROJECT_DIR, file_name)
        file_path = os.path.normpath(file_path)
        try:
            os.remove(file_path)
            return f"File '{file_name}' deleted successfully from 'C:\workdir\projects'."
        except FileNotFoundError as e:
            return f"Error: File '{file_name}' not found in 'C:\workdir\projects'. Please make sure the file exists."

    @tool
    def list_files() -> str:
        """
        List all the files in the 'C:\workdir\projects' directory.
        """
        try:
            files = os.listdir(AgentTools.PROJECT_DIR)
            if files:
                file_list = "\n".join(files)
                return f"Files in 'C:\workdir\projects':\n{file_list}"
            else:
                return "No files found in 'C:\workdir\projects'."
        except FileNotFoundError as e:
            return "Error: 'C:\workdir\projects' directory not found. Please make sure the directory exists."

    @tool
    def search_files(search_query: str) -> str:
        """
        Search for files in the 'C:\workdir\projects' directory that match the given search query.
        Example:
        - search_query: '.py'
        """
        try:
            files = [file for file in os.listdir(AgentTools.PROJECT_DIR) if search_query in file]
            if files:
                file_list = "\n".join(files)
                return f"Files matching '{search_query}' in 'C:\workdir\projects':\n{file_list}"
            else:
                return f"No files matching '{search_query}' found in 'C:\workdir\projects'."
        except FileNotFoundError as e:
            return "Error: 'C:\workdir\projects' directory not found. Please make sure the directory exists."

    @tool
    def create_directory(directory_name: str) -> str:
        """
        Create a new directory in the 'C:\workdir\projects' directory with the given directory name.
        Example:
        - directory_name: 'my_project'
        """
        directory_path = os.path.join(AgentTools.PROJECT_DIR, directory_name)
        directory_path = os.path.normpath(directory_path)
        try:
            os.makedirs(directory_path, exist_ok=True)
            return f"Directory '{directory_name}' created successfully in 'C:\workdir\projects'."
        except OSError as e:
            return f"Error creating directory '{directory_name}': {str(e)}"

    @tool
    def create_project_structure(project_name: str) -> str:
        """
        Create a standard project structure with directories like "src", "tests", "docs", etc.
        Example:
        - project_name: 'my_project'
        """
        project_path = os.path.join(AgentTools.PROJECT_DIR, project_name)
        project_path = os.path.normpath(project_path)
        try:
            os.makedirs(project_path, exist_ok=True)
            os.makedirs(os.path.join(project_path, "src"), exist_ok=True)
            os.makedirs(os.path.join(project_path, "tests"), exist_ok=True)
            os.makedirs(os.path.join(project_path, "docs"), exist_ok=True)
            return f"Project structure created successfully for '{project_name}' in 'C:\workdir\projects'."
        except OSError as e:
            return f"Error creating project structure for '{project_name}': {str(e)}"

    @tool
    def generate_requirements() -> str:
        """
        Generate a requirements.txt file based on the project's installed packages.
        """
        try:
            result = subprocess.run(["pip", "freeze"], capture_output=True, text=True, check=True)
            requirements = result.stdout
            with open(os.path.join(AgentTools.PROJECT_DIR, "requirements.txt"), "w") as file:
                file.write(requirements)
            return "Requirements file 'requirements.txt' generated successfully in 'C:\workdir\projects'."
        except subprocess.CalledProcessError as e:
            return f"Error generating requirements file: {str(e)}. stderr:\n{e.stderr}"

    @tool
    def run_tests(test_directory: str = "tests") -> str:
        """
        Run the test suite for the project.
        Example:
        - test_directory: 'tests'
        """
        test_path = os.path.join(AgentTools.PROJECT_DIR, test_directory)
        test_path = os.path.normpath(test_path)
        try:
            result = subprocess.run(["python", "-m", "unittest", "discover", test_path], capture_output=True, text=True, check=True)
            return f"Tests executed successfully. Output:\n{result.stdout}"
        except subprocess.CalledProcessError as e:
            return f"Error running tests: {str(e)}. stderr:\n{e.stderr}"

    @tool
    def format_code(file_name: str) -> str:
        """
        Format the code in a file using a code formatter like Black.
        Example:
        - file_name: 'example.py'
        """
        file_path = os.path.join(AgentTools.PROJECT_DIR, file_name)
        file_path = os.path.normpath(file_path)
        try:
            subprocess.run(["black", file_path], check=True)
            return f"Code in file '{file_name}' formatted successfully using Black."
        except FileNotFoundError as e:
            return f"Error: File '{file_name}' not found in 'C:\workdir\projects'. Please make sure the file exists."
        except subprocess.CalledProcessError as e:
            return f"Error formatting code: {str(e)}. stderr:\n{e.stderr}"

    @tool
    def lint_code(file_name: str) -> str:
        """
        Lint the code in a file using a linter like flake8.
        Example:
        - file_name: 'example.py'
        """
        file_path = os.path.join(AgentTools.PROJECT_DIR, file_name)
        file_path = os.path.normpath(file_path)
        try:
            result = subprocess.run(["flake8", file_path], capture_output=True, text=True, check=True)
            return f"Code in file '{file_name}' linted successfully using flake8. Output:\n{result.stdout}"
        except FileNotFoundError as e:
            return f"Error: File '{file_name}' not found in 'C:\workdir\projects'. Please make sure the file exists."
        except subprocess.CalledProcessError as e:
            return f"Linting errors found in file '{file_name}'. Output:\n{e.stdout}"
    
    @tool
    def list_directory_contents(directory_name: str) -> str:
        """
        List the contents of a specific directory within the 'C:\workdir\projects' directory.
        Example:
        - directory_name: 'my_project'
        """
        directory_path = os.path.join(AgentTools.PROJECT_DIR, directory_name)
        directory_path = os.path.normpath(directory_path)
        try:
            contents = os.listdir(directory_path)
            if contents:
                content_list = "\n".join(contents)
                return f"Contents of directory '{directory_name}' in 'C:\workdir\projects':\n{content_list}"
            else:
                return f"Directory '{directory_name}' is empty."
        except FileNotFoundError as e:
            return f"Error: Directory '{directory_name}' not found in 'C:\workdir\projects'. Please make sure the directory exists."
        
    @tool
    def analyze_image_dir(image_path: str) -> str:
        """
        Analyze an image from the given file path within the 'C:\workdir\projects' directory and return a description of its contents.
        Example:
        - image_path: 'my_project/images/image.jpg'
        - image_path: 'my_project/images/image.png'
        """
        full_path = os.path.join(AgentTools.PROJECT_DIR, image_path)
        full_path = os.path.normpath(full_path)
        if os.path.isfile(full_path):
            return f"Analyzing image: {image_path}"
        else:
            return f"Error: Image file '{image_path}' not found in the project directory."
    
    @tool
    def analyze_image_url(image_url: str) -> str:
        """
        Analyze an image from the given URL and return a description of its contents.
        Example:
        - image_url: 'https://example.com/image.jpg'
        """
        return f"Analyzing image: {image_url}"

    def tools(self):
        return [
            self.create_python_file,
            self.create_markdown_file,
            self.run_python_file,
            self.edit_file,
            self.read_file,
            self.append_to_file,
            self.delete_file,
            self.list_files,
            self.search_files,
            self.create_directory,
            self.create_project_structure,
            self.generate_requirements,
            self.run_tests,
            self.format_code,
            self.lint_code,
            self.list_directory_contents,
            self.analyze_image_dir,
            self.analyze_image_url
        ]