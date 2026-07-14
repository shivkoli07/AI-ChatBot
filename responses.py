"""
=========================================================
Response Library
---------------------------------------------------------
This file contains all predefined chatbot responses.
=========================================================
"""

import random

# =========================================================
# GREETINGS
# =========================================================

GREETINGS = [

    "Hello! 👋 How can I help you today?",

    "Hi there! 😊",

    "Hey! Nice to meet you.",

    "Welcome! What would you like to know?",

    "Hello! I'm RuleBot, your AI assistant.",

    "Hi! Hope you're having a wonderful day.",

    "Hey there! How may I assist you?",

    "Greetings! Ready to chat?",

    "Hello! Feel free to ask me anything.",

    "Hi! Let's have a great conversation."

]

# =========================================================
# FAREWELLS
# =========================================================

FAREWELLS = [

    "Goodbye! 👋 Have a wonderful day.",

    "Bye! See you again soon.",

    "Take care and stay safe!",

    "It was nice chatting with you.",

    "See you next time!",

    "Bye! Keep learning and keep smiling.",

    "Have a fantastic day ahead!",

    "Hope to see you again soon.",

    "Goodbye! Happy coding!",

    "Until next time!"

]

# =========================================================
# THANK YOU RESPONSES
# =========================================================

THANKS = [

    "You're welcome! 😊",

    "Happy to help!",

    "My pleasure!",

    "Anytime!",

    "Glad I could help.",

    "No problem at all!",

    "You're most welcome!",

    "Always here to help!",

    "You're welcome. Have a great day!",

    "It was my pleasure."

]

# =========================================================
# HELP MESSAGE
# =========================================================

HELP_MESSAGE = """
I can help you with:

👋 Greetings
🕒 Current Time
📅 Current Date
📆 Current Day
🍎 Fruits
🥕 Vegetables
🌍 Countries
💻 Information Technology
🧠 Artificial Intelligence
🐍 Python
☕ Java
🌐 HTML
🎨 CSS
⚡ JavaScript
🗄 SQL
🖥 Computer Science
😂 Jokes
➕ Basic Math

Just ask naturally!

Examples:

• Hello
• What is AI?
• Tell me about Python
• What is HTML?
• What is today's date?
• What time is it?
• Tell me about India
• Tell me about Apple
• Bye
"""

# =========================================================
# UNKNOWN / FALLBACK RESPONSES
# =========================================================

DEFAULT_RESPONSES = [

    "🤔 I'm not sure I understand that.",

    "Sorry, I don't have information about that yet.",

    "Could you please rephrase your question?",

    "I haven't learned that topic yet.",

    "Interesting question! Unfortunately I don't know the answer.",

    "I'm still learning. Try asking something else.",

    "Sorry, I don't have a rule for that yet.",

    "Can you ask that in a different way?",

    "I don't understand. Type 'help' to see what I can do.",

    "Let's try another question."

]

# =========================================================
# MOTIVATIONAL QUOTES
# =========================================================

QUOTES = [

    "Success is the sum of small efforts repeated every day.",

    "Believe in yourself and all that you are.",

    "Dream big. Start small. Act now.",

    "Learning never exhausts the mind.",

    "Every expert was once a beginner.",

    "Stay positive. Work hard. Make it happen.",

    "Don't stop until you're proud.",

    "Consistency beats talent when talent doesn't work hard.",

    "The future belongs to those who learn more skills.",

    "Coding is today's language of creativity."

]

# =========================================================
# JOKES
# =========================================================

JOKES = [

    "😂 Why do programmers prefer dark mode? Because light attracts bugs.",

    "😂 Why do Java developers wear glasses? Because they don't C#.",

    "😂 Why did the computer catch a cold? Because it left its Windows open.",

    "😂 Why was the JavaScript developer sad? Because he didn't Node how to Express himself.",

    "😂 There are only 10 types of people: those who understand binary and those who don't.",

    "😂 Debugging is like being the detective in a crime movie where you are also the criminal.",

    "😂 Why was the computer tired? It had too many tabs open.",

    "😂 Why don't robots panic? Because they keep their circuits together."

]

# =========================================================
# RANDOM RESPONSE FUNCTIONS
# =========================================================

def random_greeting():
    return random.choice(GREETINGS)


def random_farewell():
    return random.choice(FAREWELLS)


def random_thanks():
    return random.choice(THANKS)


def random_default():
    return random.choice(DEFAULT_RESPONSES)


def random_quote():
    return random.choice(QUOTES)


def random_joke():
    return random.choice(JOKES)