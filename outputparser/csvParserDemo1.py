from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from llm35Models import Models35


llm = Models35.turbo3516KLLMModel()

output_parser=CommaSeparatedListOutputParser()

format_instructions =output_parser.get_format_instructions()
prompt= PromptTemplate(
    template="List five places {places}.\n {format_instructions}",
    input_variables=["places"],
    partial_variables={"format_instructions": format_instructions},
)

chain = prompt | llm | output_parser

res= chain.invoke({'places':"for summer tourism in India"})

print(res)