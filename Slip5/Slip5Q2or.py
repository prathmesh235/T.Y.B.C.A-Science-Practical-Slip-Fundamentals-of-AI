
# Simple Chatbot using Predefined Rules

print("Chatbot: Hello! Welcome to the Simple Chatbot.")
print("Chatbot: Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Chatbot: Hello! How are you?")

    elif user_input == "how are you":
        print("Chatbot: I am fine. Thank you!")

    elif user_input == "what is your name":
        print("Chatbot: I am a simple Python chatbot.")

    elif user_input == "what can you do":
        print("Chatbot: I can answer simple predefined questions.")

    elif user_input == "bye":
        print("Chatbot: Goodbye! Have a nice day.")
        break

    else:
        print("Chatbot: Sorry, I don't understand that.")
