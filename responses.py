
# Project Name : StudyMate - Rule Based Student Assistant
# File Name    : responses.py
#
# Description:
# This file stores all predefined chatbot responses.


import random

# Greetings

GREETINGS = [
    "Hello! 👋",
    "Hi! Nice to meet you.",
    "Welcome to StudyMate.",
    "Hey! How can I help you today?",
    "Hello Student!"
]


# Goodbye

GOODBYE = [
    "Goodbye! Have a wonderful day.",
    "See you again. Happy Learning!",
    "Take care.",
    "Bye! Keep Studying.",
    "Best of Luck for your studies."
]


# Thank You

THANKS = [
    "You're Welcome 😊",
    "Happy to help.",
    "Anytime!",
    "Glad I could help.",
    "No problem."
]


# Study Tips

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

    "Consistency is more important than motivation."
]


# Motivation

MOTIVATION = [

    "Believe in yourself.",

    "Every expert was once a beginner.",

    "Success comes from consistency.",

    "Hard work beats talent.",

    "Never stop learning.",

    "Small improvements every day create huge success.",

    "Don't compare yourself with others.",

    "Discipline creates freedom."
]


# Python Facts

PYTHON_FACTS = [

    "Python was created by Guido van Rossum.",

    "Python supports Object Oriented Programming.",

    "Python is widely used in Artificial Intelligence.",

    "Python is one of the easiest programming languages.",

    "Python supports multiple programming paradigms.",

    "Python has a huge collection of libraries.",

    "Python is used in Machine Learning and Data Science."
]


# Java Tips

JAVA_TIPS = [

    "Learn OOP concepts first.",

    "Practice Collections Framework.",

    "Understand Exception Handling.",

    "Practice Multithreading.",

    "Learn JDBC after Core Java.",

    "Practice coding daily."
]


# SQL Tips

SQL_TIPS = [

    "Practice JOIN queries.",

    "Understand GROUP BY and HAVING.",

    "Learn Subqueries.",

    "Practice Aggregate Functions.",

    "Understand Normalization.",

    "Learn Indexing."
]


# Unknown Responses

UNKNOWN = [

    "Sorry, I didn't understand that.",

    "Please try another command.",

    "Type HELP to see available commands.",

    "I'm still learning new commands.",

    "Can you rephrase your question?"
]


# Random Response Functions

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


def unknown():
    return random.choice(UNKNOWN)