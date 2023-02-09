import nltk
import random

nltk.download('punkt')

greetings = ['hello', 'hi', 'hey', 'hola', 'wassup', 'greetings']
greetingsresponses = ['hi there!', 'hey!', '*nods*', 'hi!', 'hello!', 'I am glad! You are talking to me']
howareyou = ['how are you?', 'how are you doing?', 'how is it going']
howareyouresponses = ['i am good, thanks for asking!', 'amazing now you are here']

def respond(user_input):
    for word in nltk.word_tokenize(user_input):
        if word.lower() in greetings:
            return random.choice(greetingsresponses),
        if word.lower() in howareyou:
            return random.choice(howareyouresponses)
    return "Sorry, I did not understand what you said."

while True:
    user_input = input("You: ")
    bot_response = respond(user_input)
    print("Bot: ", bot_response)

