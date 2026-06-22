import json
import os
from datetime import datetime


TICKET_FILE = "tickets.json"


def create_ticket(question, persona):

    ticket = {
        "ticket_id": int(datetime.now().timestamp()),
        "customer_issue": question,
        "emotion": persona,
        "status": "OPEN",
        "created_at": str(datetime.now())
    }


    if os.path.exists(TICKET_FILE):

        with open(TICKET_FILE, "r") as file:
            tickets = json.load(file)

    else:
        tickets = []


    tickets.append(ticket)


    with open(TICKET_FILE, "w") as file:
        json.dump(tickets, file, indent=4)


    return ticket["ticket_id"]