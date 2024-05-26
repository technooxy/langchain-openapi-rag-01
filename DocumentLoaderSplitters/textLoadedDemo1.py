from langchain_community.document_loaders import TextLoader


#load text datafrom a file using Textloaded

loader = TextLoader("sample.txt")
document = loader.load()

print(document[0].metadata)
print(document[0].page_content)