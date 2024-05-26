from langchain_core.prompts import ChatPromptTemplate
#from langchain_openai import ChatOpenAI
from langchain_openai import AzureOpenAI
#from langchain.chains import LLMChain
from langchain_core.messages import HumanMessage
from langchain_openai import AzureChatOpenAI

from langchain.prompts import PromptTemplate
import os
# from dotenv import load_dotenv
# load_dotenv()

os.environ['AZURE_OPENAI_API_KEY'] = '65672342343242365ad266bdea567fe4'
os.environ['AZURE_OPENAI_API_TYPE'] = 'azure'
os.environ['OPENAI_API_VERSION'] = '2024-02-01'
#os.environ['AZURE_OPENAI_API_BASE'] = 'https://rag-dev-001.openai.azure.com/'
os.environ["AZURE_OPENAI_ENDPOINT"] ='https://rag-dev-001.openai.azure.com/'
os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"] = "rag-dev-35trubo16k-001"


# llm = AzureOpenAI(
#     deployment_name="rag-dev-35trubo16k-001",
#     model_name="gpt-35-turbo-16k"
# )

model = AzureChatOpenAI(
    openai_api_version=os.environ["OPENAI_API_VERSION"],
    azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
)


print ("First Azure based chat gp with GPT 3.5 model")

print("invoke demo1")
message = HumanMessage(content="Translate this sentence from English to French. I love programming." )
res = model.invoke([message])
print(res.content)



