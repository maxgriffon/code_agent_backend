
from pathlib import Path
from typing import Annotated, Optional

from copilotkit import CopilotKitState
from pydantic import BaseModel, Field
from typing_extensions import TypedDict
from langgraph.graph import StateGraph

from langgraph.graph.message import add_messages



class UserRequest(BaseModel):
    operation_type: str = Field(description="Type of operation that the user would like to do from a code prespective")
    language: str = Field( description="the lanuage the code is/would be developed in")
    code_type: str = Field(description="1 or 2 word summary used to generalize the request")
    filename: str = Field(description = "file name if mentioned or a generated file name")
    directory: Optional[str] = Field(description= "a path to the direct that wants to be used if any")
    user_message: str = Field(description = "the user message that was sent with any additional analysis")

class State(TypedDict):
    messages: Annotated[list, add_messages]
    userRequest: UserRequest


graph_builder = StateGraph(State)
