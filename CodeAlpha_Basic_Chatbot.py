import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hello|hey",
        ["Hello, how are you?",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by you.",]
    ],
    [
        r"how are you?",
        ["I am just a program, but I'm doing well! How about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright.", "No problem at all.",]
    ],
    [
        r"i'm (.*) doing good",
        ["That's great to hear!",]
    ],
    [
        r"what (.*) want?",
        ["I'm here to help you with any questions you may have.",]
    ],
    [
        r"(.*) created you?",
        ["I was created by a programmer.",]
    ],
    [
        r"bye|goodbye",
        ["Goodbye! It was nice talking to you.", "See you later!"]
    ],
]

def basic_chatbot():
    print("Hi! I'm a chatbot. Type 'bye' to exit.")

    chat = Chat(pairs, reflections)

    chat.converse()

if __name__ == "__main__":
    basic_chatbot()
