from ag_ui_langgraph import add_langgraph_fastapi_endpoint
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from copilotkit import LangGraphAGUIAgent 
import uvicorn

from agent.graph import graph

# Create FastAPI app
app = FastAPI(
    title="Code Editing Agent API",
    description="Simple code editing agent",
    version="1.0.0"
)


add_langgraph_fastapi_endpoint(
  app=app,
  agent=LangGraphAGUIAgent(
    name="agent", # the name of your agent defined in langgraph.json
    description="Helps with create updating and deleting codes",
    graph=graph, # the graph object from your langgraph import
  ),
  path="/agent", # the endpoint you'd like to serve your agent on
)



# Add CORS middleware for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],  # React dev servers
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Routes
@app.get("/")
async def root():
    return {"message": "Code Editing Agent API is running!", "status": "healthy"}

# Run the server
if __name__ == "__main__":
    print("Starting Code Editing Agent API...")
    print("Open http://localhost:8000/docs to see the API documentation")
    
    uvicorn.run(
        "main:app",  # This refers to the app object in this file
        host="0.0.0.0",
        port=8000,
        reload=True  # Auto-reload on file changes
    )