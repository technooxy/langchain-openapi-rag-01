from langchain_openai import AzureOpenAI
import os

os.environ['OPENAI_API_KEY'] = '65672342343242365ad266bdea567fe4'
os.environ['OPENAI_API_TYPE'] = 'azure'
#os.environ['OPENAI_API_VERSION'] = '2024-02-01'
os.environ['OPENAI_API_VERSION'] ='2024-02-15-preview'
#os.environ['AZURE_OPENAI_API_BASE'] = 'https://rag-dev-001.openai.azure.com/'
os.environ["AZURE_OPENAI_ENDPOINT"] ='https://rag-dev-001.openai.azure.com/'
#os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"] ='rag-dev-35trubo16k-001'
os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"] ='rag-dev-35turboinstruc-001'

class Models35:
    
    def turboInstruct35LLMModel():
        model = AzureOpenAI (
            temperature= 0.5, 
            openai_api_version=os.environ["OPENAI_API_VERSION"],
            azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
        )
        
        return model
    