from langchain_community.document_loaders import TextLoader 
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv


loader = TextLoader('amsterdam_text_document.txt')

docs= loader.load()


model = ChatOpenAI(model='gpt-5-mini')

prompt = PromptTemplate.from_template(
    'Summarize the following text \n {text}'

)


parser = StrOutputParser()

chain=prompt | model | parser
result = chain.invoke({'text':docs[0].page_content})
print(result)

