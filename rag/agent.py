from langchain.agents import create_agent
from rag.llm import get_llm
from rag.tools import search_policies

def build_agent():
    return create_agent(
        model=get_llm(),
        tools=[search_policies],
        system_prompt=(
            "You are a helpful company policy assistant. "
            "Always use the search_policies tool to find the answer. "
            "If the policies do not contain the answer, say you don't know."
        ),
    )