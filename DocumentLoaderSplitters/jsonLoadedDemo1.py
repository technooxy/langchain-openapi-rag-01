from langchain_community.document_loaders import JSONLoader

import json
from pathlib import Path
from pprint import pprint


#load text datafrom a file using Textloaded

#each page will be created as single document 
filePath='contact.json'
data= json.loads(Path(filePath).read_text())
pprint(data)

loader = loader = JSONLoader(file_path="contact.json",jq_schema=".employee[].email", text_content=False)
jsondata = loader.load()

print (jsondata)