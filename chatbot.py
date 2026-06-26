# ============================================================
# Project Name : StudyMate - Rule Based Student Assistant
# File Name    : chatbot.py
#
# Description:
# Main chatbot logic.
# Receives user message and returns chatbot response.
# ============================================================

import re

from responses import (
    greeting,
    goodbye,
    thanks,
    study_tip,
    motivation,
    python_fact,
    java_tip,
    sql_tip,
    unknown
)

from utils import (
    get_current_time,
    get_current_date,
    get_current_day,
    calculate,
    percentage_to_cgpa,
    cgpa_to_percentage,
    save_chat
)


class StudyMateBot:

    def __init__(self):
        pass


    # --------------------------------------------------------
    # Process User Message
    # --------------------------------------------------------

    def get_response(self, message):

        user_message = message.strip().lower()

        # Save User Chat
        save_chat("Student", message)

        # ===============================
        # Greeting
        # ===============================

        if user_message in [
            "hi",
            "hello",
            "hey",
            "good morning",
            "good afternoon",
            "good evening"
        ]:

            bot = greeting()

            save_chat("StudyMate", bot)

            return bot


        # ===============================
        # Thank You
        # ===============================

        elif user_message in [
            "thanks",
            "thank you",
            "thankyou"
        ]:

            bot = thanks()

            save_chat("StudyMate", bot)

            return bot


        # ===============================
        # Bye
        # ===============================

        elif user_message in [
            "bye",
            "exit",
            "quit",
            "close"
        ]:

            bot = goodbye()

            save_chat("StudyMate", bot)

            return bot


        # ===============================
        # Time
        # ===============================

        elif "time" in user_message:

            bot = f"Current Time : {get_current_time()}"

            save_chat("StudyMate", bot)

            return bot


        # ===============================
        # Date
        # ===============================

        elif "date" in user_message:

            bot = f"Today's Date : {get_current_date()}"

            save_chat("StudyMate", bot)

            return bot


        # ===============================
        # Day
        # ===============================

        elif "day" in user_message:

            bot = f"Today is {get_current_day()}"

            save_chat("StudyMate", bot)

            return bot


        # ===============================
        # Study Tips
        # ===============================

        elif user_message in [
            "study",
            "study tip",
            "study tips",
            "tips"
        ]:

            bot = study_tip()

            save_chat("StudyMate", bot)

            return bot


        # ===============================
        # Motivation
        # ===============================

        elif user_message in [
            "motivate me",
            "motivation",
            "motivate",
            "inspire me"
        ]:

            bot = motivation()

            save_chat("StudyMate", bot)

            return bot


        # ===============================
        # Python
        # ===============================

        elif user_message in [
            "python",
            "python fact",
            "python facts"
        ]:

            bot = python_fact()

            save_chat("StudyMate", bot)

            return bot


        # ===============================
        # Java
        # ===============================

        elif user_message in [
            "java",
            "java tips",
            "java guide"
        ]:

            bot = java_tip()

            save_chat("StudyMate", bot)

            return bot


        # ===============================
        # SQL
        # ===============================

        elif user_message in [
            "sql",
            "sql tips",
            "database"
        ]:

            bot = sql_tip()

            save_chat("StudyMate", bot)

            return bot
                # ===============================
        # Calculator
        # ===============================

        elif user_message.startswith("calc"):

            try:

                expression = message[4:].strip()

                result = calculate(expression)

                bot = f"Answer = {result}"

            except:

                bot = "Example : calc 25+35"

            save_chat("StudyMate", bot)

            return bot


        # ===============================
        # Direct Mathematical Expression
        # Example : 10+20*3
        # ===============================

        elif re.fullmatch(r"[0-9+\-*/(). ]+", user_message):

            result = calculate(user_message)

            bot = f"Answer = {result}"

            save_chat("StudyMate", bot)

            return bot


        # ===============================
        # Percentage To CGPA
        # Example : cgpa 85
        # ===============================

        elif user_message.startswith("cgpa"):

            try:

                percentage = user_message.split()[1]

                result = percentage_to_cgpa(percentage)

                if result is None:

                    bot = "Invalid Percentage."

                else:

                    bot = f"Estimated CGPA : {result}"

            except:

                bot = "Example : cgpa 85"

            save_chat("StudyMate", bot)

            return bot


        # ===============================
        # CGPA To Percentage
        # Example : percentage 8.2
        # ===============================

        elif user_message.startswith("percentage"):

            try:

                cgpa = user_message.split()[1]

                result = cgpa_to_percentage(cgpa)

                if result is None:

                    bot = "Invalid CGPA."

                else:

                    bot = f"Percentage : {result}%"

            except:

                bot = "Example : percentage 8.4"

            save_chat("StudyMate", bot)

            return bot


        # ===============================
        # About Project
        # ===============================

        elif user_message == "about":

            bot = (
                "StudyMate is a Rule-Based Student Assistant.\n\n"
                "Features:\n"
                "- Study Tips\n"
                "- Motivation\n"
                "- Python Facts\n"
                "- Java Guide\n"
                "- SQL Guide\n"
                "- Calculator\n"
                "- Date & Time\n"
                "- CGPA Calculator\n"
                "- Percentage Calculator"
            )

            save_chat("StudyMate", bot)

            return bot


        # ===============================
        # Help Command
        # ===============================

        elif user_message == "help":

            bot = (
                "\n========== AVAILABLE COMMANDS ==========\n\n"
                "hello\n"
                "hi\n"
                "bye\n"
                "date\n"
                "time\n"
                "day\n"
                "study tip\n"
                "motivation\n"
                "python\n"
                "java\n"
                "sql\n"
                "calc 20+30\n"
                "25+30*4\n"
                "cgpa 85\n"
                "percentage 8.6\n"
                "about\n"
                "help\n"
            )

            save_chat("StudyMate", bot)

            return bot


        # ===============================
        # Who are you
        # ===============================

        elif user_message in [

            "who are you",

            "your name",

            "what is your name"

        ]:

            bot = (
                "I am StudyMate 🤖\n"
                "A Rule-Based Student Assistant developed in Python."
            )

            save_chat("StudyMate", bot)

            return bot


        # ===============================
        # Creator
        # ===============================

        elif user_message in [

            "creator",

            "developer",

            "who developed you"

        ]:

            bot = (
                "I was developed by Saurav Shukla "
                "using Python and Tkinter."
            )

            save_chat("StudyMate", bot)

            return bot


        # ===============================
        # Unknown Command
        # ===============================

        else:

            bot = unknown()

            save_chat("StudyMate", bot)

            return bot