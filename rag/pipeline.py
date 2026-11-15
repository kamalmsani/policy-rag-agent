from rag.agent import build_agent

_agent = build_agent()

def ask(question: str) -> str:
    result = _agent.invoke({"messages": [("user", question)]})
    return result["messages"][-1].content