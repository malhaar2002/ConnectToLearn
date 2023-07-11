#importing langchain modules
from langchain.document_loaders import UnstructuredExcelLoader
from langchain.vectorstores import Chroma
from langchain.prompts import PromptTemplate
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
from langchain import OpenAI, VectorDBQA
from langchain.llms import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.text_splitter import CharacterTextSplitter
from langchain.text_splitter import TokenTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.document_loaders import TextLoader
import sys
sys.path.append('../config.py')
from config import OPENAI_API_KEY

#loading the excel files
loader = UnstructuredExcelLoader(
    "excel/database.xlsx"
)

docs = loader.load()

text_splitter_character = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=300
)
#docs = TextLoader('file.txt').load()
#embedding
all_splits = text_splitter_character.split_documents(docs)
#db = FAISS.from_documents(text_character, OpenAIEmbeddings())

# create the open-source embedding function
vectorstore = Chroma.from_documents(documents=all_splits,embedding=OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY))

query = "Who is Rucha Joshi"
docs =vectorstore.similarity_search(query)
print(docs)
# load it into Chroma

