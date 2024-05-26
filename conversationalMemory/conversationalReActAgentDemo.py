from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain.agents import load_tools, create_react_agent, create_structured_chat_agent, initialize_agent, AgentType
from langchain.tools import Tool
from langchain_core.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from llm35Models import Models35

llm = Models35.turbo3516KLLMModel()


# math_tool= Tool(
#     name = "Calculator",
#     func = llm.invoke,
#     description ='Tool to answer the questions on the Math problems'
# )
#passing the list of tools to LLM ,
#tools=[math_tool]
tools= load_tools(["llm-math"], llm=llm)

memory = ConversationBufferMemory(memory_key="chat_history")

# agent_prompt = PromptTemplate.from_template(
#         """{question}."""
#     )

def custom_parser(output):
    # Parse the LLM output and extract relevant information
    # 
    # This is an example, replace with your actual parsing logic
    # based on the expected LLM response format
    if "answer" in output:
      return output["answer"]
    else:
      return output
  
conversation_agent= initialize_agent(
    #agent = AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    tools=tools,
    llm=llm,
    #prompt=agent_prompt,
    verbose= True,
    max_iteration=5,
    memory=memory,
     # Custom parsing function
    #parse=custom_parser
      #parse=lambda output: re.search(r"final result is (\d+)", output).group(1) if output else None
    )



# res1 = conversation_agent.invoke("Add 7 to 9 and tell me the result")
# print(res1)

#res2 = conversation_agent.invoke("Add 5 to previous result")
#print(res2)

messages = [
    HumanMessage(content="Hello! How can I help you today?"),
]
#ANOTHER APPROACH
# Function to generate response and update conversation history
def get_response(prompt):
  messages.append(HumanMessage(content=prompt))
  #response = llm(messages=messages)
  response = conversation_agent.invoke(input=messages)
  #return response.contenthi
  return response['output']


while True:
  user_input = input("You: ")
  system_response = get_response(user_input)
  print(f"Bard: {system_response}")

  # Optional: Exit condition based on user input
  if user_input.lower() == "exit":
    break

# Clear conversation history when exiting
messages.clear()



