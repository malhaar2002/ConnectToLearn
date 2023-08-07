from langchain.memory import ConversationBufferMemory
from config import OPENAI_API_KEY
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
import langchain.embeddings 
from langchain.document_loaders import UnstructuredExcelLoader
from langchain.vectorstores import Chroma
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
llm = ChatOpenAI(model_name="gpt-4", temperature=0)
from langchain.chains import RetrievalQA
from langchain.tools import Tool
from langchain.agents.types import AgentType
from langchain.agents import initialize_agent

#excel file loader function
def Loader(excel_file_url, document_loader):
    loader = document_loader(
    excel_file_url
    )
    data_to_split = loader.load()
    return data_to_split

#Splitters
def document_splitter(data_to_split, chunk_size, chunk_overlap, splitting_function):
    text_splitter = splitting_function(chunk_size = chunk_size, chunk_overlap = chunk_overlap)
    all_splits = text_splitter.split_documents(data_to_split)
    return all_splits


#embedding functions which uses Chroma vectore store
def embed_documents(splitted_document):
    vectorstore = Chroma.from_documents(documents=splitted_document,embedding=OpenAIEmbeddings())
    return vectorstore

#Template for the model one
def template_1():
    template = """You are owned by Plaksha University. You help with connecting user who have a particular interest in a topic to a Professor who have experience in such topic. You also can answer questions regarding a professor. When you are asked about a professor, ensure you provide a well detailed answer to it.
    Ensure you go through the below context before answering a question, if you do not know the answer just tell the user that you do not have any information about that. If you are asked to provide or recommend a professor in a field, check for more than one professor in that field. Only return one professor name if there is only one professor in such field

    You can only get the answer from the context:-
    {context}
    Also, get a if there is not professor in the similar field, recommend a professor that his field is similar
    Question: {question}
    Helpful Answer:"""
    QA_CHAIN_PROMPT = PromptTemplate(input_variables=["context","question"],template=template,)
    return QA_CHAIN_PROMPT

def retrieval(QA_CHAIN_PROMPT, vectorstore):
    qa_chain = RetrievalQA.from_chain_type(llm,
                                       retriever=vectorstore.as_retriever(),
                                       chain_type_kwargs={"prompt": QA_CHAIN_PROMPT})
    return qa_chain


# This function get the question and use relevant_documents to search some key words 
def search_relevant_doc(vectorestore, question):    
    a = vectorestore.as_retriever(search_type="mmr")
    ans = a.get_relevant_documents(question)
    return ans

def memory():
    conversational_memory = ConversationBufferMemory(
    memory_key="chat_history", return_messages=True
    )
    return conversational_memory

def question_factory(prof_info_1, prof_info_2, conversational_memory):
    system_message = """
        "Always use all the tool provided"
        "pass in any question I passed to you directly to the tools do not change anything"
        "You should get a professor name"
        "If you do not get the answer through a tool, use the second a one"
        """
    tools = [
        Tool(
            name="prof_info_1",
            func=prof_info_1.run,
            description="The first Tool to answer questions ",
        ),
        Tool(
            name="qa-prof_2",
            func=prof_info_2.run,
            description="Use this tool when there is not answer from the first one",
        )
    ]
    executor = initialize_agent(
        agent = AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
        tools=tools,
        llm=llm,
        memory=conversational_memory,
        agent_kwargs={"system_message": system_message},
        verbose=True,
    )


def main():
    #Load documents
    data_to_split = Loader("../excel/faculty.xlsx", UnstructuredExcelLoader)

    # split documents
    all_splits = document_splitter(data_to_split, 1000, 200, RecursiveCharacterTextSplitter)

    # embed and store
    vectorstore = embed_documents(all_splits)

    #prompt
    QA_CHAIN_PROMPT = template_1

    #setting up first retrieval
    qa_chain = retrieval(QA_CHAIN_PROMPT, vectorstore)

    qexecutor = question_factory(qa_chain, qa_chain, memory())    

    # Loop
    user_input = input("Input your question \n") 
    answer = executor.run(human_input=user_input)
    print(answer
if __name__ == "__main__":
    main()
