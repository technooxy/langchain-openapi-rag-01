from typing import List
from langchain_core.output_parsers import JsonOutputParser
from langchain.prompts import PromptTemplate
from llm35Models import Models35

llm = Models35.turbo3516KLLMModel()

#TODO we need to customize the JSON output parser as per our need.

#note we are not able to use the class travel here to structure what we need 
#json_output = '{"destination": "Paris", "date": "2024-07-15", "duration": 5}'

class Travel:
  """
  A simple class to represent travel data (replace with your actual structure).
  """
  def __init__(self, destination, date, duration):
    self.destination = destination
    self.date = date
    self.duration = duration
 

travel_query="Suggest a 5 place in India for going on a trip this summer to avoid heat."

json_output = '{"destination": "Paris", "date": "2024-07-15", "duration": 5}'

#parser = JsonOutputParser(pydantic_object=Travel)
parser = JsonOutputParser()
#travel_data = parser.parse(json_output)

prompt = PromptTemplate(
    template = "Answer the user query.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions":parser.get_format_instructions},
)

chain =prompt | llm 

res= chain.invoke({"query":travel_query})

print(res)
    