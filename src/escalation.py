def check_escalation(question, persona):

    question = question.lower()

    escalation_words = [
        "complaint",
        "complain",
        "manager",
        "human",
        "support team",
        "legal",
        "court",
        "not helping",
        "worst service",
        "many times"
    ]


    for word in escalation_words:
        if word in question:
            return True


    if persona == "ANGRY":
        if "again" in question or "still" in question:
            return True


    return False