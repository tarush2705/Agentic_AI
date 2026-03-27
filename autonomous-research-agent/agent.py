from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from tools import tools
import os

def create_agent():
    llm = ChatOpenAI(
        temperature=0,
        model="gpt-4",
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )

    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    return agent