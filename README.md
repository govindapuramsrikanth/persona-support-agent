# 🤖 AI Support Agent

An intelligent AI-powered customer support assistant that understands customer queries, remembers conversation context, detects customer emotions, and escalates serious issues by creating support tickets.

---

## 🚀 Features

### 💬 AI Chat Support
- Users can ask support-related questions
- AI generates human-like responses
- Maintains conversation context

### 🧠 RAG (Retrieval Augmented Generation)
- Loads company documents
- Retrieves relevant policy information
- Provides accurate answers based on knowledge base

### 🎭 Customer Persona Detection
Detects customer emotions like:

- Angry customers
- Normal users
- Confused users

and changes responses accordingly.

### 🚨 Human Escalation System
Automatically detects serious complaints and creates support tickets.

Example:

User:
"I requested refund many times. Nobody helped me."

System:
- Detects frustration
- Creates ticket
- Sends escalation response


### 🎫 Ticket Management

Stores escalated issues with:

- Ticket ID
- Customer problem
- Emotion
- Status
- Created time


---

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI
- Uvicorn

### AI
- Groq API
- Llama 3 Model

### Vector Search
- Sentence Transformers
- Vector Database

### Frontend
- HTML
- CSS
- JavaScript

### Version Control
- Git
- GitHub


---

## 📂 Project Structure
persona-support-agent/

├── src/
│ ├── document_loader.py
│ ├── retriever.py
│ ├── persona_detector.py
│ ├── response_generator.py
│ ├── escalation.py
│ └── ticket_manager.py
│
├── frontend/
│ ├── index.html
│ ├── style.css
│ └── script.js
│
├── data/
│ └── refund_policy.md
│
├── api.py
├── requirements.txt
└── README.md



---

## ▶️ How To Run

Clone repository:

```bash
git clone <repository-url>



Install dependencies:
pip install -r requirements.txt



Start backend:
uvicorn api:app



Open frontend:
src/frontend/index.html



🌟 Future Improvements
User authentication
Database integration
Admin dashboard
Voice support
WhatsApp integration



👨‍💻 Developer

Built by Srikanth Raipally