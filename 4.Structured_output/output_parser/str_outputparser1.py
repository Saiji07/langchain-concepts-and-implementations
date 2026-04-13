from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")


templeate1=PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)
templeate2=PromptTemplate(
    template='write a 5 line summary on the following text {text}',
    input_variables=['text']
)
parser=StrOutputParser()

chain=templeate1 | model | parser | templeate2 | model |parser
result=chain.invoke({'topic':'black hole'})
print(result)