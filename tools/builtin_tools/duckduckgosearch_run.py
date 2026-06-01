from langchain_community.tools import DuckDuckGoSearchRun

tool = DuckDuckGoSearchRun()

query = "todays new news in india?"

result = tool.invoke(query)

print(result)
