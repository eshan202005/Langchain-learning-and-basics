from langchain_openai import ChatOpenAI
from langchain_core.tools import tool

llm=ChatOpenAI(model="gpt-5-mini")

@tool
def multiply(a: int, b: int) -> int:
    """Multiplies two numbers."""
    return a * b    

llm_with_tool= llm.bind_tools([multiply])


