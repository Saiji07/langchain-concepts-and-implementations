from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

tempelate1=PromptTemplate(
    template='Generate summary on the following text {text}',
    input_variables=['text']
)
tempelate2=PromptTemplate(
    template="Generate exactly 5 clear quiz questions based on the following text.\nOnly return questions in numbered format.\n\n{text}",
    input_variables=['text']   
)
tempelate3 =PromptTemplate(
    template="""
Combine the following summary and quiz into a structured format.

Summary:
{summary}

Quiz:
{quiz}

Keep all quiz questions EXACTLY as they are.
""",
    input_variables=['summary','quiz']
)

parser=StrOutputParser()
parallel_chain=RunnableParallel(
    {
        'summary':tempelate1| model |parser,
        'quiz' : tempelate2 |model| parser
    }
)

chain2=tempelate3| model|parser
final_chain=parallel_chain | chain2
text="""LangChain is an open-source framework designed to simplify the development of applications powered by large language models (LLMs). It provides a structured way to connect language models with external data sources, APIs, and workflows, enabling developers to build more advanced and context-aware AI systems. Instead of relying solely on raw model prompts, LangChain introduces concepts like chains, agents, memory, and tools, which help manage multi-step reasoning, maintain conversational context, and perform dynamic actions such as retrieving information from databases or calling external services. This makes it particularly useful for building chatbots, question-answering systems, document analysis tools, and AI assistants. By offering modular components and integrations with platforms like OpenAI, Hugging Face, and vector databases, LangChain allows developers to rapidly prototype and deploy scalable AI applications with better control, flexibility, and reliability.
"""


result=final_chain.invoke({'text':text})
print(result)
