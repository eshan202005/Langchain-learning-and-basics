from langchain_openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
model = OpenAI(model="gpt-5-mini",temperature=0.1)
result = model.invoke("What is the capital of India?")
print (result.content)