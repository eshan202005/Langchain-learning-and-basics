from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel


load_dotenv()

parser= StrOutputParser()

model= ChatOpenAI(model="gpt-5-mini")

class response(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description="The sentiment of the given text")
prompt1= PromptTemplate.from_template(
    "classify the sentiment of the following text into positive or negative:\n {text}")

model1= model.with_structured_output(response)

classifier_chain= prompt1 | model1

result=classifier_chain.invoke({"text": "I am very happy with the service provided!"}).sentiment


print(result)