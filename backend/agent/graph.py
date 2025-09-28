from agent.state import State, graph_builder
from agent.model import llm
from langgraph.graph import START, END
from langgraph.checkpoint.memory import MemorySaver  # Add this import

from agent.nodes.analysis_node import analyze_request
from agent.nodes.generate_code import generate_code,should_continue_to_tools
from agent.tools import tool_node

def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}

def route_after_analysis(state: State):
    """Route based on analysis results"""
    
    operation_type = state.get("operation_type", "generate")
    
    if operation_type == "generate":
        return "generate_code"
    elif operation_type == "update":
        return "generate_code"  # For now, both generate and update go to same node
    elif operation_type == "explain":
        return "chatbot"  # Use regular chatbot for explanations
    elif operation_type == "delete":
        return "generate_code"  # Generate test code
    else:
        return "chatbot"  # Default to chatbot


# Add all nodes to the graph
graph_builder.add_node("analysis_node", analyze_request)
graph_builder.add_node("generate_code", generate_code)
graph_builder.add_node("tools", tool_node)
graph_builder.add_node("chatbot", chatbot)



# Define the flow
graph_builder.add_edge(START, "analysis_node")

# After analysis, route to appropriate node
graph_builder.add_conditional_edges(
    "analysis_node",
    route_after_analysis,
    {
        "generate_code": "generate_code",
        "chatbot": "chatbot"
    }
)

# After generate_code, check if tools need to be called
graph_builder.add_conditional_edges(
    "generate_code",
    should_continue_to_tools,
    {
        "tools": "tools",
        "end": END
    }
)

# # After tools are used, go back to generate_code for final response
graph_builder.add_edge("tools", "generate_code")

# Chatbot goes directly to end
graph_builder.add_edge("chatbot", END)

memory = MemorySaver()


# Compile the graph
graph = graph_builder.compile(checkpointer=memory)