# 💬 Gemma 3 Streamlit Chatbot

A **local AI chatbot** built using **Gemma 3 (Ollama)**, **LangChain**, and **Streamlit**, with optional **LangSmith** tracking for prompts and responses.  
This project is designed for learning, experimentation, and exploring lightweight local LLMs on a standard PC.

---

## ⚡ Features

-  **Local LLM**: Gemma 3:1B (Ollama) runs fully on your machine  
-  **LangChain integration**: Prompt templates, chains, and output parsing  
-  **Streamlit UI**: Easy-to-use chat interface  
-  **LangSmith tracking**: Logs prompts, responses, and chain steps for debugging/experiments  
-  **Lightweight**: Runs on 16 GB RAM without GPU  
-  **Expandable**: Swap models, add memory, or integrate RAG later  

---
## 📂 Project Structure
```bash
langchainP/
│── app.py           # Streamlit + LangChain chatbot code
│── requirements.txt # Python dependencies
│── .env.example     # Example env variables
│── .gitignore       # Ignore venv, cache, .env
```
## 🛠️ Setup Instructions

1. **Clone the repository**

```bash
git clone <your-repo-url>
cd <repo-folder>

```
2. **Create a virtual environment**
```bash
python -m venv venv
.\venv\Scripts\activate   # Windows
```

3. **Install dependencies**
 ```bash
   pip install -r requirements.txt
```
4. Add your LangSmith API key (optional)
Create a .env file in the root folder:
```bash
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_api_key_here
```
-If you don’t want tracking, you can skip this step.

5. Pull the Gemma 3 model via Ollama
```bash
ollama pull gemma3:1b
```

Run the chatbot
```bash
streamlit run app.py
```

## 📝 Usage
Type any question in the input box
Chatbot responds using Gemma 3
If LangSmith is enabled, every interaction is tracked for later inspection

## ⚙️ Note:
The .env file is not included in the repo for security
Virtual environment folder venv/ is ignored via .gitignore
Upgrade to larger models (Gemma 3 4B or Phi Mini) if you have more RAM
