
# Project Name : StudyMate - Rule Based Student Assistant
# File Name    : main.py
# code by       : Saurav Shukla
# This file launches the graphical interface of the chatbot.


from gui import StudyMateGUI


def main():
    """
    Starts the Student Assistant application.
    """

    try:
        app = StudyMateGUI()
        app.run()

    except KeyboardInterrupt:
        print("\nApplication Closed Successfully.")

    except Exception as error:
        print("Unexpected Error:", error)


if __name__ == "__main__":
    main()