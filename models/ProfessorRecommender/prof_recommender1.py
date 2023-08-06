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

