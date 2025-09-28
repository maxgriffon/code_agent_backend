from agent.state import State
from agent.model import llm
from langchain_core.messages import AIMessage
from agent.tools import tools
from constants.constants import ALLOWED_EXTENSIONS



# Bind tools to LLM
llm_with_tools = llm.bind_tools(tools)

def generate_code(state: State):
    """Generate code node that uses analysis results and creates files with code"""
    # Create a system message with context from analysis
    system_context = f"""You are an expert {state.get("userRequest").language} developer.
    use

    Some additional context:
    the operation that you are preforming {state.get("userRequest").operation_type}
    the type of code that you are building is {state.get("userRequest").code_type}
    the language that you are devloping in {state.get("userRequest").language}

    This is the requst the user is want accomplished:
    {state.get("userRequest").user_message}
    
    You have access to tools to:
    1. create_file - Create a new file with appropriate name and extension
    2. write_code_to_file - Write code content to the file
    3. read_file - read in file content to understand what is currently there should be used when updating files
    4. delete_file - delete file based on a path given should be used to remove files

    Your process should be:
    1. First, create or find an appropriate file using create_file tool
    2. if you are updating code read in file content
    3. Then, generate the actual code and write it using write_code_to_file tool or delet file based on file path
    4. Provide a summary of what you created

    Generate clean, well-documented {state.get("userRequest").language} code that fulfills the user's request."""

    # Get existing messages and add system context
    messages = state.get("messages", [])
    
    # Add system message at the beginning if not already there
    if not any("expert" in str(msg) for msg in messages):
        messages = [AIMessage(content=system_context)] + messages
    
    # Call LLM with tools
    response = llm_with_tools.invoke(messages)
    
    return {"messages": [response]}

def should_continue_to_tools(state: State):
    """Decide whether to continue to tools or end"""
    
    last_message = state["messages"][-1]
    
    # If the last message has tool calls, go to tools
    if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
        return "tools"
    else:
        return "end"