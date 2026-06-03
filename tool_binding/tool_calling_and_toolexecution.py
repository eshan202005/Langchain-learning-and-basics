from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

llm=ChatOpenAI(model="gpt-5-mini")

messages = []

@tool
def multiply(a: int, b: int) -> int:
    """Multiplies two numbers."""
    return a * b    

llm_with_tool= llm.bind_tools([multiply])


query= HumanMessage(content="What is the product of 3 and 4?")

messages.append(query)



#tool calling which returns a structured out with name of the tool and the arguments passed to it.

response= llm_with_tool.invoke(messages)

messages.append(AIMessage(content=response.content))

print(response.tool_calls)
#tool execution 

result = multiply.invoke(response.tool_calls[0]["args"])


messages.append(result)


llm_with_tool.invoke(messages)







 