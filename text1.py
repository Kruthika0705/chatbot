import random


def get_response(user_input):
    user_input = user_input.lower()  
    
    
    greetings = ['hi', 'hello', 'hey', 'hola', 'howdy']
    farewells = ['bye', 'goodbye', 'see you', 'take care']
    questions = ['how are you', 'how is it going', 'how are you doing']
    
    if any(greeting in user_input for greeting in greetings):
        return random.choice(["Hello!", "Hi there!", "Hey! How can I assist you today?"])
    
    elif any(farewell in user_input for farewell in farewells):
        return random.choice(["Goodbye!", "See you later!", "Take care!"])
    
    elif any(question in user_input for question in questions):
        return random.choice(["I'm doing great, thanks for asking!", "I'm good! How about you?", "I'm just a bot, but thanks for asking!"])
    
    else:
        return "Sorry, I didn't understand that. Could you try asking something else?"


def chatbot():
    print("Welcome to the chatbot! Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        response = get_response(user_input)
        print(f"Bot: {response}")


if __name__ == "__main__":
    chatbot()
