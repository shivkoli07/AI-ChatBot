"""
=========================================================
Chatbot Engine
---------------------------------------------------------
This file controls the chatbot logic.
=========================================================
"""

import re
import random
from datetime import datetime

from responses import (
    GREETINGS,
    FAREWELLS,
    THANKS,
    HELP_MESSAGE,
    DEFAULT_RESPONSES,
    JOKES,
    QUOTES,
)

from knowledge import KNOWLEDGE


def get_bot_response(user_input):

    text = user_input.lower().strip()

    # ----------------------------------------------------
    # Greetings
    # ----------------------------------------------------

    if re.search(r"\b(hello|hi|hey|hii|heyy)\b", text):
        return random.choice(GREETINGS)

    # ----------------------------------------------------
    # Good Morning / Afternoon / Evening / Night
    # ----------------------------------------------------

    elif "good morning" in text:
        return "🌞 Good Morning! Hope you have a wonderful day."

    elif "good afternoon" in text:
        return "😊 Good Afternoon! Hope your day is going well."

    elif "good evening" in text:
        return "🌇 Good Evening! Nice to see you."

    elif "good night" in text:
        return "🌙 Good Night! Sweet Dreams."

    # ----------------------------------------------------
    # Goodbye
    # ----------------------------------------------------

    elif re.search(r"\b(bye|goodbye|exit|quit)\b", text):
        return random.choice(FAREWELLS)

    # ----------------------------------------------------
    # Thank You
    # ----------------------------------------------------

    elif re.search(r"\b(thanks|thank you|thx)\b", text):
        return random.choice(THANKS)

    # ----------------------------------------------------
    # Help
    # ----------------------------------------------------

    elif "help" in text:
        return HELP_MESSAGE

    # ----------------------------------------------------
    # Introduction
    # ----------------------------------------------------

    elif (
        "your name" in text
        or "who are you" in text
        or "introduce yourself" in text
        or "what are you" in text
    ):

        return (
            "👋 Hello!\n\n"
            "I am ChatBot.\n\n"
            "I was designed and developed by Shiv Pramod Koli during his AI Internship.\n\n"
            "My purpose is to help users by answering questions, "
            "providing useful information, and making conversations easy and helpful."
        )

    # ----------------------------------------------------
    # Developer
    # ----------------------------------------------------

    elif (
        "who developed you" in text
        or "who created you" in text
        or "who made you" in text
        or "developer" in text
    ):

        return (
            "👨‍💻 I was designed and developed by "
            "Shiv Pramod Koli during his AI Internship."
        )

    # ----------------------------------------------------
    # What are you doing
    # ----------------------------------------------------

    elif (
        "what are you doing" in text
        or "what are you up to" in text
    ):

        return (
            "😊 I'm waiting for your questions and always ready to help!"
        )

    # ----------------------------------------------------
    # Age
    # ----------------------------------------------------

    elif (
        "how old are you" in text
        or "your age" in text
    ):

        return (
            "😄 I'm just a chatbot, so I don't really have an age."
        )

    # ----------------------------------------------------
    # Can you help me
    # ----------------------------------------------------

    elif (
        "can you help me" in text
        or "help me" in text
    ):

        return (
            "Of course! 😊\n"
            "You can ask me about:\n"
            "• Countries\n"
            "• Fruits\n"
            "• Vegetables\n"
            "• AI\n"
            "• Computer Science\n"
            "• Programming Languages\n"
            "• Current Date & Time\n"
            "• General Knowledge"
        )

    # ----------------------------------------------------
    # OK
    # ----------------------------------------------------

    elif text in ["ok", "okay", "okk"]:

        return random.choice([
            "😊 Great!",
            "👍 Alright!",
            "Sounds good!",
            "Okay! What would you like to know next?"
        ])

    # ----------------------------------------------------
    # Yes
    # ----------------------------------------------------

    elif text in ["yes", "yeah", "yup"]:

        return "😊 Great! Please continue."

    # ----------------------------------------------------
    # No
    # ----------------------------------------------------

    elif text in ["no", "nope"]:

        return "No worries! Ask me something else."

    # ----------------------------------------------------
    # Time
    # ----------------------------------------------------

    elif "time" in text:

        return "🕒 Current Time: " + datetime.now().strftime("%I:%M:%S %p")

    # ----------------------------------------------------
    # Date
    # ----------------------------------------------------

    elif "date" in text:

        return "📅 Today's Date: " + datetime.now().strftime("%d %B %Y")

    # ----------------------------------------------------
    # Day
    # ----------------------------------------------------

    elif (
        "day" in text
        or "today" in text
        or "what day is it" in text
    ):

        return "📆 Today is " + datetime.now().strftime("%A")

    # ----------------------------------------------------
    # Knowledge Base
    # ----------------------------------------------------

    for keyword, response in KNOWLEDGE.items():

        if keyword in text:
            return response

    # ----------------------------------------------------
    # Simple Calculator
    # ----------------------------------------------------

    try:

        if any(op in text for op in ["+", "-", "*", "/"]):

            answer = eval(text)

            return f"🧮 Answer: {answer}"

    except:
        pass

    # ----------------------------------------------------
    # Default Response
    # ----------------------------------------------------

    return random.choice(DEFAULT_RESPONSES)