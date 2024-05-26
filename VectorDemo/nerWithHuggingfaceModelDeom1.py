from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
import torch

import pandas as pd
import torch
from sentence_transformers import SentenceTransformer





##########Data cleaning############
# df= pd.read_csv("medium_post_titles.csv", nrows=10000) # only 10k are loaded
# #df= pd.read_csv("medium_post_titles.csv") #all are loaded.
# #print(df.head())
# print(df["subtitle_truncated_flag"].value_counts())
# #print(df.isna().sum()) detect missing values (such as NaN, None, or numpy.NaN
# df=df.dropna() #method in Pandas is used to remove rows from a DataFrame that contain missing (NaN) values.
# df=df[~df["subtitle_truncated_flag"]]
# #df.shape()
# df['title_extended']= df['title'] + df['subtitle']
# # df['category'].nunique()
# # df.shape


#create pinecone index 

from pinecone import Pinecone, ServerlessSpec
pc = Pinecone(api_key="a0fdf126-03fb-4240-bb72-b8945d9c39ea", environment="us-east-1")

# pc.create_index(
#             name='csvrag-vector-pinecone002',
#             dimension=384,
#             metric='euclidean',
#             spec=ServerlessSpec(
#                 cloud='aws',
#                 region='us-east-1'
#             )
#         )
print(pc.list_indexes())


#hugging face embedding models

model = SentenceTransformer('all-miniLM-L6-v2', device='cpu')
#print('model')

#title_extended in each rows is mapped as values in vector using map and Lambda
#below code using pandas map capability to do vector embedding at a scale

########### prepare VECTOR VALUES FOR SEMANTIC SEARCH###########
# put the title_extended into as vector and include it as values colum
# df['values']=df['title_extended'].map(lambda x:model.encode(x).tolist())
# #print(df['values'].head(2))

# #to find the range of the index
# df['id']= df.reset_index(drop='index').index

# df['metadata']=df.apply(lambda x:{
#     'title':x['title'],
#     'subtitle':x['subtitle'],
#     'category':x['category']}, axis=1)

# # put all in df_upsert to upload it to vector db.
# df_upsert =df[['id','values','metadata']]
# # Id should be string so converting to string.
# df_upsert['id']=df_upsert['id'].map(lambda x:str(x)) 

# #Insert /Upsert to the pinecone DB
index= pc.Index('csvrag-vector-pinecone002')
# index.upsert_from_dataframe(df_upsert)

res = index.query(vector=(model.encode('famous hospital')).tolist()
                   ,top_k=10
                   ,include_metadata=True)

for result in res['matches']:
    print(f"{round(result['score'],2)}:{result['metadata']['subtitle']}")




model_id='dslim/bert-base-NER'

access_token = "dYrzPElzVKpqMLMeowngodapvXuhPAjRpnpuqcyJyEJfoHbovUArMRaomQClzybLbBBaBMJjkUBWsuYMrDYgUfRCojPUOWusUJlWvmFKpccVDkUDoFrtpVlOjacOlxRR"

tokenizer_ner= AutoTokenizer.from_pretrained(model_id)
ner_model = AutoModelForTokenClassification.from_pretrained(model_id)

device= torch.cuda.current_device() if torch.cuda.is_available() else 'cpu'

nlp = pipeline('ner',model=ner_model, tokenizer=tokenizer_ner, aggregation_strategy='max',device=None, token=access_token)

res= nlp('My Name is Rajesh, I work as freelancer, from coimbatore, Tamilnadu, India')

print(res)
print("==================")


