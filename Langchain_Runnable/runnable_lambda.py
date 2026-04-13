from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.runnables import RunnableParallel,RunnablePassthrough,RunnableSequence,RunnableLambda

load_dotenv()

def word_counter(text):
    return len(text.split())


model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser=StrOutputParser()

temeplate1=PromptTemplate(
    template="generate joke on this topic{topic},give only one joke",
    input_variables=['topic']
)
chain1=temeplate1 | model|parser

chain2=RunnableParallel(
    {
        "joke":RunnablePassthrough(),
        "count":RunnableLambda(word_counter)
    }


)
final_chain=chain1 | chain2
result=final_chain.invoke({'topic':'slow strike rate batting of batsmen'})
print(result)
