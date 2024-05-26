from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import AzureChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from llmModels import Models35


import os
# from dotenv import load_dotenv
# load_dotenv()

os.environ['OPENAI_API_KEY'] = '65672342343242365ad266bdea567fe4'
os.environ['OPENAI_API_TYPE'] = 'azure'
os.environ['OPENAI_API_VERSION'] = '2024-02-01'
#os.environ['AZURE_OPENAI_API_BASE'] = 'https://rag-dev-001.openai.azure.com/'
os.environ["AZURE_OPENAI_ENDPOINT"] ='https://rag-dev-001.openai.azure.com/'
os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"] ='rag-dev-35trubo16k-001'

#llm=ChatOpenAI()

llm = AzureChatOpenAI(
    openai_api_version=os.environ["OPENAI_API_VERSION"],
    azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are world class technical documetnation writer."),
    ("user","{input}")
    ])

output_parser =StrOutputParser()

chain = prompt | llm | output_parser

outpout= chain.invoke({"input":"how can langsmith help with testing?"})

print(outpout)

