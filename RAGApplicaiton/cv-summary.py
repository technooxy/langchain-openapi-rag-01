from langchain.document_loaders import Docx2txtLoader
from langchain_openai import AzureChatOpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.prompts import PromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
import textwrap
import streamlit as st
import os
from dotenv import load_dotenv


# from dotenv import load_dotenv
load_dotenv()

# Use gpt-35-turbo-16k

# from dotenv import load_dotenv
# load_dotenv()

os.environ['OPENAI_API_KEY'] = '65672342343242365ad266bdea567fe4'
os.environ['OPENAI_API_TYPE'] = 'azure'
os.environ['OPENAI_API_VERSION'] = '2024-02-01'
#os.environ['AZURE_OPENAI_API_BASE'] = 'https://rag-dev-001.openai.azure.com/'
os.environ["AZURE_OPENAI_ENDPOINT"] ='https://rag-dev-001.openai.azure.com/'
os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"] ='rag-dev-35trubo16k-001'

#llm=ChatOpenAI()
llm = AzureChatOpenAI(
    openai_api_version=os.environ["OPENAI_API_VERSION"],
    azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
)


def process_docx(docx_file):
    # Add your docx processing code here
    text=""
    #Docx2txtLoader loads the Document 
    loader=Docx2txtLoader(docx_file)

    #Load Documents and split into chunks
    text = loader.load_and_split()

    return text

def process_pdf(pdf_file):
    text=""
    #PYPDFLoader loads a list of PDF Document objects
    loader=PyPDFLoader("D:/Rajesh/technooxy_Docs/Client_Projects/inhouse/AI/LangChain-OpenAI-RAG-01/openAIRAGApplication/git/langchain-openapi-rag-01/PrakashA.pdf")
    pages = loader.load()
        
    for page in pages:
        text+=page.page_content
    text= text.replace('\t', ' ')

    #splits a long document into smaller chunks that can fit into the LLM's 
    #model's context window
    text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=50
        )
    #create_documents() create documents froma list of texts
    texts = text_splitter.create_documents([text])

    print(len(text))

    return texts

def main():

    st.title("CV Summary Generator")

    uploaded_file = st.file_uploader("Select CV", type=["docx", "pdf"])

    text = ""
    if uploaded_file is not None:
        file_extension = uploaded_file.name.split('.')[-1]

        st.write("File Details:")
        st.write(f"File Name: {uploaded_file.name}")
        st.write(f"File Type: {file_extension}")

        if file_extension == "docx":
            text = process_docx(uploaded_file.name)
        elif file_extension == "pdf":
            text = process_pdf(uploaded_file.name)
        else:
            st.error("Unsupported file format. Please upload a .docx or .pdf file.")
            return

        prompt_template = """You have been given a Resume to analyse. 
        Write a verbose detail of the following: 
        {text}
        Details:"""
        prompt = PromptTemplate.from_template(prompt_template)

        refine_template = (
            "Your job is to produce a final outcome\n"
            "We have provided an existing detail: {existing_answer}\n"
            "We want a refined version of the existing detail based on initial details below\n"
            "------------\n"
            "{text}\n"
            "------------\n"
            "Given the new context, refine the original summary in the following manner:"
            "Name: \n"
            "Email: \n"
            "Key Skills: \n"
            "Last Company: \n"
            "Experience Summary: \n"
        )
        refine_prompt = PromptTemplate.from_template(refine_template)
        chain = load_summarize_chain(
            llm=llm,
            chain_type="refine",
            question_prompt=prompt,
            refine_prompt=refine_prompt,
            return_intermediate_steps=True,
            input_key="input_documents",
            output_key="output_text",
        )
        result = chain({"input_documents": text}, return_only_outputs=True)

        st.write("Resume Summary:")
        st.text_area("Text", result['output_text'], height=400)

if __name__ == "__main__":
    main()

