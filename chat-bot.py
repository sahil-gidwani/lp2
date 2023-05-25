import random

bot_responses = [
    "Welcome to Burger King! How can I assist you today?",
    "Hello! How may I help you with your Burger King experience?",
    "I'm doing great. How about you?",
    "At Burger King, we offer a wide range of delicious burgers and meals. Is there anything specific you're looking for?",
    "You can contact us through phone, email, or our website's contact form for any inquiries or feedback.",
    "You're welcome! Enjoy your meal at Burger King.",
    "Thank you for choosing Burger King! Have a great day!"
]

def generate_response(user_input):
    user_input = user_input.lower()

    if "hi" in user_input or "hello" in user_input:
        return random.choice(bot_responses[:2])
    elif "how are you" in user_input:
        return bot_responses[2]
    elif "menu" in user_input or "food" in user_input:
        return bot_responses[3]
    elif "contact" in user_input or "feedback" in user_input:
        return bot_responses[4]
    elif "thank you" in user_input:
        return bot_responses[5]
    elif "goodbye" in user_input:
        return bot_responses[6]
    else:
        return "I'm sorry, I didn't understand. Can you please rephrase your question?"

print("Bot: Welcome to Burger King! How can I assist you today?")

while True:
    user_input = input("User: ")
    response = generate_response(user_input)
    print("Bot:", response)

    if "goodbye" in user_input:
        break