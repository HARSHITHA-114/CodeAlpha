import random
responses = {
    "hello": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm doing well, thank you!", "I'm good, thanks for asking.", "All good here!"],
    "bye": ["Goodbye!", "See you later!", "Bye! Take care!"],
    "default": ["I'm not sure I understand.", "Could you please rephrase that?", "Sorry, I didn't get that."]
}
# Function to generate response based on user input
def generate_response(user_input):
    input_lower = user_input.lower()
    for key in responses:
        if key in input_lower:
            return random.choice(responses[key])
    return random.choice(responses["default"])

# Main function to run the chatbot
def chatbot():
    print("Welcome to the Chatbot!")
    print("You can start chatting. Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print(generate_response(user_input))
            break
        else:
            print("Bot:", generate_response(user_input))

# Run the chatbot
chatbot()
