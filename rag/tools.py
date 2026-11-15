from langchain_core.tools import tool
from rag.ingest import load_and_split
from rag.vectorstore import build_vectorstore

_store = build_vectorstore(load_and_split())

@tool
def search_policies(question: str) -> str:
    """Search the company policies and return the most relevant passages."""
    results = _store.similarity_search(question, k=3)
    return "\n\n".join(doc.page_content for doc in results)