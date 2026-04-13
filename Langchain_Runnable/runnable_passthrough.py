from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.runnables import RunnableParallel,RunnablePassthrough,RunnableSequence

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser=StrOutputParser()

temeplate1=PromptTemplate(
    template="generate joke on this topic{topic}",
    input_variables=['topic']
)
temeplate2=PromptTemplate(
    template="give explanation of this joke {joke} and give response in format such that text contains joke and below that explnation of that jok",
    input_variables=['joke']
)


final_chain=RunnableSequence(temeplate1,model,parser,RunnableParallel({
    "joke":RunnablePassthrough(),
    "explanation":RunnableSequence(temeplate2,model,parser)
}))

result=final_chain.invoke({'topic':'cricket'})
print(result)
