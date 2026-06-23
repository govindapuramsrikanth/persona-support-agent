# 🤖 Persona Based AI Support Agent

An AI-powered customer support assistant that understands customer queries, detects customer emotions/personas, retrieves relevant knowledge, and generates personalized support responses using AI.

The system helps businesses automate customer support by identifying different customer situations like refund requests, angry customers, confused users, and technical issues.

---

# 🌐 Live Demo

🚀 **Frontend Application**

https://persona-support-agent-ui.onrender.com


⚙️ **Backend API Documentation**

https://persona-support-agent-g4pf.onrender.com/docs


---

# 🚀 Features

## 💬 AI Chat Support

- Users can ask customer-support related questions
- AI generates human-like support responses
- Stores chat history for better user experience
- Real-time chatbot interface


---

## 🧠 RAG (Retrieval Augmented Generation)

- Loads support/company documents
- Retrieves relevant information from knowledge base
- Provides context-aware responses


---

## 🎭 Customer Persona Detection

The system detects different customer personas:

- 😡 Angry Customers
- 🙂 Normal Users
- 😕 Confused Users
- 🔧 Technical Issue Users


Based on the detected persona, the AI changes its response style.


Example:

User:

```
I am angry. I want refund immediately.
```

System:

```
Persona: Angry Customer

Response:
I understand your frustration.
I am here to help resolve your issue.
```


---

## 🎫 Support Intelligence

The assistant can handle:

- Refund related queries
- Product issues
- Account problems
- General customer questions
- Support guidance


---

# ⚙️ How It Works


```
User Message

      ↓

Frontend Chat Interface

      ↓

FastAPI Backend

      ↓

Persona Detection

      ↓

Knowledge Retrieval (RAG)

      ↓

AI Response Generation

      ↓

Personalized Customer Reply
```


---

# 🛠️ Tech Stack


## Frontend

- HTML
- CSS
- JavaScript


## Backend

- Python
- FastAPI
- Uvicorn


## AI

- Groq API
- Llama 3 Model


## Vector Search / RAG

- Sentence Transformers
- Vector Database


## Deployment

- Render


## Version Control

- Git
- GitHub


---

# 📂 Project Structure


```text
persona-support-agent/

│
├── src/
│
│   ├── document_loader.py
│   ├── retriever.py
│   ├── persona_detector.py
│   └── response_generator.py
│
│
├── frontend/
│
│   ├── index.html
│   ├── style.css
│   └── script.js
│
│
├── data/
│
│   └── refund_policy.md
│
│
├── api.py
├── requirements.txt
├── README.md

```


---

# ▶️ How To Run Locally


Clone the repository:


```bash
git clone <your-repository-url>
```


Install dependencies:


```bash
pip install -r requirements.txt
```


Start FastAPI backend:


```bash
uvicorn api:app
```


Open frontend:


```text
src/frontend/index.html
```


---

# 📌 Example Usage


User:

```
My account login is not working.
```


AI:

```
I understand you are facing login issues.

Let me help you troubleshoot your problem.
```


---


# 🚀 Future Improvements

- User authentication
- Database integration
- Admin dashboard
- Voice assistant support
- WhatsApp integration
- Multi-language support


---


# 👨‍💻 Developer

Built by

**Srikanth Raipally**   and **Dudam Lokesh**
