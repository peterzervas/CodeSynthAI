import os
import subprocess
import difflib
import shutil
import tempfile
from datetime import datetime
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

    @tool
    def insert_code_at_line(file_name: str, line_number: int, code: str) -> str:
        """
        Insert code at a specific line number in a file.
        Example:
        - file_name: 'example.py'
        - line_number: 5
        - code: 'print("Inserted line")'
        """
        file_path = os.path.join(AgentTools.PROJECT_DIR, file_name)
        file_path = os.path.normpath(file_path)
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
            
            lines.insert(line_number - 1, code + '\n')
            
            with open(file_path, 'w') as file:
                file.writelines(lines)
            
            return f"Code inserted successfully at line {line_number} in file '{file_name}'."
        except FileNotFoundError:
            return f"Error: File '{file_name}' not found in 'C:\workdir\projects'."
        except IndexError:
            return f"Error: Line number {line_number} is out of range for file '{file_name}'."

    @tool
    def read_file_portion(file_name: str, start_line: int, end_line: int) -> str:
        """
        Read a specific portion of a file.
        Example:
        - file_name: 'example.py'
        - start_line: 10
        - end_line: 20
        """
        file_path = os.path.join(AgentTools.PROJECT_DIR, file_name)
        file_path = os.path.normpath(file_path)
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
            
            if start_line < 1 or end_line > len(lines):
                return f"Error: Line range {start_line}-{end_line} is out of bounds for file '{file_name}'."
            
            portion = lines[start_line-1:end_line]
            return f"Contents of file '{file_name}' from line {start_line} to {end_line}:\n{''.join(portion)}"
        except FileNotFoundError:
            return f"Error: File '{file_name}' not found in 'C:\workdir\projects'."

    @tool
    def compare_files(file1: str, file2: str) -> str:
        """
        Compare the contents of two files and show differences.
        Example:
        - file1: 'old_version.py'
        - file2: 'new_version.py'
        """
        file_path1 = os.path.join(AgentTools.PROJECT_DIR, file1)
        file_path2 = os.path.join(AgentTools.PROJECT_DIR, file2)
        file_path1 = os.path.normpath(file_path1)
        file_path2 = os.path.normpath(file_path2)
        
        try:
            with open(file_path1, 'r') as f1, open(file_path2, 'r') as f2:
                diff = difflib.unified_diff(f1.readlines(), f2.readlines(), fromfile=file1, tofile=file2)
            
            diff_text = ''.join(diff)
            return f"Differences between '{file1}' and '{file2}':\n{diff_text}" if diff_text else "The files are identical."
        except FileNotFoundError as e:
            return f"Error: One or both files not found. {str(e)}"

    @tool
    def create_file_backup(file_name: str) -> str:
        """
        Create a backup of a file before making changes.
        Example:
        - file_name: 'important_script.py'
        """
        file_path = os.path.join(AgentTools.PROJECT_DIR, file_name)
        file_path = os.path.normpath(file_path)
        backup_path = f"{file_path}.bak"
        
        try:
            shutil.copy2(file_path, backup_path)
            return f"Backup of '{file_name}' created successfully as '{file_name}.bak'."
        except FileNotFoundError:
            return f"Error: File '{file_name}' not found in 'C:\workdir\projects'."
        except shutil.SameFileError:
            return f"Error: Backup file '{file_name}.bak' already exists."

    @tool
    def merge_code(file1: str, file2: str, output_file: str) -> str:
        """
        Merge code from two different files or sources.
        Example:
        - file1: 'feature1.py'
        - file2: 'feature2.py'
        - output_file: 'merged_features.py'
        """
        file_path1 = os.path.join(AgentTools.PROJECT_DIR, file1)
        file_path2 = os.path.join(AgentTools.PROJECT_DIR, file2)
        output_path = os.path.join(AgentTools.PROJECT_DIR, output_file)
        file_path1 = os.path.normpath(file_path1)
        file_path2 = os.path.normpath(file_path2)
        output_path = os.path.normpath(output_path)
        
        try:
            with open(file_path1, 'r') as f1, open(file_path2, 'r') as f2, open(output_path, 'w') as out:
                out.write(f1.read() + '\n\n' + f2.read())
            return f"Code from '{file1}' and '{file2}' merged successfully into '{output_file}'."
        except FileNotFoundError as e:
            return f"Error: One or more files not found. {str(e)}"

    @tool
    def find_and_replace(file_name: str, find_str: str, replace_str: str) -> str:
        """
        Find a specific string in a file and replace it with new content.
        Example:
        - file_name: 'config.py'
        - find_str: 'DEBUG = False'
        - replace_str: 'DEBUG = True'
        """
        file_path = os.path.join(AgentTools.PROJECT_DIR, file_name)
        file_path = os.path.normpath(file_path)
        
        try:
            with open(file_path, 'r') as file:
                content = file.read()
            
            new_content = content.replace(find_str, replace_str)
            
            with open(file_path, 'w') as file:
                file.write(new_content)
            
            return f"Successfully replaced '{find_str}' with '{replace_str}' in file '{file_name}'."
        except FileNotFoundError:
            return f"Error: File '{file_name}' not found in 'C:\workdir\projects'."

    @tool
    def check_file_exists(file_name: str) -> str:
        """
        Check if a file exists before attempting to modify it.
        Example:
        - file_name: 'important_data.txt'
        """
        file_path = os.path.join(AgentTools.PROJECT_DIR, file_name)
        file_path = os.path.normpath(file_path)
        
        if os.path.exists(file_path):
            return f"File '{file_name}' exists in 'C:\workdir\projects'."
        else:
            return f"File '{file_name}' does not exist in 'C:\workdir\projects'."

    @tool
    def get_file_info(file_name: str) -> str:
        """
        Get information about a file (size, creation date, last modified date).
        Example:
        - file_name: 'data_analysis.py'
        """
        file_path = os.path.join(AgentTools.PROJECT_DIR, file_name)
        file_path = os.path.normpath(file_path)
        
        try:
            stats = os.stat(file_path)
            size = stats.st_size
            created = datetime.fromtimestamp(stats.st_ctime)
            modified = datetime.fromtimestamp(stats.st_mtime)
            
            return f"""File information for '{file_name}':
            Size: {size} bytes
            Created: {created}
            Last Modified: {modified}"""
        except FileNotFoundError:
            return f"Error: File '{file_name}' not found in 'C:\workdir\projects'."

    @tool
    def create_temp_file(content: str) -> str:
        """
        Create a temporary file for intermediate operations.
        Example:
        - content: 'Temporary data for processing'
        """
        try:
            with tempfile.NamedTemporaryFile(mode='w+', delete=False, dir=AgentTools.PROJECT_DIR, suffix='.tmp') as temp:
                temp.write(content)
                temp_name = os.path.basename(temp.name)
            
            return f"Temporary file '{temp_name}' created successfully in 'C:\workdir\projects'."
        except Exception as e:
            return f"Error creating temporary file: {str(e)}"

    @tool
    def revert_changes(file_name: str) -> str:
        """
        Revert recent changes made to a file.
        Example:
        - file_name: 'modified_script.py'
        """
        file_path = os.path.join(AgentTools.PROJECT_DIR, file_name)
        backup_path = f"{file_path}.bak"
        file_path = os.path.normpath(file_path)
        backup_path = os.path.normpath(backup_path)
        
        try:
            if os.path.exists(backup_path):
                shutil.copy2(backup_path, file_path)
                return f"Changes to '{file_name}' have been reverted using the backup file."
            else:
                return f"Error: Backup file for '{file_name}' not found. Unable to revert changes."
        except Exception as e:
            return f"Error reverting changes: {str(e)}"

    def tools(self):
        return[
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
            self.analyze_image_url,
            self.insert_code_at_line,
            self.read_file_portion,
            self.compare_files,
            self.create_file_backup,
            self.merge_code,
            self.find_and_replace,
            self.check_file_exists,
            self.get_file_info,
            self.create_temp_file,
            self.revert_changes
        ]
