# ============================================================
# Project Name : StudyMate - Rule Based Student Assistant
# File Name    : responses.py
#
# Description:
# Stores all chatbot responses, motivational quotes,
# study tips, programming facts, mood responses,
# compliments, small talk responses, etc.
# ============================================================

import random

# ============================================================
# GREETINGS
# ============================================================

GREETINGS = [

    "Hello! 👋",

    "Hi! Nice to meet you.",

    "Welcome to StudyMate.",

    "Hey! How can I help you today?",

    "Hello Student!",

    "Greetings! 😊",

    "Hi there! Ready to learn something new?",

    "Welcome back! Hope you're having a productive day.",

    "Hello! Let's make today a learning day.",

    "Nice to see you again!"
]

# ============================================================
# GOODBYE
# ============================================================

GOODBYE = [

    "Goodbye! Have a wonderful day.",

    "See you again. Happy Learning!",

    "Take care.",

    "Bye! Keep Studying.",

    "Best of Luck for your studies.",

    "See you soon. 😊",

    "Keep learning and keep growing.",

    "Have an amazing day ahead.",

    "Take care and stay positive.",

    "Until next time!"
]

# ============================================================
# THANK YOU
# ============================================================

THANKS = [

    "You're Welcome 😊",

    "Happy to help.",

    "Anytime!",

    "Glad I could help.",

    "No problem.",

    "Always here for you.",

    "My pleasure!",

    "You're most welcome.",

    "Happy Learning!",

    "Keep asking great questions."
]

# ============================================================
# STUDY TIPS
# ============================================================

STUDY_TIPS = [

    "Study for 45 minutes and take a 10 minute break.",

    "Practice coding every day.",

    "Always revise your notes before sleeping.",

    "Make handwritten notes.",

    "Solve previous year questions.",

    "Understand concepts instead of memorizing.",

    "Avoid multitasking while studying.",

    "Drink enough water during study.",

    "Keep your phone away while studying.",

    "Consistency is more important than motivation.",

    "Teach someone else what you learned today.",

    "Study difficult subjects in the morning.",

    "Create a daily timetable and follow it.",

    "Focus on understanding rather than mugging up.",

    "Practice more than you read.",

    "Use flashcards for revision.",

    "Keep your study desk clean.",

    "Take short breaks to improve concentration.",

    "Sleep at least 7-8 hours daily.",

    "Set small achievable goals every day."
]

# ============================================================
# MOTIVATIONAL QUOTES
# ============================================================

MOTIVATION = [

    "Believe in yourself.",

    "Every expert was once a beginner.",

    "Success comes from consistency.",

    "Hard work beats talent.",

    "Never stop learning.",

    "Small improvements every day create huge success.",

    "Don't compare yourself with others.",

    "Discipline creates freedom.",

    "Dream big and stay focused.",

    "Success is earned, not given.",

    "Push yourself because no one else will do it for you.",

    "Learning is a lifelong journey.",

    "Every day is another chance to improve.",

    "Stay positive and keep working hard.",

    "Your future depends on what you do today."
]

# ============================================================
# PYTHON FACTS
# ============================================================

PYTHON_FACTS = [

    "Python was created by Guido van Rossum.",

    "Python supports Object Oriented Programming.",

    "Python is widely used in Artificial Intelligence.",

    "Python is one of the easiest programming languages.",

    "Python supports multiple programming paradigms.",

    "Python has a huge collection of libraries.",

    "Python is used in Machine Learning and Data Science.",

    "Python is an interpreted language.",

    "Python is open-source.",

    "Python supports cross-platform development.",

    "Python is one of the most popular programming languages in the world.",

    "Python uses indentation instead of braces.",

    "Python is used by Google, Netflix and Instagram.",

    "Python is excellent for automation.",

    "Python is beginner-friendly."
]
# ============================================================
# JAVA TIPS
# ============================================================

JAVA_TIPS = [

    "Learn OOP concepts first.",

    "Practice Collections Framework.",

    "Understand Exception Handling.",

    "Practice Multithreading.",

    "Learn JDBC after Core Java.",

    "Practice coding daily.",

    "Master Inheritance and Polymorphism.",

    "Understand Interfaces and Abstract Classes.",

    "Always handle exceptions properly.",

    "Learn Java Streams API.",

    "Practice solving DSA problems using Java.",

    "Understand Garbage Collection.",

    "Use meaningful variable names.",

    "Practice File Handling.",

    "Understand Lambda Expressions.",

    "Write clean and readable code."
]

# ============================================================
# SQL TIPS
# ============================================================

SQL_TIPS = [

    "Practice JOIN queries.",

    "Understand GROUP BY and HAVING.",

    "Learn Subqueries.",

    "Practice Aggregate Functions.",

    "Understand Normalization.",

    "Learn Indexing.",

    "Practice writing complex SELECT queries.",

    "Learn Views and Stored Procedures.",

    "Understand Foreign Keys.",

    "Always backup your database.",

    "Practice Transactions.",

    "Use aliases for better readability.",

    "Learn Window Functions.",

    "Avoid SELECT * in large databases.",

    "Understand Database Relationships."
]

# ============================================================
# GENERAL FACTS
# ============================================================

GENERAL_FACTS = [

    "Honey never spoils.",

    "Light travels faster than sound.",

    "The Earth revolves around the Sun in about 365 days.",

    "The human brain has around 86 billion neurons.",

    "Octopuses have three hearts.",

    "Bananas are berries but strawberries are not.",

    "Water expands when it freezes.",

    "The tallest mountain above sea level is Mount Everest.",

    "The speed of light is about 300,000 km/s.",

    "The first programmer was Ada Lovelace."
]

# ============================================================
# COMPLIMENTS
# ============================================================

COMPLIMENTS = [

    "You're doing an amazing job! 🌟",

    "Keep learning. You're improving every day.",

    "You're smarter than you think.",

    "Great question!",

    "I like your curiosity.",

    "Stay consistent and you'll achieve your goals.",

    "You're becoming a better programmer every day.",

    "Keep believing in yourself.",

    "Excellent! Keep it up.",

    "Learning suits you. 😊"
]

# ============================================================
# MOOD RESPONSES
# ============================================================

MOOD_RESPONSES = {

    "happy":
        "😊 That's wonderful! Keep smiling and enjoy your day.",

    "sad":
        "💙 Don't worry. Every bad day eventually comes to an end.",

    "angry":
        "Take a deep breath. Stay calm and think positively.",

    "stressed":
        "Take a short break, drink some water and relax for a few minutes.",

    "tired":
        "You should take some rest. Health always comes first.",

    "excited":
        "That's awesome! I hope everything goes well for you.",

    "confused":
        "Don't worry. Every expert was once confused. Keep learning."
}

# ============================================================
# SMALL TALK
# ============================================================

SMALL_TALK = {

    "weather":
        "I can't access live weather, but I hope it's a beautiful day outside. ☀",

    "music":
        "Music is a great way to refresh your mind while studying.",

    "movies":
        "Watching a good movie after completing your work is always enjoyable.",

    "cricket":
        "Cricket is one of the most popular sports in India.",

    "football":
        "Football has millions of fans around the world.",

    "ai":
        "Artificial Intelligence is one of the fastest-growing technologies today.",

    "python":
        "Python is my favourite language because it's simple and powerful."
}

# ============================================================
# UNKNOWN RESPONSES
# ============================================================

UNKNOWN = [

    "Sorry, I didn't understand that.",

    "Please try another command.",

    "Type HELP to see available commands.",

    "I'm still learning new commands.",

    "Can you rephrase your question?",

    "I'm not sure about that yet.",

    "I don't have an answer for that right now.",

    "Let's talk about studies, programming or technology.",

    "Please ask something related to my available features.",

    "Interesting question! Unfortunately I don't know that yet."
]
# ============================================================
# MEMORY MESSAGES
# ============================================================

MEMORY_MESSAGES = {

    "remember":
        "Great! I'll remember that during this session. 😊",

    "forgot":
        "Okay! I've forgotten that information.",

    "not_found":
        "I don't remember that yet. Tell me first.",

    "memory_cleared":
        "All remembered information has been cleared successfully."
}

# ============================================================
# BAD LANGUAGE RESPONSE
# ============================================================

BAD_LANGUAGE = [

    "Let's keep our conversation respectful. 😊",

    "Please use polite language.",

    "I'm here to help you. Let's be respectful.",

    "Kind words make conversations better.",

    "Let's continue with respectful language."
]

# ============================================================
# HELP TEXT
# ============================================================

HELP_TEXT = """

================ AVAILABLE COMMANDS ================

👋 Basic
• hi
• hello
• hey
• bye
• thanks

📅 Date & Time
• date
• time
• day

📚 Study
• study tip
• motivation

💻 Programming
• python
• java
• sql

🧮 Calculator
• calc 25+35
• 25+35*5

🎓 CGPA
• cgpa 85
• percentage 8.6

💡 Fun
• fact
• compliment

😊 Mood
• I am happy
• I am sad
• I am stressed

💬 Small Talk
• weather
• music
• cricket
• football
• movies

ℹ Other
• about
• help

====================================================

"""

# ============================================================
# RANDOM RESPONSE FUNCTIONS
# ============================================================

def greeting():
    return random.choice(GREETINGS)


def goodbye():
    return random.choice(GOODBYE)


def thanks():
    return random.choice(THANKS)


def study_tip():
    return random.choice(STUDY_TIPS)


def motivation():
    return random.choice(MOTIVATION)


def python_fact():
    return random.choice(PYTHON_FACTS)


def java_tip():
    return random.choice(JAVA_TIPS)


def sql_tip():
    return random.choice(SQL_TIPS)


def random_fact():
    return random.choice(GENERAL_FACTS)


def compliment():
    return random.choice(COMPLIMENTS)


def mood_response(mood):

    mood = mood.lower()

    if mood in MOOD_RESPONSES:
        return MOOD_RESPONSES[mood]

    return "I hope you're having a wonderful day. 😊"


def small_talk(topic):

    topic = topic.lower()

    if topic in SMALL_TALK:
        return SMALL_TALK[topic]

    return "Let's talk about something interesting!"


def bad_language():

    return random.choice(BAD_LANGUAGE)


def memory_message(key):

    return MEMORY_MESSAGES.get(
        key,
        "Memory response not found."
    )


def help_text():

    return HELP_TEXT


def unknown():
    return random.choice(UNKNOWN)