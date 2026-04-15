from langchain.text_splitter import CharacterTextSplitter
text="""LangChain is an open-source framework designed to simplify the development of applications powered by large language models (LLMs). It provides a structured way to connect language models with external data sources, APIs, and workflows.

The framework introduces key concepts such as chains, agents, memory, and tools. Chains allow developers to combine multiple steps into a single pipeline. Agents enable decision-making capabilities, allowing models to choose actions dynamically. Memory helps retain context across interactions, and tools allow integration with external systems like databases and APIs.

LangChain is widely used for building applications such as chatbots, question-answering systems, document analysis tools, and AI assistants. It supports integrations with multiple platforms and enables developers to build scalable and efficient AI systems.

In modern AI development, combining LLMs with external data is crucial. LangChain makes this process easier by providing modular components and flexible architecture, allowing developers to experiment and innovate rapidly."""


splitter=CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)

result=splitter.split_text(text)
print(result)

