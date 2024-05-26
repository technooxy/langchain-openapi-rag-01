from langchain_community.document_loaders import WikipediaLoader

loader = WikipediaLoader("Machine_learning")
document =loader.load()

print(document[0].page_content)