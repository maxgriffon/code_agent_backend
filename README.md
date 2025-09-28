# Code Editing Agent

A AI-powered code editing agent built with LangGraph and CopilotKit that can generate, update, analyze, and manage code files through natural language conversations.

## Features

- 🤖 **Intelligent Code Generation**: Create code in multiple programming languages
- ✏️ **Code Updates**: Modify existing code with natural language instructions
- 🔍 **Code Analysis**: Explain and analyze code functionality
- 📁 **File Management**: Create, read, write, and delete files
- 🌐 **Multi-language Support**: Python, JavaScript, TypeScript, Java, C++, and more
- 💬 **Conversational Interface**: Powered by CopilotKit for seamless chat experience
- 🔧 **Tool Integration**: Built-in file operations and syntax validation

## Architecture

```
Frontend (Next.js) ↔ CopilotKit ↔ FastAPI Backend ↔ LangGraph Agent ↔ Groq LLM
```

- **Frontend**: Next.js with CopilotKit React components
- **Backend**: FastAPI server with LangGraph agent integration
- **AI Model**: Llama 3.3 70B model for code generation
- **Agent Framework**: LangGraph for structured conversation flow
- **File Operations**: Custom tools for workspace management

## Prerequisites

- Python 3.12
- Node.js 18+
- Groq API key ([Get one here](https://console.groq.com))

## Python
- Recommend Python version 3.12 some computers are running python 3.9 or python 3.13 these will not work as there are packages that don't exist in these versions.

```bash
brew install python3.12
```
This should install it then you can create your venv with command below. If this does not work then you can try this alternative. 

```bash
brew install pyenv
pyenv install 3.12.0
pyenv local 3.12.0
```

To confirm your python version you can run:
```bash
python3 --version
```

## Installation

### Backend Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd code_agent_backend 
   ```

2. **Create virtual environment**
   ```bash
   python3.12 -m venv venv
   source venv/bin/activate  # On Windows: venv_312\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip3 install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the backend directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```
   If you don't have a groq key please go to `https://console.groq.com` and create/sign in an account. Once logged in, look for "API Keys" in the upper right navigation bar. Finally click on Create api key and then copy it into your .env

5. **Start the backend server**
   ```bash
   python3 main.py
   ```
   
   The API will be available at `http://localhost:8000`

    OR 
    If you just wnat to try the agent out in the terminal you can run. 
    This will run everything in the terminal and you can interact with agent in the terminal. Useful if the frontend is not working. 

    ```bash
   python3 test.py
   ```

### Frontend Setup

1. **Navigate to frontend directory**
    Open a new terminal at the root of the project. Both should be running at the same time. 

   ```bash
   cd frontend 
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start the development server**
   ```bash
   npm run dev
   ```
   
   The frontend will be available at `http://localhost:3000`

## Configuration

### Backend Configuration

The agent can be configured through environment variables:

```env
# Required
GROQ_API_KEY=your_groq_api_key_here

# Optional
MODEL_NAME=llama-3.3-70b-versatile
TEMPERATURE=0.1
PORT=8000
```

### Supported Languages

The agent supports the following programming languages:

- Python (`.py`)
- JavaScript (`.js`)
- TypeScript (`.ts`, `.tsx`)
- Java (`.java`)
- C++ (`.cpp`)
- C (`.c`)
- C# (`.cs`)
- Go (`.go`)
- Rust (`.rs`)
- PHP (`.php`)
- Swift (`.swift`)
- Kotlin (`.kt`)

## Usage

### Basic Commands

The agent understands natural language instructions for various code operations:

#### Sample Prompts
```
"Create a Python function that calculates fibonacci numbers"
"Write a JavaScript function to reverse a string"
"Write a Python Pong game in my Downloads folder"
"Update my hello world code to saying "hello how are you"
"Delete XXXX file code file from my repo."
```

#### Agent Interaction
```bash
POST http://localhost:8000/agent
Content-Type: application/json

{
  "messages": [
    {
      "role": "user", 
      "content": "Create a hello world function in Python"
    }
  ]
}
```

## Project Structure

```
code_agent_backend/
├── backend/
│   ├── agent/
│   │   ├── nodes/
│   │   │   ├── analysis_node.py      # Request analysis
│   │   │   └── generate_code.py      # Code generation
│   │   ├── constants/
│   │   │   └── constants.py          # Constants
│   │   ├── graph.py                  # Graph workflow
│   │   ├── model.py                  # LLM Model configuration
│   │   ├── prompts.py                # System prompts
│   │   ├── state.py                  # State management
│   │   ├── tools.py                  # File operation tools
│   │   └── utils.py                  # Utility functions
│   ├── main.py                       # FastAPI server
│   ├── test.py                       # Testing script
└── frontend/
|    ├── api/copilot/route.ts      # CopilotKit API route
|    ├── layout.tsx                # App layout with CopilotKit
|    └── page.tsx                  # Main chat interface
|    └── package.json                  # Node.js dependencies
|__requirements.txt
```

## Development

### Testing the Agent

1. **Backend testing**
   ```bash
   python test.py
   ```

## Troubleshooting

### Common Issues

1. **"No checkpointer set" error**
   - Ensure the graph is compiled with a checkpointer
   - Provide proper config with thread_id when testing

2. **Groq API key error**
   - Set the `GROQ_API_KEY` environment variable
   - Check that the API key is valid

3. **Socket connection errors**
   - Ensure both backend (8000) and frontend (3000) are running
   - Check CORS configuration in main.py

4. **File operation errors**
   - Check file permissions in the workspace directory
   - Ensure the target directory exists

5. **Rate Limit**
    - If you get a generic error on the frontend it is possible you are getting rate limited. This should show up in the backend terminal. 

6. **Frontend Crash**
    - if frontend crashes for what ever reason you can run this instead of the main.py:
    ```bash
    python3 test.py
    ```
## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Add tests for new functionality
5. Commit your changes: `git commit -am 'Add feature'`
6. Push to the branch: `git push origin feature-name`
7. Submit a pull request

## Acknowledgments

- [LangGraph](https://github.com/langchain-ai/langgraph) for the agent framework
- [CopilotKit](https://github.com/CopilotKit/CopilotKit) for the chat interface
- [Groq](https://groq.com/) for the fast LLM inference
- [FastAPI](https://fastapi.tiangolo.com/) for the backend framework

## Support

If you encounter any issues or have questions:

1. Check the [troubleshooting section](#troubleshooting)
2. Search existing [GitHub issues](link-to-issues)
3. Create a new issue with detailed information about your problem

---

**Happy Coding! 🚀**