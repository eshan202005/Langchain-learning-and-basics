from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from pydantic import BaseModel, Field
load_dotenv()


class Review(BaseModel):
    answer: str = Field(description="Write a review for the movie Inception.")
    summary: str = Field(description="A brief summary of the review")

model = ChatOpenAI(model="gpt-5-mini", temperature=0.9)
structured_model = model.with_structured_output(Review)

prompt= PromptTemplate.from_template(
    "Write a review for the movie {name}."
    
)

chain= prompt | structured_model

result=chain.invoke({"name": "Inception"})

print(result)
