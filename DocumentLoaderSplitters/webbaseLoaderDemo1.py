from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter # mostly used in RAG application
import re


#character text spliter
# text_splitter = CharacterTextSplitter(
#     separator="\n\n",
#     chunk_size=200,
#     chunk_overlap=20,
#     length_function=len,
#     is_separator_regex=False
# )

#Recursive character text spliter
text_splitter = RecursiveCharacterTextSplitter(
    #separator="\n\n",
    chunk_size=200,
    chunk_overlap=20,
    length_function=len,
    is_separator_regex=False
)

#load text datafrom a file using Textloaded

loader = WebBaseLoader("https://www.cbd.ae/")
webpage = loader.load()

#to print document without splitter
#print(webpage[0].page_content.strip().replace("\n\n",""))

# chunks = text_splitter.split_text(webpage[0].page_content)
# print(len(chunks))

# for chunk in chunks:
#     print(chunk)
#     print("-------")
    
    
#create document from the chunks as seperate document

documents =text_splitter.create_documents([webpage[0].page_content])

print(len(documents))
for doc in documents:
    print(doc)
    print("-------")
