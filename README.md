# 🌐 Global AI Knowledge Bridge

A web platform designed to make complex, technical knowledge accessible to billions — breaking down **language** and **complexity** barriers using cutting-edge AI.

---

## 🚀 The Problem: Information is Locked Away

Critical knowledge in fields like **healthcare**, **global policy**, and **academic research** is overwhelmingly published in English and written for technical experts.  
This creates **two massive barriers** for billions worldwide:

- 🌏 **The Language Barrier** — Non-English speakers are immediately excluded from the conversation.  
- 🧠 **The Complexity Barrier** — Documents are too long and filled with jargon, even for native speakers.

This **knowledge gap** prevents local experts, students, and communities from benefiting from global insights.

---

## ✨ Our Solution: An AI-Powered Simplification Pipeline

The **Global AI Knowledge Bridge** eliminates these barriers through a simple yet powerful workflow:

1. **📤 Upload Any Document**  
   Users can upload complex PDFs — such as WHO reports or academic research papers.

2. **🪄 Instant Page-by-Page Summaries**  
   The **Cerebras gpt-oss-120b** model processes the document and generates clear, concise summaries for each page — removing the complexity barrier.

3. **💬 Ask Questions in Any Language**  
   Users can ask questions about the document in their native language (e.g., Hindi).  
   Using **Meta Llama 3**, the system responds with context-aware answers in that same language — removing the language barrier.

---

## 🧠 Tech Stack & Architecture

| Layer | Technology | Purpose |
|-------|-------------|----------|
| **Frontend** | React, Tailwind CSS | Interactive and responsive user interface |
| **Backend** | FastAPI (Python) | Efficient and lightweight API server |
| **AI Summarization** | Cerebras `gpt-oss-120b` | Handles complex document understanding and summarization |
| **AI Q&A** | Meta Llama 3 (`meta-llama/llama-3-8b-instruct`) via OpenRouter | Context-aware multilingual Q&A |
| **Deployment** | Docker (Multi-Container) | Scalable and portable deployment environment |

---

## 🏆 Integration of Sponsor Technologies

### 🧩 **Cerebras: The Heavy-Lifter for Complex Documents**
We use **Cerebras gpt-oss-120b** for its unparalleled capacity to handle long, dense contexts.  
It powers the summarization engine — the “magic” that simplifies global knowledge.

### 🗣️ **Meta: The Bridge for Human Communication**
**Meta Llama 3** acts as the human bridge.  
With excellent multilingual understanding and instruction-following, it enables users worldwide to interact naturally with complex reports — in their own languages.

# 🐳 Docker: The Delivery Vehicle for Global Access

We containerized both the **frontend (Nginx)** and **backend (FastAPI)** using Docker.  
With a single command, any organization — from NGOs to universities — can deploy the entire platform:

```bash
docker-compose up --build
```

---

This democratizes not only the knowledge, but the tool itself.

---

## ⚙️ **How to Run Locally**

### 1️⃣ Clone the Repository

```bash
git clone [your-github-repo-link-here]
cd global-ai-knowledge-bridge
```

---

### 2️⃣ Set Up Environment Variables

Create a `.env` file in the project root and add your API keys:

```bash
CEREBRAS_API_KEY='your-cerebras-key'
OPENROUTER_API_KEY='your-openrouter-key'
```

---

### 3️⃣ Build and Run with Docker

```bash
docker-compose up --build
```

---

### 4️⃣ Access the Application

- **Frontend:** [http://localhost:3000](http://localhost:3000)  
- **Backend API Docs:** [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧩 **Architecture Overview**

```plaintext
                   ┌──────────────────────────┐
                   │        FRONTEND          │
                   │  React + Tailwind (Nginx)│
                   └────────────┬─────────────┘
                                │
                                ▼
                   ┌──────────────────────────┐
                   │        BACKEND           │
                   │     FastAPI + Python     │
                   └────────────┬─────────────┘
                                │
               ┌────────────────┼────────────────┐
               ▼                ▼                ▼
        Cerebras AI        Meta Llama 3       Database (optional)
   (Summarization Engine)  (Multilingual Q&A)
```

---

## 💡 **Vision**

The **Global AI Knowledge Bridge** envisions a future where:

🌍 Every person — regardless of language or background — can access and understand global knowledge.  
🤖 AI doesn’t just translate; it transforms information into something meaningful for all.
