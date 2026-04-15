from langchain_community.document_loaders import WebBaseLoader


url="https://en.wikipedia.org/wiki/Chennai_Super_Kings"
loader=WebBaseLoader(url)
docs=loader.load()
print(docs)
