import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains.combine_documents.refine import RefineDocumentsChain
from langchain.chains.llm import LLMChain
from langchain.docstore.document import Document
from langchain.chains.llm import LLMChain

# Ensure you have set up the Azure OpenAI API environment variables

# Step 1: Load the PDF
pdf_loader = PyPDFLoader("PrakashA.pdf")
documents = pdf_loader.load()

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
# Step 2: Initialize the Azure OpenAI Embedding Model
embedding_model = AzureOpenAIEmbeddings(
        model="text-embedding-3-large",
        azure_deployment='rag-dev-txtembedding-001',
        )

# Step 3: Create a Document Store with FAISS
faiss_index = FAISS.from_documents(documents, embedding_model)

# Step 4: Define a Prompt Template for Summarization
prompt_template = """
        Extract and summarize the key skill sets and experience summary from the following CV:\n\n
        {documents}\n\n
        Key Skills:\n
        Experience Summary:
        """
prompt= PromptTemplate(template=prompt_template, input_variables=["documents"])



# prompt = PromptTemplate(input_variables=["documents"],
#                 template="Summarize this content: {documents}"
#             )
document_prompt = PromptTemplate(
                input_variables=["page_content"],
                 template="{page_content}"
            )
document_variable_name = "documents"

# prompt_refine = PromptTemplate(input_variables=["documents"],
#                  template="Here's your first summary: {prev_response}. "
#                  "Now add to it based on the following context: {documents}"
# )

prompt_refine = PromptTemplate(input_variables=["documents"],
                  template=prompt_template
 )

initial_response_name = "prev_response"
initial_llm_chain =LLMChain(llm=llm, prompt=prompt)
refine_llm_chain = LLMChain(llm=llm, prompt=prompt_refine)

summarization_chain = RefineDocumentsChain(
    initial_llm_chain=initial_llm_chain,
    refine_llm_chain=refine_llm_chain,
    document_prompt=document_prompt,
    document_variable_name=document_variable_name,
    initial_response_name=initial_response_name,
)

# Step 6: Define a function to perform the summarization
def summarize_cv(pdf_path):
    # Load the PDF
    pdf_loader = PyPDFLoader(pdf_path)
    documents = pdf_loader.load()
    
    # Format the documents into a single string
    #docs_content = "\n".join([doc.page_content for doc in documents])
    
    # Create the prompt
   # promptfrt = prompt.format(documents=docs_content)
    
    # Get the summary
    #summary = summarization_chain.invoke({"input_documents": docs_content})
    summary = summarization_chain.invoke(documents)
    return summary

# Path to your CV PDF
pdf_path = "PrakashA.pdf"

# Get the summary
summary = summarize_cv(pdf_path)

# Print the summary
print("Summary:")
print(summary)
