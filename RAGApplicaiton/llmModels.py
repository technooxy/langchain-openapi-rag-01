from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings
import os

#llm=ChatOpenAI()

class Models35:
        
    def turbo3516KLLMModel():
        
        model = AzureChatOpenAI(
        openai_api_version=os.environ["OPENAI_API_VERSION"],
        azure_deployment='rag-dev-35turboinstruc-001',
        )
        return model
    
    def turbo3516KLLMModelAzureOpenAI():
        
        modelAzureOpenAI = AzureChatOpenAI(
        openai_api_version=os.environ["OPENAI_API_VERSION"],
        azure_deployment='rag-dev-35trubo16k-001',
        )
        return modelAzureOpenAI
    
    
    def turbo3516KLLMModelAzureOpenAIembedding ():
        embedding_model = AzureOpenAIEmbeddings(
        model="text-embedding-3-large",
        azure_deployment='rag-dev-txtembedding-001',
        )
        return embedding_model
    
    
