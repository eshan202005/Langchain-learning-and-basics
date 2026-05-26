from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel , RunnableBranch , RunnableLambda



load_dotenv()

parser= StrOutputParser()

model= ChatOpenAI(model="gpt-5-mini")

class feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description="The sentiment of the given text")
prompt1= PromptTemplate.from_template(
    "classify the sentiment of the following text into positive or negative:\n {text}")

model1= model.with_structured_output(feedback)

classifier_chain= prompt1 | model1


prompt2= PromptTemplate.from_template(
    "generate a response based on positive sentiment for the following text:\n {text}")


prompt3= PromptTemplate.from_template(
    "generate a response based on negative sentiment for the following text:\n {text}")



Branching_chain= RunnableBranch(
    (lambda x : x.sentiment == 'positive',prompt2|model1),
    (lambda x : x.sentiment == 'negative',prompt3|model1),
    RunnableLambda(lambda x : "cannot find sentiment")

)
chain = classifier_chain | Branching_chain
result= chain.invoke({"text": "I am very happy with the service provided by your company."})

print(result)