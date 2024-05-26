from langchain_openai import AzureOpenAI
from langchain.utilities import WikipediaAPIWrapper
from langchain.agents import initialize_agent, AgentType
from langchain.prompts import PromptTemplate
from langchain.tools import Tool
from llm35Models import Models35
from customDocstoreExplorer import CustomDocstoreExplorer


llm = Models35.turbo3516KLLMModelAzureOpenAI()

# Initialize the Wikipedia API wrapper
wiki_wrapper = WikipediaAPIWrapper()

# Example query
query = "Tell me a few key things about Mahatma Gandhi"

# Define a function to perform a search using the Wikipedia API
def search_wikipedia(query):
    return wiki_wrapper.run(query)

# Initialize the custom DocstoreExplorer with the Wikipedia search function
docstore_explorer = CustomDocstoreExplorer(search_wikipedia)


# WITHOUT REACT AGENTS 

# Use the DocstoreExplorer to fetch information from Wikipedia
#results = docstore_explorer.search(query)

# Print the results
#print(results)



# WITH REACT AGENTS 

tools=[
    Tool(name="Search", func=docstore_explorer.search, description="useful for when you need to seach wikipedia")
    #Tool(name="Intermediate Answer", func=docstore_explorer.search, description="useful for when you need to seach wikipedia")  # used for self ask search
    ,Tool(name="Lookup", func=docstore_explorer.lookup, description="useful when you need to lookup a term in wikipedia")
]  

# agent_prompt = PromptTemplate.from_template(
#         """Question : {question}.
#         Summary: """
#     )

docstore_agent= initialize_agent(
    agent=AgentType.REACT_DOCSTORE,
    #agent= AgentType.SELF_ASK_WITH_SEARCH,
    tools=tools,
    llm=llm,
    #prompt=agent_prompt,
    verbose= True,
    max_iteration=8,
    handle_parsing_errors=True
     # Custom parsing function
    #parse=custom_parser
      #parse=lambda output: re.search(r"final result is (\d+)", output).group(1) if output else None
    )

res = docstore_agent.invoke(input="Tell me a few key things about Mahatma Gandhi")
#res = docstore_agent.invoke(input="Question:who was the president of USA when first Moon landing took place?") #for self ask search

print(f"Summary: {res}")


