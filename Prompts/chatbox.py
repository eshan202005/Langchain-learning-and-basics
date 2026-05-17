from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
load_dotenv()


model=ChatOpenAI(model="gpt-5-mini", temperature=0.9)

chat_history = [SystemMessage(content="You are a helpful assistant.")

]


while True:
    user_input=input('You:')
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() in ['exit', 'quit']:
        print("Exiting chat...")
        break

    result=model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print('AI:', result.content)