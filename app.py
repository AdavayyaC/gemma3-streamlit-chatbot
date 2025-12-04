from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()  # Loads variables from .env

# Optional: ensure tracing is enabled
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
# Streamlit Title
st.title('LangChain Demo with Gemma 3 (Ollama)')

# User Input
input_text = st.text_input("Ask something...")

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond clearly and accurately."),
        ("user", "Question: {question}")
    ]
)

# Use Gemma 3 model from Ollama
llm = Ollama(model="gemma3:1b")  # or "gemma3:1b" if small version

output_parser = StrOutputParser()

# Chain
chain = prompt | llm | output_parser

# Run
if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)
