def chatbot():
    print("🤖 ChatBot: Hello! I am your friendly bot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello", "hey"]:
            print("🤖 ChatBot: Hello there! How can I help you?")

        elif "your name" in user_input:
            print("🤖 ChatBot: I am RuleBot 1.0!")

        elif "how are you" in user_input:
            print("🤖 ChatBot: I'm just code, but I'm running fine! 😄")

        elif "time" in user_input:
            from datetime import datetime
            print("🤖 ChatBot: The current time is",
                  datetime.now().strftime("%H:%M:%S"))

        elif user_input in ["bye", "exit", "quit"]:
            print("🤖 ChatBot: Goodbye! Have a great day! 👋")
            break

        else:
            print("🤖 ChatBot: Sorry, I didn't understand that.")


# Run the chatbot
chatbot()