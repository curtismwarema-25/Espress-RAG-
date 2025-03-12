from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import GPT4All
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
model_path = os.getenv("GPT4ALL_MODEL_PATH")

# Ensure the model path is set
if not model_path:
    raise ValueError("❌ GPT4ALL_MODEL_PATH is not set in the .env file!")

# Debugging: Print model path
print(f"✅ Using GPT4All model at: {model_path}")

# Ensure model exists
if not os.path.exists(model_path):
    raise FileNotFoundError(f"❌ GPT4All model not found at {model_path}. Please download it.")

# Load documents safely
try:
    loader = TextLoader("documents.txt")
    documents = loader.load()
except FileNotFoundError:
    raise FileNotFoundError("❌ 'documents.txt' not found! Please add the file and try again.")

# Split text into chunks
text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=10)
docs = text_splitter.split_documents(documents)

# Use local embeddings instead of OpenAI
embedding_model = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en")
vectorstore = FAISS.from_documents(docs, embedding_model)

# Set up the RAG system with GPT4All
retriever = vectorstore.as_retriever()
llm = GPT4All(model=model_path, verbose=True, allow_download=False, device="cpu")

qa_chain = RetrievalQA.from_chain_type(llm, retriever=retriever)

# Ask a question
question = "Where is the Eiffel Tower?"
response = qa_chain.run(question)

print("Q:", question)
print("A:", response)
