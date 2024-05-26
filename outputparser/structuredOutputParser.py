from typing import List
from langchain_core.output_parsers import ResponseSchema,StrOutputParser


#TODO no more the ResponseSchema found in lanchain 0.2.1

output_parser = StrOutputParser.get_format_instructions()
