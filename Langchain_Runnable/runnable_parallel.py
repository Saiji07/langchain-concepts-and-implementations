from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")


tempelate1=PromptTemplate(
    template="Generate tweet for this topic {topic},, strictly give only one tweet dont give options",
    input_variables=['topic']
)

tempelate2=PromptTemplate(
    template="Generate Linkdin post text for this topic {topic}, strictly give only one post dont give options",
    input_variables=['topic']
)
parser=StrOutputParser()
parallel_chain=RunnableParallel(
    {
    "tweet":tempelate1 | model|parser,
    "linkdin":tempelate2 |model| parser
    }
)  
#parallel gives list 

result=parallel_chain.invoke({'topic':'IT Layoffs'})
print(result['tweet'])
print("Here is linkdin post")
print(result['linkdin'])