import random

user_inputs = [
    "Hi",
    "Hello",
    "How are you?",
    "What services do you offer?",
    "How can I contact you?",
    "Thank you",
    "Goodbye"
]

bot_responses = [
    "Hi! How can I assist you today?",
    "Hello! How may I help you?",
    "I'm good. How about you?",
    "We offer a wide range of services. Can you please specify what you are looking for?",
    "You can contact us through phone, email, or our website's contact form.",
    "You're welcome!",
    "Goodbye! Have a great day!"
]

def generate_response(user_input):
    user_input = user_input.lower()

    if "hi" in user_input or "hello" in user_input:
        return random.choice(bot_responses[:2])
    elif "how are you" in user_input:
        return bot_responses[2]
    elif "services" in user_input:
        return bot_responses[3]
    elif "contact" in user_input:
        return bot_responses[4]
    elif "thank you" in user_input:
        return bot_responses[5]
    elif "goodbye" in user_input:
        return bot_responses[6]
    else:
        return "I'm sorry, I didn't understand. Can you please rephrase your question?"

print("Bot: Hi! How can I assist you today?")

while True:
    user_input = input("User: ")
    response = generate_response(user_input)
    print("Bot:", response)

    if "goodbye" in user_input:
        break
