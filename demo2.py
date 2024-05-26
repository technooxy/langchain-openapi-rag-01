from langchain_core.prompts import ChatPromptTemplate
#from langchain_openai import ChatOpenAI
from langchain_openai import AzureChatOpenAI
from langchain.chains import LLMChain

from langchain.prompts import PromptTemplate
import os
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


print ("First Azure based chat gp with GPT 3.5 model")
def main():
    """
    print(demo1.__doc__)
    demo1()
    """
    print(demo2.__doc__)
    demo2()
    


def demo1():
    """This Function demo the use of the off the shelf LLM Chain to combune the prompt and an LLM call to
    get the desire response
    """
    #create a prompt template with a embedded variable

    template ="""question :{question}
    answer:"""
    prompt = PromptTemplate(template=template, input_variables=['question'])

    #user Question
    question="which is the most popular game in India ?"

    #create the Language Model Object
    #llm = ChatOpenAI()


    #use the LLMChain to stich the prompt and llm - LLMChain is used to run queries against LLMs
    #The LLMChain consist of a PromptTemplate, a language model, and an Optional output Parser.


    llm_chain= LLMChain(prompt=prompt, llm=llm) # will be deprecated in .0.1.17 and will be removed in 0.3.0
    #llm_chain= prompt | llm # LLM Expression language


    #invoke (run) the LLM Chain - the Chain returns dictionary of  named outputs
    res = llm_chain.invoke(question)["text"]
    print(res)



def demo2():
    """This Function demo the simeple LCEL [Langchain expression language] to create custom chain with the 
    prompt and model
    """

    prompt = ChatPromptTemplate.from_template("Tell me a few key achivements of {name}")
    #prompt = PromptTemplate(template=template, input_variables=['question'])

    llm_chain= prompt | llm

    res = llm_chain.invoke({"name":"Mahathma Gandhi"})
    print(res)



if __name__== "__main__":
    main()
