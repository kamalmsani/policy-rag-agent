# Company Policy Assistant
Live demo: https://kamal-policy-assistant.streamlit.app/

An AI agent with a Streamlit chat page. It answers questions about company policies by searching a text file and using a Groq language model.

## How it works (Architecture)

1. `data/policies.txt` holds the company policies.
2. The text is cut into small chunks and turned into numbers (embeddings).
3. The agent searches those chunks to find the best match for a question.
4. The Groq model writes the answer from what it found.

## Project files

- `app.py` - the Streamlit chat page
- `rag/config.py` - settings (model name, file paths)
- `rag/llm.py` - connects to the Groq model
- `rag/embeddings.py`, `rag/vectorstore.py`, `rag/ingest.py` - make the policies searchable
- `rag/tools.py` - the search tool the agent uses
- `rag/agent.py` - the agent
- `rag/pipeline.py` - the `ask()` function the app calls

## How to run

1. Create a virtual environment with Python 3.12 and activate it.
2. Install packages: `pip install -r requirements.txt`
3. Create a `.env` file with your key: `GROQ_API_KEY=your_key_here`
4. Start the app: `streamlit run app.py`
5. Open `localhost:8501` in your browser.

## Notes

- Never share your `.env` file or upload it to GitHub.
- If you see a "model not found" error, choose another model name in `rag/config.py`.

## Limitations

- Amswers come only from data/policies.txt, so the assistant cannot amswer questions the file does not cover.
- Wrong amswers are possible: the AI model can misread a policy, so important decisions should be checked with HR.
