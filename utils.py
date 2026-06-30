# ============================================================
# Project Name : StudyMate - Rule Based Student Assistant
# File Name    : utils.py
#
# Description:
# Utility functions used throughout the chatbot.
# ============================================================

from datetime import datetime
import os
import math


# ============================================================
# DATE & TIME FUNCTIONS
# ============================================================

def get_current_datetime():
    return datetime.now()

def get_current_time():
    return datetime.now().strftime("%I:%M %p")


def get_current_date():
    return datetime.now().strftime("%d %B %Y")


def get_current_day():
    return datetime.now().strftime("%A")


def get_timestamp():
    return datetime.now().strftime("[%d-%m-%Y %I:%M %p]")


# ============================================================
# CHAT HISTORY
# ============================================================

CHAT_FILE = "chat_history.txt"


def save_chat(sender, message):
    """
    Saves chat history.
    """

    with open(CHAT_FILE, "a", encoding="utf-8") as file:

        file.write(f"{get_timestamp()} {sender}: {message}\n")


def load_chat():

    """
    Loads complete chat history.
    """

    if not os.path.exists(CHAT_FILE):
        return ""

    with open(CHAT_FILE, "r", encoding="utf-8") as file:
        return file.read()


def clear_chat_history():

    """
    Clears chat history file.
    """

    with open(CHAT_FILE, "w", encoding="utf-8") as file:
        file.write("")


def export_chat(file_name="StudyMate_Chat.txt"):

    """
    Exports chat history.
    """

    if not os.path.exists(CHAT_FILE):
        return False

    with open(CHAT_FILE, "r", encoding="utf-8") as old_file:

        data = old_file.read()

    with open(file_name, "w", encoding="utf-8") as new_file:

        new_file.write(data)

    return True


# ============================================================
# CHAT STATISTICS
# ============================================================

def get_chat_statistics():

    """
    Returns statistics of current chat.
    """

    if not os.path.exists(CHAT_FILE):

        return {

            "messages": 0,
            "user_messages": 0,
            "bot_messages": 0
        }

    with open(CHAT_FILE, "r", encoding="utf-8") as file:

        lines = file.readlines()

    total = len(lines)

    users = 0
    bot = 0

    for line in lines:

        if "Student:" in line:
            users += 1

        elif "StudyMate:" in line:
            bot += 1

    return {

        "messages": total,
        "user_messages": users,
        "bot_messages": bot

    }


# ============================================================
# SAFE CALCULATOR
# ============================================================

ALLOWED = {

    "__builtins__": None,

    "sqrt": math.sqrt,

    "pow": pow,

    "abs": abs,

    "round": round

}


def calculate(expression):

    """
    Safe mathematical calculator.
    """

    try:

        answer = eval(expression, ALLOWED, {})

        return str(answer)

    except Exception:

        return "Invalid mathematical expression."


# ============================================================
# CGPA UTILITIES
# ============================================================

def percentage_to_cgpa(percentage):

    try:

        percentage = float(percentage)

        cgpa = percentage / 9.5

        return round(cgpa, 2)

    except:

        return None


def cgpa_to_percentage(cgpa):

    try:

        cgpa = float(cgpa)

        percentage = cgpa * 9.5

        return round(percentage, 2)

    except:

        return None


# ============================================================
# SESSION TIMER
# ============================================================

START_TIME = datetime.now()


def get_session_duration():

    """
    Returns current session duration.
    """

    now = datetime.now()

    duration = now - START_TIME

    seconds = int(duration.total_seconds())

    hours = seconds // 3600

    minutes = (seconds % 3600) // 60

    sec = seconds % 60

    return f"{hours}h {minutes}m {sec}s"


# ============================================================
# WELCOME MESSAGE
# ============================================================

def welcome_message():

    return """
🎓 Welcome to StudyMate

I am your Rule-Based Student Assistant.

I can help you with:

✅ Date
✅ Time
✅ Day

✅ Study Tips
✅ Motivation

✅ Python
✅ Java
✅ SQL

✅ Calculator

✅ Percentage ⇄ CGPA

✅ Random Facts

✅ Compliments

✅ Small Talk

✅ Chat History

Type HELP to see all available commands.

Happy Learning! 🚀
"""


# ============================================================
# VERSION
# ============================================================

def app_version():

    return "StudyMate Version 2.0"


# ============================================================
# ABOUT
# ============================================================

def about_project():

    return (
        "StudyMate\n\n"
        "Rule-Based Student Assistant\n\n"
        "Developed using Python & Tkinter.\n"
        "IBM AI Internship Project.\n\n"
        "Developer : Saurav Shukla"
    )