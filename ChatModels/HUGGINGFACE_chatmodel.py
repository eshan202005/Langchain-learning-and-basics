from langchain_huggingface import ChatHuggingFace ,  HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()
model = ChatHuggingFace(repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0")