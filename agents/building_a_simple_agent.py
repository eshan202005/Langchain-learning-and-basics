from langchain_openai import ChatOpenAI

from langchain_core.tools import tool

import requests

from dotenv import load_dotenv

from langchain_community.tools import DuckDuckGoSearchRun

load_dotenv()
#make a search tool

search_tool = DuckDuckGoSearchRun()

results = search_tool.invoke("What is the capital of France?")


llm=ChatOpenAI(model="gpt-5-mini")

from langchain.agents import create_agent

agent = create_agent(
    model=llm,
    tools=[search_tool],
)


result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "What are 3 ways to reach Goa?"
            }
        ]
    }
)

print(result["messages"][-1].content)
