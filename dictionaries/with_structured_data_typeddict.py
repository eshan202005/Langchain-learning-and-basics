from langchain_openai import ChatOpenAI
from typing import TypedDict , Annotated , Optional
from dotenv import load_dotenv
load_dotenv()


model=ChatOpenAI(model="gpt-5-mini", temperature=0.9)
 
class review(TypedDict):
    summary: Annotated[str, "A brief summary of the movie."]
    sentiment : Annotated[str, "The overall sentiment of the review."]
    cons: Annotated[Optional[list[str]], "List the negative aspects of the movie."]
structured_model= model.with_structured_output(review)


result=structured_model.invoke("Write a review for the movie Inception.")
print(result)
