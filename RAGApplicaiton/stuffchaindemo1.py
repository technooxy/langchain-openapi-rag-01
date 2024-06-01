from langchain_community.document_loaders import PyPDFLoader
from langchain.chains.summarize.chain import load_summarize_chain
from langchain_core.prompts import PromptTemplate
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
<<<<<<< HEAD
print(llm)
=======
>>>>>>> e845a3a21b0a1a8823f21e8e23c818e682a16c73

loader =PyPDFLoader("PrakashA.pdf")
docs= loader.load()

cnt=0

# for doc in docs:
#     cnt= cnt+1
#     print("----Documents ###",cnt)
#     print(doc.page_content.strip())
    
prompt_template="""
you are given a Resume as the below text
--------
{text}
--------
Question:Please respond with the key skills and experience summary of the person.
Key Skills:
Experience Summary:
"""

prompt= PromptTemplate(template=prompt_template, input_variables=["text"])

stuff_chain= load_summarize_chain(llm=llm, chain_type="stuff")

output_summary=stuff_chain.invoke(docs)

print(output_summary['output_text'])

 
    