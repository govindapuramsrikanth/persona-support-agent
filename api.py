from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os

from src.persona_detector import detect_persona
from src.retriever import retrieve_documents
from src.response_generator import generate_response



# Create FastAPI app
app = FastAPI(
    title="AI Support Agent",
    description="Persona based AI Customer Support Agent",
    version="1.0.0"
)



# Enable frontend access (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://persona-support-agent-ui.onrender.com"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




# Request model
class ChatRequest(BaseModel):

    message: str





# Home route
@app.get("/")
def home():

    return {
        "status": "success",
        "message": "AI Support Agent API is running 🚀",
        "docs": "/docs"
    }





# Health check route
@app.get("/health")
def health():

    return {
        "status": "healthy"
    }






# Chat API
@app.post("/chat")
def chat(request: ChatRequest):


    # user question from frontend
    user_message = request.message



    # detect customer emotion/persona
    persona = detect_persona(
        user_message
    )



    # get related documents
    documents = retrieve_documents(
        user_message
    )



    # generate AI response
    answer = generate_response(
        user_message,
        persona,
        documents
    )



    # send response to frontend
    return {

        "question": user_message,

        "persona": persona,

        "answer": answer

    }