
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain.chains import LLMChain
from langchain.agents import Tool
from langchain.tools import tool
from langchain.agents import initialize_agent, AgentType
from llm35Models import Models35


print ("Customer Tool is created in different class and using that cusotm tool we are creating the Agent, this will be used for the accessing enterprice Data")
user_input = "which is the top football team in the world and how, the response should have three fields in JSON - topic of the question,question details and detailed response"

    
def main():  
    tools = [StructuredResponse]
    
    zero_shot_agent = initialize_agent(
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            llm=Models35.turboInstruct35LLMModel(), 
            tools=tools,
            verbose=True,
            max_iteration=20
            )
    res= zero_shot_agent.invoke(input="which is the top football team in the world and how, the response should have three fields in JSON - topic of the question, the question and the detailed response")
    print(res)
    
    
@tool("JSON_response", return_direct=True)
def StructuredResponse(question: str):
    
    """use this tool to send a prompt and get a JSON returned
    with three  fields - Topic , Question_Details and Detailed_Response
    """
    json_prompt = PromptTemplate.from_template(
        """Return a JSON object with an 'answers' key tha answer the following question: {question}.
        the JSON object will have three fields - Topic , Question_Details and Detailed_Response"""
    )
    
    
    json_parser = JsonOutputParser()
    json_chain =json_prompt | Models35.turboInstruct35LLMModel() | json_parser
    
    res = json_chain.invoke({"question":question})
    
    return res


if __name__=="__main__":
    main()