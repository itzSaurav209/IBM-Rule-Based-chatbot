# chatbot.py
# ============================================================
# Project Name : StudyMate - Rule Based Student Assistant
# File Name    : chatbot.py
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
    random_fact,
    compliment,
    mood_response,
    small_talk,
    bad_language,
    help_text,
    unknown,
)

from utils import (
    get_current_time,
    get_current_date,
    get_current_day,
    calculate,
    percentage_to_cgpa,
    cgpa_to_percentage,
    save_chat,
    get_chat_statistics,
)

class StudyMateBot:

    def __init__(self):
        self.memory = {}

    def reply(self, text):
        save_chat("StudyMate", text)
        return text

    def get_response(self, message):

        user = message.strip()
        text = user.lower()

        save_chat("Student", user)

        # Greetings
        if text in ["hi","hello","hey","good morning","good evening","good afternoon"]:
            return self.reply(greeting())

        # Thanks
        if text in ["thanks","thank you","thankyou"]:
            return self.reply(thanks())

        # Goodbye
        if text in ["bye","exit","quit","close"]:
            return self.reply(goodbye())

        # Date Time
        if "time" in text:
            return self.reply(f"Current Time : {get_current_time()}")

        if "date" in text:
            return self.reply(f"Today's Date : {get_current_date()}")

        if "day" in text:
            return self.reply(f"Today is {get_current_day()}")

        # Study
        if text in ["study","study tip","study tips","tips"]:
            return self.reply(study_tip())

        if text in ["motivation","motivate me","motivate","inspire me"]:
            return self.reply(motivation())

        if text in ["python","python fact","python facts"]:
            return self.reply(python_fact())

        if text in ["java","java tips","java guide"]:
            return self.reply(java_tip())

        if text in ["sql","sql tips","database"]:
            return self.reply(sql_tip())

        if text in ["fact","random fact","tell me a fact"]:
            return self.reply(random_fact())

        if text in ["compliment","compliment me","praise me"]:
            return self.reply(compliment())

        # Mood
        for mood in ["happy","sad","angry","stressed","tired","excited","confused"]:
            if mood in text:
                return self.reply(mood_response(mood))

        # Small Talk
        for topic in ["weather","music","movies","movie","cricket","football","ai"]:
            if topic in text:
                return self.reply(small_talk(topic))

        # Memory
        m = re.search(r"my name is (.+)", text)
        if m:
            self.memory["name"] = m.group(1).title()
            return self.reply(f"Nice to meet you, {self.memory['name']}! I'll remember your name.")

        if "what is my name" in text:
            if "name" in self.memory:
                return self.reply(f"Your name is {self.memory['name']}.")
            return self.reply("I don't know your name yet. Tell me by saying 'My name is ...'")

        m = re.search(r"i am (\d{1,2}) years old", text)
        if m:
            self.memory["age"] = m.group(1)
            return self.reply("Okay! I'll remember your age.")

        if "how old am i" in text:
            if "age" in self.memory:
                return self.reply(f"You are {self.memory['age']} years old.")
            return self.reply("You haven't told me your age yet.")

        m = re.search(r"my favourite color is (.+)|my favorite color is (.+)", text)
        if m:
            color = m.group(1) or m.group(2)
            self.memory["color"] = color.title()
            return self.reply("Favourite color saved.")

        if "favorite color" in text or "favourite color" in text:
            if "color" in self.memory:
                return self.reply(f"Your favourite color is {self.memory['color']}.")
            return self.reply("You haven't told me your favourite color yet.")

        # Calculator
        if text.startswith("calc"):
            exp = user[4:].strip()
            return self.reply(f"Answer = {calculate(exp)}")

        if re.fullmatch(r"[0-9+\-*/(). ]+", text):
            return self.reply(f"Answer = {calculate(text)}")

        # CGPA
        if text.startswith("cgpa"):
            try:
                p = text.split()[1]
                return self.reply(f"Estimated CGPA : {percentage_to_cgpa(p)}")
            except:
                return self.reply("Example : cgpa 85")

        if text.startswith("percentage"):
            try:
                c = text.split()[1]
                return self.reply(f"Percentage : {cgpa_to_percentage(c)}%")
            except:
                return self.reply("Example : percentage 8.4")

        # Stats
        if text == "statistics":
            s = get_chat_statistics()
            return self.reply(
                f"Total Messages : {s['messages']}\n"
                f"Student Messages : {s['user_messages']}\n"
                f"Bot Replies : {s['bot_messages']}"
            )

        # Help
        if text == "help":
            return self.reply(help_text())

        # About
        if text == "about":
            return self.reply(
                "StudyMate\n\n"
                "Rule-Based Student Assistant\n"
                "Built using Python & Tkinter\n"
                "Developer : Saurav Shukla"
            )

        # Creator
        if text in ["creator","developer","who developed you","who made you"]:
            return self.reply("I was developed by Saurav Shukla using Python.")

        # Bad words
        bad_words = ["idiot","stupid","fuck","shit","madarchod","bhosdike","bc","mc"]
        if any(word in text for word in bad_words):
            return self.reply(bad_language())

        return self.reply(unknown())
