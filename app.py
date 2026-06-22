from src.response_generator import generate_response


chat_history = []


def chat():

    print("AI Support Agent Started")
    print("Type 'exit' to stop")

    while True:

        user_question = input("\nCustomer: ")

        if user_question.lower() == "exit":
            break


        answer = generate_response(
            user_question,
            chat_history
        )


        chat_history.append(
            {
                "customer": user_question,
                "agent": answer
            }
        )


        print("\nAgent:")
        print(answer)


chat()