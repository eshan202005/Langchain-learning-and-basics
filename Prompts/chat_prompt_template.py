from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
chat_template = ChatPromptTemplate([
    ('system', "You are a helpful {domain} expert."),
    ('human', "What is the best way to learn {topic}?")
])
prompt=chat_template.invoke({"domain": "programming", "topic": "Python"})
