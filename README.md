# 🦜 LangChain Learning Journey

A hands-on repository documenting my journey of learning **LangChain, Large Language Models (LLMs), Generative AI, and AI application development using Python**.

This repository contains practical implementations, experiments, and code examples as I explore the fundamentals of building LLM-powered applications.

## 🚀 What I'm Learning

- **LangChain Fundamentals** — Models, chains, prompts, and LCEL
- **LLMs** — Integrating Google Gemini and OpenAI models
- **Prompt Engineering** — Static prompts, dynamic prompts, and prompt templates
- **Embeddings** — Generating vector embeddings using Hugging Face and OpenAI
- **Semantic Search** — Finding relevant documents using cosine similarity
- **Chatbots** — Building command-line conversational applications
- **Streamlit** — Creating interactive AI-powered web applications
- **Structured Outputs** — Generating structured responses using schemas and Pydantic
- **RAG (Retrieval-Augmented Generation)** — Exploring document-based question answering
- **Environment Management** — Managing API keys and dependencies securely

## 🛠️ Tech Stack

- Python
- LangChain
- Google Gemini API
- OpenAI API
- Hugging Face
- Sentence Transformers
- Scikit-learn
- Streamlit
- Python-dotenv
- Git and GitHub

## 📂 Repository Structure

```text
LangChain-Models/
├── Chat_models/
├── Embeddings_Model/
├── LangChain_Prompts/
├── LLM_CHAT_prompts/
├── LLM_Structured_Output/
├── LLMs-models/
├── Python_learn/
├── .gitignore
├── requirements.txt
└── README.md
```

*The folders contain practical exercises and implementations as I progress through the learning journey.*

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/guptamayank9/Langchain_Models.git
cd Langchain_Models
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root and add the API key required by your selected model:

```env
GOOGLE_API_KEY=your_google_api_key
OPENAI_API_KEY=your_openai_api_key
```

Use only the keys required by your application. Never commit your `.env` file or expose API keys publicly.

### 5. Run your Python scripts

```bash
python your_script.py
```

For Streamlit applications:

```bash
streamlit run your_app.py
```

Replace the example filenames with the actual Python filenames in the relevant folders.

## 🎯 Learning Goals

- Understand how LangChain connects applications with LLMs.
- Build reusable prompt templates and model workflows.
- Work with embeddings and semantic similarity.
- Develop interactive AI applications.
- Learn the foundations of RAG and retrieval-based systems.
- Write clean, reusable, and maintainable Python code.

## 📈 Progress

This repository is continuously updated with new concepts, experiments, and implementations as I learn and build with LangChain.

## 🤝 Contributions

Suggestions, feedback, and learning resources are welcome.

---

**Learning by building, one AI concept at a time.** 🚀
