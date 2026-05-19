from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from pydantic import BaseModel, Field
load_dotenv()


prompt1= PromptTemplate.from_template(
    "generate a detailed  report on {topic}.")

prompt2= PromptTemplate.from_template(
    "generate a 5 pointer summary of the following report:\n {report}")

class Report(BaseModel):
    report: str = Field(description="A detailed report on the given topic")
class Summary(BaseModel):
    summary: str = Field(description="A 5 pointer summary of the given report")

model = ChatOpenAI(model="gpt-5-mini", temperature=0.9)
structured_model1 = model.with_structured_output(Report)
structured_model2 = model.with_structured_output(Summary)

chain= prompt1 | structured_model1 | prompt2 | structured_model2

result=chain.invoke({"topic": "The impact of AI on the job market"})

print(result)

chain.get_graph().print_ascii()
