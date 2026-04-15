from langchain_community.document_loaders import PyPDFLoader
loader=PyPDFLoader("sample.pdf")
docments=loader.load()
print(len(docments))
print(docments[0])
#pypdf loader makes the document object of each page so it returns list of document objects