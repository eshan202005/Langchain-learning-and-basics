from langchain_community.tools import DuckDuckGoSearchRun, ShellTool

tool = ShellTool()

query = "whoami"

result = tool.invoke(query)

print(result)
