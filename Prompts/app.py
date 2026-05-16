from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
import streamlit as st


st.header("Research tool")
user_input = st.text_input("Enter your research query:")
model = ChatOpenAI(model="gpt-5-mini", temperature=0.9)
if st.button("Submit"):
    result = model.invoke(user_input)
    st.text(result.content)