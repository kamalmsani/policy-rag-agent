from langchain_community.vectorstores import FAISS
from rag.embeddings import get_embeddings

def build_vectorstore(chunks):
    return FAISS.from_documents(chunks, get_embeddings())