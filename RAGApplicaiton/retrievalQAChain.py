

# Step 8: Create the Retrieval Chain
class RetrievalQAChain:
    def __init__(self, llm, retriever, prompt_template, docs_content):
        self.llm = llm
        self.retriever = retriever
        self.prompt_template = prompt_template
        self.docs_content=docs_content

    def invoke(self, query: str) -> str:
        # Retrieve relevant documents
        docs = self.retriever.retrieve(query)
        docs_content = "\n".join([doc.page_content for doc in docs])

        # Format the prompt
        prompt = self.prompt_template.format(documents=docs_content, question=query)

        # Get the LLM response
        #response = self.llm(prompt) 
        response = self.llm(prompt) 
        print (response)
        return response