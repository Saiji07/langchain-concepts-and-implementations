from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.runnables import RunnableParallel,RunnablePassthrough,RunnableSequence,RunnableLambda,RunnableBranch

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser=StrOutputParser()
temeplate1=PromptTemplate(
    template="generate report on this topic{topic}",
    input_variables=['topic']
)

temeplate2=PromptTemplate(
    template="generate summary of this text{text}",
    input_variables=['text']
)
chain1=temeplate1|model|parser
conditional_chain=RunnableBranch(
    (lambda x:len(x.split())>500,temeplate2|model|parser),
    RunnablePassthrough()
)
final_chain=chain1 | conditional_chain
result=final_chain.invoke({'topic':'Nirma University'})
print(result)

