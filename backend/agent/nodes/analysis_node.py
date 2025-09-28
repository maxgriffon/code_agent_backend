
from agent.model import llm
from agent.prompts import ANALYSIS_PROMPT
from langchain_core.prompts import ChatPromptTemplate
from agent.state import State, UserRequest

tagging_prompt = ChatPromptTemplate.from_template(ANALYSIS_PROMPT)

def analyze_request(state:State):
    """analyze user request in order to produce a better code."""

    # Get user message
    messages = state.get("messages", [])
    user_message = messages[-1].content
    structured_llm = llm.with_structured_output(UserRequest)
    prompt = tagging_prompt.invoke({"user_request": user_message})
    response = structured_llm.invoke(prompt)
    state["userRequest"] = response

    print({
        **state,
        "user_request":response,
        "analysis_complete": True
    })
    return {
        **state,
        "user_request":response,
        "analysis_complete": True
    }




