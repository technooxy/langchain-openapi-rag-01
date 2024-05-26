from langchain_core.prompts import ChatPromptTemplate
#from langchain_openai import ChatOpenAI
from langchain_openai import AzureOpenAI
from langchain.chains import LLMChain
from langchain.agents import Tool
from langchain.agents import initialize_agent, AgentType


import os
# from dotenv import load_dotenv
# load_dotenv()

os.environ['OPENAI_API_KEY'] = '65672342343242365ad266bdea567fe4'
os.environ['OPENAI_API_TYPE'] = 'azure'
#os.environ['OPENAI_API_VERSION'] = '2024-02-01'
os.environ['OPENAI_API_VERSION'] ='2024-02-15-preview'
#os.environ['AZURE_OPENAI_API_BASE'] = 'https://rag-dev-001.openai.azure.com/'
os.environ["AZURE_OPENAI_ENDPOINT"] ='https://rag-dev-001.openai.azure.com/'
#os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"] ='rag-dev-35trubo16k-001'
os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"] ='rag-dev-35turboinstruc-001'



print ("First Agent and Tool creation with GPT 3.5 model")
def main():

    print(createmathagent.__doc__)
    createmathagent()
    

def createmathagent():

    llm =AzureOpenAI(
        temperature= 0, # most deterministic and not required any creativity
        #model_kwargs = {
            #"temperature": 0,
            #"max_length": 150,
            #"top_k": 50,
            #"no_repeat_ngram_size": 2,
            #"early_stopping": True
            #},
        openai_api_version=os.environ["OPENAI_API_VERSION"],
        azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
    )


    llm_math=llm

    #initialize math tool

    math_tool= Tool(
        name = "Calculator",
        func = llm_math.invoke,
        description ='Tool to answer the questions on the Math problems'
    )

    #passing the list of tools to LLM ,
    tools=[math_tool]
    
    print(tools[0].name, ":::::",tools[0].description)

    zero_shot_agent = initialize_agent(
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        llm=llm, 
        tools=tools,
        verbose=True,
        max_iteration=20
        )
    
   
    #user_input ="What is the root over 25 using python"
    user_input ="""
                You are building a house.There are two bed rooms of 5 meters by 5 meters each and drawing cum open kitchen is 7 meters 
                by 6 meters and balcony is 3 meters by 2 meters. what is the total area of your house?
                """
    res= zero_shot_agent(user_input)
    print(res)


if __name__== "__main__":
    main()