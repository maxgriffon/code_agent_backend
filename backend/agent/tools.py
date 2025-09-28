from pathlib import Path
from typing import Optional
from langgraph.prebuilt import ToolNode
from agent.utils import get_file_extension, sanitize_filename
from langchain_core.tools import tool


@tool
def create_file(
    filename: str = None,
    language: str = "python",
    directory: Optional[str] = None
) -> str:
    """ 
    Create a new file in the workspace for code generation.
    
    Args:
        filename: Optional filename. If not provided, generates appropriate name.
        language: Programming language (python, javascript, typescript, etc.)
        code_type: Type of code (function, class, script, application, etc.)
        directory: Optional subdirectory within workspace
        
    Returns:
        String with file path and status message
    """
    
    try:
        base_dir = Path.home() 
        
        filename = sanitize_filename(filename)
        if '.' not in filename:
            extension = get_file_extension(language)
            filename += extension

        if directory:
            full_path = base_dir / sanitize_filename(directory)
        else:
            full_path = Path.home() / "code_agent_workspace"
        
        full_path.mkdir(parents=True, exist_ok=True)
        
        # Search for matching file
        existing_files = list(full_path.rglob(filename))
        
        if existing_files:
            # return the first one
            found_file = existing_files[0]
            relative_path = found_file.relative_to(full_path)
            return f"Found existing file: {relative_path}"
        
        file_path = full_path / filename

         # failsafe
        if file_path.exists():
            relative_path = file_path.relative_to(base_dir)
            return f"File already exists: {relative_path}"
        
        file_path.touch()
        
        relative_path = file_path.relative_to(base_dir)
        return f"File created successfully: {relative_path}"
        
    except Exception as e:
        return f"Error creating file: {str(e)}"

@tool
def delete_file(file_path:str):
    """
    Use this file tool to delete any files

    Args:
        file path: Path to the file relatvie to home directory
    Returns:
        String confirming file was removed. 

    """
    try:
        full_path = Path.home() / file_path

        if not full_path.exists():
            return f"File not found: {file_path}"
        
        if not full_path.is_file():
            return f"Path is not a file: {file_path}"
        
        full_path.unlink()
        
        return f"Successfully deleted the file: {full_path}"
        
    except Exception as e:
        return f"Error writing code: {str(e)}"


@tool
def read_file(file_path:str):
    """
    Read existing code/content from a file.
    
    Args:
        file_path: Path to the file relative to home directory
        
    Returns:
        String with file content or error message
    """

    try:
        full_path = Path.home() / file_path
        
        if not full_path.exists():
            return f"File not found: {file_path}"
        
        if not full_path.is_file():
            return f"Path is not a file: {file_path}"
        
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        return f"File content from {full_path}:\n\n{content}"
    
    except Exception as e:
        return f"Error reading file: {str(e)}"



@tool
def write_code_to_file(
    file_path: str,
    code_content: str
) -> str:
    """
    Write code content to an existing file.
    
    Args:
        file_path: Path to the file relative to home directory
        code_content: The code to write to the file
        
    Returns:
        String with success/error message
    """
    
    try:
        full_path = Path.home()/file_path
        print(full_path)
        
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(code_content)
        
        return f"Code written successfully to: {full_path}"
        
    except Exception as e:
        return f"Error writing code: {str(e)}"

# Create tools list
tools = [create_file, write_code_to_file, read_file, delete_file]

# Create tool node for Graph
tool_node = ToolNode(tools)