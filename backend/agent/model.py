from langchain_groq import ChatGroq
import os


# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # dotenv not installed, skip loading
    pass


# Set your API key (get from console.groq.com)
groq_api_key = os.environ.get('GROQ_API_KEY')

llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    temperature=0.1,
    groq_api_key=groq_api_key
)


