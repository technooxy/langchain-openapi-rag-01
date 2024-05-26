from langchain.agents.react.base import DocstoreExplorer

# Initialize the DocstoreExplorer with a custom search function
class CustomDocstoreExplorer(DocstoreExplorer):
    def __init__(self, search_func):
        self.search_func = search_func

    def search(self, query):
        return self.search_func(query)