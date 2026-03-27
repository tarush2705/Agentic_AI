from langchain.tools import Tool
from langchain.utilities import WikipediaAPIWrapper
from tavily import TavilyClient
import os

# Wikipedia Tool
wiki = WikipediaAPIWrapper()

def wikipedia_search(query):
    return wiki.run(query)

wiki_tool = Tool(
    name="Wikipedia",
    func=wikipedia_search,
    description="Useful for factual information and general knowledge"
)

# Web Search Tool
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def web_search(query):
    result = tavily.search(query=query, max_results=5)
    return str(result)

web_tool = Tool(
    name="Web Search",
    func=web_search,
    description="Useful for latest information from the web"
)

tools = [wiki_tool, web_tool]