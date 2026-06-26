# gui.py
# ============================================================
# GUI for StudyMate Chatbot
# Part 1
# ============================================================

import tkinter as tk
from tkinter import scrolledtext, messagebox
from chatbot import StudyMateBot


class StudyMateGUI:

    def __init__(self):

        # -----------------------------
        # Create chatbot instance
        # -----------------------------
        self.bot = StudyMateBot()

        # -----------------------------
        # Main Window
        # -----------------------------
        self.root = tk.Tk()
        self.root.title("StudyMate - AI Study Assistant")

        self.root.geometry("900x650")
        self.root.minsize(800, 600)

        self.root.configure(bg="#EAF4FC")

        # -----------------------------
        # Fonts
        # -----------------------------
        self.title_font = ("Segoe UI", 20, "bold")
        self.header_font = ("Segoe UI", 12, "bold")
        self.chat_font = ("Segoe UI", 11)
        self.input_font = ("Segoe UI", 11)

        # -----------------------------
        # Colors
        # -----------------------------
        self.primary_color = "#1565C0"
        self.secondary_color = "#42A5F5"
        self.background = "#EAF4FC"
        self.chat_background = "#FFFFFF"
        self.button_color = "#1976D2"
        self.button_hover = "#0D47A1"

        # -----------------------------
        # Header
        # -----------------------------
        self.header_frame = tk.Frame(
            self.root,
            bg=self.primary_color,
            height=70
        )

        self.header_frame.pack(fill=tk.X)

        self.title_label = tk.Label(
            self.header_frame,
            text="StudyMate - Rule Based Study Assistant",
            font=self.title_font,
            fg="white",
            bg=self.primary_color
        )

        self.title_label.pack(pady=15)

        # -----------------------------
        # Chat Frame
        # -----------------------------
        self.chat_frame = tk.Frame(
            self.root,
            bg=self.background
        )

        self.chat_frame.pack(
            fill=tk.BOTH,
            expand=True,
            padx=10,
            pady=10
        )

        # -----------------------------
        # Scrollbar
        # -----------------------------
        self.scrollbar = tk.Scrollbar(
            self.chat_frame
        )

        self.scrollbar.pack(
            side=tk.RIGHT,
            fill=tk.Y
        )

        # -----------------------------
        # Chat Area
        # -----------------------------
        self.chat_area = scrolledtext.ScrolledText(
            self.chat_frame,
            wrap=tk.WORD,
            font=self.chat_font,
            bg=self.chat_background,
            fg="black",
            padx=12,
            pady=12,
            state="disabled"
        )

        self.chat_area.pack(
            fill=tk.BOTH,
            expand=True
        )

        # -----------------------------
        # Input Frame
        # -----------------------------
        self.input_frame = tk.Frame(
            self.root,
            bg=self.background
        )

        self.input_frame.pack(
            fill=tk.X,
            padx=10,
            pady=10
        )

        # -----------------------------
        # User Input
        # -----------------------------
        self.user_input = tk.Entry(
            self.input_frame,
            font=self.input_font
        )

        self.user_input.pack(
            side=tk.LEFT,
            fill=tk.X,
            expand=True,
            padx=(0, 10),
            ipady=8
        )

        # Press Enter to Send
        self.user_input.bind(
            "<Return>",
            self.send_message
        )

        # -----------------------------
        # Send Button
        # -----------------------------
        self.send_button = tk.Button(
            self.input_frame,
            text="Send",
            bg=self.button_color,
            fg="white",
            font=self.header_font,
            width=10,
            cursor="hand2",
            command=self.send_message
        )

        self.send_button.pack(
            side=tk.LEFT,
            padx=5
        )

        # -----------------------------
        # Clear Button
        # -----------------------------
        self.clear_button = tk.Button(
            self.input_frame,
            text="Clear",
            bg="#E53935",
            fg="white",
            font=self.header_font,
            width=10,
            cursor="hand2",
            command=self.clear_chat
        )

        self.clear_button.pack(
            side=tk.LEFT
        )
        self.send_button.bind("<Enter>", self.on_enter_send)
        self.send_button.bind("<Leave>", self.on_leave_send)
        self.clear_button.bind("<Enter>", self.on_enter_clear)
        self.clear_button.bind("<Leave>", self.on_leave_clear)

        # -----------------------------
        # Welcome Message
        # -----------------------------
        self.display_message(
            "StudyMate",
            "Hello! 👋\n\n"
            "I am StudyMate.\n"
            "Ask me questions related to your studies.\n\n"
            "Examples:\n"
            "- What is Python?\n"
            "- Explain OOP\n"
            "- What is SQL?\n"
            "- Difference between List and Tuple\n"
            "- What is Machine Learning?"
        )
            # ============================================================
    # Display Message
    # ============================================================

    def display_message(self, sender, message):
        """
        Display messages inside the chat area.
        """

        self.chat_area.config(state="normal")

        self.chat_area.insert(
            tk.END,
            f"{sender}:\n",
            "sender"
        )

        self.chat_area.insert(
            tk.END,
            f"{message}\n\n",
            "message"
        )

        self.chat_area.tag_config(
            "sender",
            foreground="#1565C0",
            font=("Segoe UI", 11, "bold")
        )

        self.chat_area.tag_config(
            "message",
            foreground="black",
            font=("Segoe UI", 11)
        )

        self.chat_area.config(state="disabled")
        self.chat_area.see(tk.END)

    # ============================================================
    # Send Message
    # ============================================================

    def send_message(self, event=None):
        """
        Handles user input and bot response.
        """

        user_text = self.user_input.get().strip()

        if user_text == "":
            return

        # Display user's message
        self.display_message("You", user_text)

        # Clear input field
        self.user_input.delete(0, tk.END)

        try:
            response = self.bot.get_response(user_text)
        except Exception as e:
            response = f"Error: {e}"

        self.display_message("StudyMate", response)

    # ============================================================
    # Clear Chat
    # ============================================================

    def clear_chat(self):
        """
        Clears all chat messages.
        """

        answer = messagebox.askyesno(
            "Clear Chat",
            "Do you really want to clear the conversation?"
        )

        if not answer:
            return

        self.chat_area.config(state="normal")
        self.chat_area.delete("1.0", tk.END)
        self.chat_area.config(state="disabled")

        self.display_message(
            "StudyMate",
            "Chat cleared successfully.\nHow can I help you today?"
        )

    # ============================================================
    # Hover Effects
    # ============================================================

    def on_enter_send(self, event):
        self.send_button.config(bg=self.button_hover)

    def on_leave_send(self, event):
        self.send_button.config(bg=self.button_color)

    def on_enter_clear(self, event):
        self.clear_button.config(bg="#C62828")

    def on_leave_clear(self, event):
        self.clear_button.config(bg="#E53935")
            # ============================================================
    # Focus on Input Box
    # ============================================================

    def focus_input(self):
        """
        Keeps the cursor inside the input field.
        """
        self.user_input.focus_set()

    # ============================================================
    # Window Closing Event
    # ============================================================

    def on_closing(self):
        """
        Confirm before closing the application.
        """
        close = messagebox.askokcancel(
            "Exit StudyMate",
            "Are you sure you want to exit?"
        )

        if close:
            self.root.destroy()

    # ============================================================
    # Status Bar
    # ============================================================

    def create_status_bar(self):
        """
        Creates a status bar at the bottom.
        """
        self.status_bar = tk.Label(
            self.root,
            text="StudyMate is Ready",
            bd=1,
            relief=tk.SUNKEN,
            anchor=tk.W,
            font=("Segoe UI", 10),
            bg="#F5F5F5"
        )

        self.status_bar.pack(
            side=tk.BOTTOM,
            fill=tk.X
        )

    # ============================================================
    # Update Status
    # ============================================================

    def set_status(self, text):
        """
        Updates the status bar text.
        """
        if hasattr(self, "status_bar"):
            self.status_bar.config(text=text)

    # ============================================================
    # Run Application
    # ============================================================

    def run(self):
        """
        Starts the GUI application.
        """

        # Create footer
        self.create_status_bar()

        # Focus on text box
        self.focus_input()

        # Window close event
        self.root.protocol(
            "WM_DELETE_WINDOW",
            self.on_closing
        )

        # Start GUI loop
        self.root.mainloop()