from langchain_community.document_loaders import PyPDFLoader


#load text datafrom a file using Textloaded

#each page will be created as single document 
loader = PyPDFLoader("offerLetter.pdf")
pages = loader.load()

cnt =0
for page in pages:
    cnt=cnt+1
    print("Document :::",cnt)
    print (page.page_content.strip())