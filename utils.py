"""
=========================================================
Utility Functions
---------------------------------------------------------
This file contains helper functions used by the chatbot.
=========================================================
"""

import os
import time
from datetime import datetime


# =========================================================
# CHAT HISTORY FILE
# =========================================================

CHAT_HISTORY_FILE = "data/chat_history.txt"


# =========================================================
# CREATE HISTORY FILE
# =========================================================

def create_history_file():
    """
    Creates the chat history file if it doesn't exist.
    """

    folder = "data"

    if not os.path.exists(folder):
        os.makedirs(folder)

    if not os.path.exists(CHAT_HISTORY_FILE):
        with open(CHAT_HISTORY_FILE, "w", encoding="utf-8") as file:
            file.write("=========== CHAT HISTORY ===========\n\n")


# =========================================================
# SAVE CHAT HISTORY
# =========================================================

def save_chat(user, bot):
    """
    Save conversation to chat_history.txt
    """

    create_history_file()

    timestamp = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    with open(CHAT_HISTORY_FILE, "a", encoding="utf-8") as file:

        file.write(f"[{timestamp}]\n")
        file.write(f"You     : {user}\n")
        file.write(f"RuleBot : {bot}\n")
        file.write("-" * 50 + "\n")


# =========================================================
# CURRENT TIME
# =========================================================

def current_time():

    return datetime.now().strftime("%I:%M:%S %p")


# =========================================================
# CURRENT DATE
# =========================================================

def current_date():

    return datetime.now().strftime("%d %B %Y")


# =========================================================
# CURRENT DAY
# =========================================================

def current_day():

    return datetime.now().strftime("%A")


# =========================================================
# CURRENT MONTH
# =========================================================

def current_month():

    return datetime.now().strftime("%B")


# =========================================================
# CURRENT YEAR
# =========================================================

def current_year():

    return datetime.now().strftime("%Y")


# =========================================================
# CURRENT DATE & TIME
# =========================================================

def current_datetime():

    return datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")


# =========================================================
# SESSION START TIME
# =========================================================

SESSION_START = datetime.now()


def session_duration():

    duration = datetime.now() - SESSION_START

    minutes = duration.seconds // 60

    seconds = duration.seconds % 60

    return f"{minutes} minute(s) {seconds} second(s)"


# =========================================================
# SIMPLE TYPING DELAY
# =========================================================

def typing_delay():

    time.sleep(0.8)


# =========================================================
# CLEAR CHAT HISTORY
# =========================================================

def clear_chat_history():

    create_history_file()

    with open(CHAT_HISTORY_FILE, "w", encoding="utf-8") as file:

        file.write("=========== CHAT HISTORY ===========\n\n")


# =========================================================
# WORD COUNTER
# =========================================================

def count_words(text):

    return len(text.split())


# =========================================================
# CHARACTER COUNTER
# =========================================================

def count_characters(text):

    return len(text)


# =========================================================
# BOT VERSION
# =========================================================

def bot_version():

    return "RuleBot Version 1.0"


# =========================================================
# BOT AUTHOR
# =========================================================

def bot_author():

    return "Shiv Koli"


# =========================================================
# INTERNSHIP NAME
# =========================================================

def internship():

    return "DecodeLabs AI Internship"