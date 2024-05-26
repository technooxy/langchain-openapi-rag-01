from langchain_openai import AzureChatOpenAI
import os

os.environ['OPENAI_API_KEY'] = '65672342343242365ad266bdea567fe4'
os.environ['OPENAI_API_TYPE'] = 'azure'
os.environ['OPENAI_API_VERSION'] = '2024-02-01'
#os.environ['AZURE_OPENAI_API_BASE'] = 'https://rag-dev-001.openai.azure.com/'
os.environ["AZURE_OPENAI_ENDPOINT"] ='https://rag-dev-001.openai.azure.com/'
os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"] ='rag-dev-35trubo16k-001'

#llm=ChatOpenAI()



class Models35:
    
    def turbo3516KLLMModel():
        
        model = AzureChatOpenAI(
        openai_api_version=os.environ["OPENAI_API_VERSION"],
        azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
        )
        return model
    
    def turbo3516KLLMModelAzureOpenAI():
        
        modelAzureOpenAI = AzureChatOpenAI(
        openai_api_version=os.environ["OPENAI_API_VERSION"],
        azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
        )
        return modelAzureOpenAI
    