from pinecone import Pinecone, ServerlessSpec

pc = Pinecone(api_key="a0fdf126-03fb-4240-bb72-b8945d9c39ea", environment="us-east-1")

# pc.create_index(
#             name='rag-vector-pinecone002',
#             dimension=8,
#             metric='euclidean',
#             spec=ServerlessSpec(
#                 cloud='aws',
#                 region='us-east-1'
#             )
#         )


print(pc.list_indexes())