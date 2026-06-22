import os
from groq import Groq
from dotenv import load_dotenv


load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_response(message, persona, documents):

    context = "\n".join(documents)


    prompt = f"""

You are an AI customer support agent.

Customer Persona:
{persona}


Company Knowledge:
{context}


Customer Message:
{message}


Give a helpful customer support response.

"""


    completion = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.5
    )


    return completion.choices[0].message.content