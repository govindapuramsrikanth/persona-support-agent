from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from src.persona_detector import detect_persona
from src.retriever import retrieve_documents
from src.response_generator import generate_response


app = FastAPI()


# ADD CORS IMMEDIATELY AFTER app creation
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "status": "success",
        "message": "AI Support Agent API is running 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/chat")
async def chat(request: ChatRequest):

    user_message = request.message

    persona = detect_persona(user_message)

    documents = retrieve_documents(user_message)

    answer = generate_response(
        user_message,
        persona,
        documents
    )

    return {
        "question": user_message,
        "persona": persona,
        "answer": answer
    }