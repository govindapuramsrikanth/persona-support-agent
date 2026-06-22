from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from src.response_generator import generate_response


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# temporary API memory
chat_history = []


class ChatRequest(BaseModel):
    question: str



@app.get("/")
def home():
    return {
        "message": "AI Support Agent Running"
    }



@app.post("/chat")
def chat(request: ChatRequest):

    answer = generate_response(
        request.question,
        chat_history
    )


    chat_history.append(
        {
            "customer": request.question,
            "agent": answer
        }
    )


    return {
        "answer": answer
    }