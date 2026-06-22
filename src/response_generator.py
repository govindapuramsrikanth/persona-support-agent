from groq import Groq
from dotenv import load_dotenv
import os

from src.retriever import retrieve_documents
from src.persona_detector import detect_persona
from src.escalation import check_escalation
from src.ticket_manager import create_ticket


load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_response(question, chat_history):

    # Detect customer emotion
    persona = detect_persona(question)


    # Check escalation
    escalate = check_escalation(question, persona)


    if escalate:

        ticket_id = create_ticket(question, persona)

        return f"""
I understand this issue needs extra attention.

I have escalated your request to our support team.

Ticket ID: #{ticket_id}

Our support team will review your case and contact you soon.
"""


    # Retrieve company information
    documents = retrieve_documents(question)


    context = ""

    for doc in documents:
        context += doc + "\n"


    # Previous conversation memory
    memory = ""

    for chat in chat_history:
        memory += f"""
Customer: {chat['customer']}
Agent: {chat['agent']}
"""


    prompt = f"""

You are a helpful customer support agent.

Customer Emotion:
{persona}


Response Rules:

If Customer Emotion is ANGRY:
- Apologize first.
- Show empathy.
- Calm the customer.

If Customer Emotion is CONFUSED:
- Explain slowly in simple steps.

If Customer Emotion is NORMAL:
- Give a normal professional answer.


Previous Conversation:
{memory}


Company Information:
{context}


Current Customer Question:
{question}


Answer naturally using company information and previous conversation.

"""


    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )


    return response.choices[0].message.content