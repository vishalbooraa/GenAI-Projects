from agno.agent import Agent
from agno.tools.youtube import YouTubeTools
from agno.models.groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def build_yt_agent():
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY not found in .env file")

    return Agent(
        tools=[YouTubeTools()],
        description="""
        You are a YouTube video analysis agent.

        Your job:
        - Extract captions from the video
        - Understand the content
        - Provide structured analysis

        Always give:
        - Summary
        - Key insights
        - Important topics
        """,
        model=Groq(
            id="qwen/qwen3-32b",
            api_key=api_key
        ),
    )