import streamlit as st
from rag.pipeline import ask

st.set_page_config(page_title="Policy Assistant", page_icon="🤖")
st.title("Company Policy Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.write(m["content"])

question = st.chat_input("Ask a question about the policies...")

if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                answer = ask(question)
            except Exception:
                answer = (
                    "Sorry, I could not get an answer right now. "
                    "Please check your internet connection and try again."
                )
        st.write(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})