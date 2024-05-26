from langchain.docstore.document import Document
from typing import List

class CustomRetriever:
    def __init__(self, vector_store):
        self.vector_store = vector_store

    def retrieve(self, query: str) -> List[Document]:
        return self.vector_store.similarity_search(query)