from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel,Field
from typing import Literal
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda
load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser=StrOutputParser()
class feedback(BaseModel):
    sentiment: Literal["positive","negative"]= Field(description="give this feedback is positive or negative")

parser1=PydanticOutputParser(pydantic_object=feedback)

template1=PromptTemplate(
    template="from this feedback {feedback} identify whether it is positive or negative {format_instruction}",
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser1.get_format_instructions()}
)
template2=PromptTemplate(
    template="give customer appropriate one response to this positive {feedback}.",
    input_variables=['feedback']
)
template3=PromptTemplate(
    template="give customer appropriate response to this negative {feedback}.",
    input_variables=['feedback']
)

chain=template1 |model|parser1
branch_chain=RunnableBranch(
    (lambda x:x.sentiment=='positive',template2|model|parser ),
    (lambda x:x.sentiment=='negative',template3|model|parser),
    RunnableLambda(lambda x:"not an appropriate sentiment")
)
main_chain=chain| branch_chain
result=main_chain.invoke({'feedback':"this phone is horrible"})
print(result)


