# This program is intended to demo the use of the following
# - webbasedloaded to read a webpage
# - RecusrsiveCharacterTextSplitter to chunk the webcontent into documents
# - convert the documents into embeddings and store into an FAAISS DB
# - create a Stuff document chain, create a retrieval chain from the FAISS DB [Facebook AI Similarity Search]
# - create retrivel chain using the FAISS retriver and document chain

from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter # mostly used in RAG application
from langchain_community.vectorstores import FAISS
from langchain_openai import AzureOpenAIEmbeddings, AzureOpenAI
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.documents import Document
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from llmModels import Models35
from retrievalQAChain import RetrievalQAChain
from customRetriever import CustomRetriever 
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings

import os
# from dotenv import load_dotenv
# load_dotenv()

# os.environ['OPENAI_API_KEY'] = '65672342343242365ad266bdea567fe4'
# os.environ['OPENAI_API_TYPE'] = 'azure'
# os.environ['OPENAI_API_VERSION'] = '2024-02-01'
# #os.environ['AZURE_OPENAI_API_BASE'] = 'https://rag-dev-001.openai.azure.com/'
# os.environ["AZURE_OPENAI_ENDPOINT"] ='https://rag-dev-001.openai.azure.com/'
# os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"] ='rag-dev-35trubo16k-001'

#llm=ChatOpenAI()

llm = AzureChatOpenAI(
    openai_api_version=os.environ["OPENAI_API_VERSION"],
    azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
)

loader = WebBaseLoader("https://www.cbd.ae/")
webpages = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    #separator="\n\n",
     chunk_size=200,
     chunk_overlap=20,
     length_function=len,
     is_separator_regex=False
)

#load text web page to splitter
documents =text_splitter.split_documents(webpages)

# documents = [
#     Document(page_content="The Eiffel Tower is in Paris."),
#     Document(page_content="The Great Wall of China is in China."),
#     Document(page_content="The Colosseum is in Rome."),
# ]

print("Total Document Length ::",len(documents))
# for doc in documents:
#     print(doc)
#     print("-------")

embeddings = AzureOpenAIEmbeddings(
        model="text-embedding-3-large",
        azure_deployment='rag-dev-txtembedding-001',
        )
#FAISS (Facebook AI Similarity Search) is a library that allows developers to store for embeddings of 
#documents that are similar to each other.
faiss_index = FAISS.from_documents(documents,embeddings)

# prompt = ChatPromptTemplate.from_template("""
#                                           Answer the following question based only on the provided context:
#                                           <context>
#                                           {context}
#                                           </context>
#                                           Question: {input}"""
#                                           )


prompt = PromptTemplate(
    template="Given the following documents:\n{documents}\nAnswer the question: {question}\n",
    input_variables=["documents", "question"]
)

#takes all information and send to the llm model
#Since we use custom retrieverqa class we are notusing below chain and also there is missing create_retrieval_chain
# document_chain=create_stuff_documents_chain(llm, prompt)

#retrive information from the vector DB

#retriever= vector.as_retriever()
retriever = CustomRetriever(vector_store=faiss_index)
#Retriever chain - user retriever object to pull all data from vector DB and pass to document chain 
#and document chain will load the documents to llm model. 
#retriever_chain=create_retrieval_chain(retriever,document_chain)
#res=retriever_chain.invoke({"context":"Find the savings account details"})

# Directly search from vector DB
similar_documents = faiss_index.similarity_search(query="Savings Account", top_k=5)

print(len(similar_documents))
# Print similar documents
for doc in similar_documents:
    print(f"Document ID: {doc}")
    print("========================")

# query = "Find the savings account details"
# retriever_chain = RetrievalQAChain(llm=llm, prompt_template=prompt, retriever=retriever,docs_content=documents)

# result = retriever_chain.invoke("Revolutionizing customer service")

# #result = retriever_chain("Where is the Eiffel Tower?")

# print(result)

