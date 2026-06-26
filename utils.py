
# Project Name : StudyMate - Rule Based Student Assistant
# File Name    : utils.py
#
# Description:
# This file contains helper functions used throughout
# the chatbot application.


from datetime import datetime



# Returns current date and time

def get_current_datetime():
    return datetime.now()



# Returns current time
# Example: 08:35 PM

def get_current_time():

    return datetime.now().strftime("%I:%M %p")



# Returns current date
# Example: 26 June 2026

def get_current_date():

    return datetime.now().strftime("%d %B %Y")



# Returns current day
# Example: Monday

def get_current_day():

    return datetime.now().strftime("%A")



# Returns chat timestamp
# Example:
# [08:30 PM]

def get_timestamp():

    return datetime.now().strftime("[%I:%M %p]")



# Save chat history

def save_chat(sender, message):

    with open("chat_history.txt", "a", encoding="utf-8") as file:

        file.write(f"{get_timestamp()} {sender}: {message}\n")



# Performs simple calculator operations

def calculate(expression):

    try:

        answer = eval(expression)

        return str(answer)

    except:

        return "Invalid mathematical expression."



# Percentage to CGPA

def percentage_to_cgpa(percentage):

    try:

        percentage = float(percentage)

        cgpa = percentage / 9.5

        return round(cgpa, 2)

    except:

        return None



# CGPA to Percentage

def cgpa_to_percentage(cgpa):

    try:

        cgpa = float(cgpa)

        percentage = cgpa * 9.5

        return round(percentage, 2)

    except:

        return None



# Welcome Message

def welcome_message():

    return """
🎓 Welcome to StudyMate

I can help you with:

✅ Date
✅ Time
✅ Day
✅ Study Tips
✅ Motivation
✅ Python Facts
✅ Java Guide
✅ SQL Guide
✅ Calculator
✅ CGPA Calculator
✅ Percentage Calculator

Type HELP to see all commands.
"""