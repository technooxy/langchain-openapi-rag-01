import os
from datasets import load_dataset
from langchain_openai.embeddings import AzureOpenAIEmbeddings
import pandas as pd
import pinecone
from tqdm.auto import tqdm # to show the progress bar

# from dotenv import load_dotenv
# load_dotenv()

# os.environ['OPENAI_API_KEY'] = 'e6801663670645d7a71e3bf1d95cff51'
# os.environ['OPENAI_API_TYPE'] = 'azure'
# os.environ['OPENAI_API_VERSION'] = '2024-02-01'
# #os.environ['AZURE_OPENAI_API_BASE'] = 'https://rag-dev-001.openai.azure.com/'
# os.environ["AZURE_OPENAI_ENDPOINT"] ='https://aoai-eu-rag-dev-001.openai.azure.com/'
# os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"] ='aoai-eu-rag-dev-txtembedding-001'


#llm=ChatOpenAI()

embeddingModel = AzureOpenAIEmbeddings(
    model="text-embedding-3-large",
    openai_api_version=os.environ["OPENAI_API_VERSION"],
    azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
)


 #Data load to get the exact question and answers
 # Data set - https://rajpurkar.github.io/SQuAD-explorer/

# data= load_dataset('squad',split='train')
# df= data.to_pandas()
# # print(df.head())
# # df.iloc['id']
# # df.iloc['title']
# # df.iloc['context']
# # df.iloc['answer']
# print(df.columns)
# print(df.iloc[0]['question'])

# #to remove the duplicated context from th dataset
# df = pd.DataFrame(data)

# #print(sum(df['context'].duplicated())) # will give 688708

# df.drop_duplicates(subset='context', keep='first', inplace=True)
# print(df.shape) #out (18891, 5) we have 18891 documents

embeddingModel = AzureOpenAIEmbeddings(
    model="text-embedding-3-large",
    openai_api_version=os.environ["OPENAI_API_VERSION"],
    azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
)

def get_embedding(text, model):
    text= text.replace("\n", "")
    res=model.embed_query(text)
    return res
    
vec=get_embedding("I am trying a new text and see how it gets embedded", embeddingModel)

# print(len(vec))
#print(vec)


#PINECONE configuration

pinecone.init(
        api_key=os.environ["PINECONE_API_KEY"],
        environment =os.environ["PINECONE_REGION"]
        )

# pinecone.create_index("ai-agnet",dimension=3072, metric='dotproduct')


 
 