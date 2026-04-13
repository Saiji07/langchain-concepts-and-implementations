from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace
from dotenv import load_dotenv
import os
os.environ['HF_HOME']='D:/huggingface_cache'

load_dotenv()
llm=HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation'
    
)
mdl=ChatHuggingFace(llm=llm)
result=mdl.invoke("who is ms dhoni")
print(result.content)
