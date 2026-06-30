# gui.py
# ============================================================
# GUI for StudyMate Chatbot
# ============================================================

import tkinter as tk
from tkinter import scrolledtext, messagebox
from chatbot import StudyMateBot
from utils import (
    get_current_time,
    get_chat_statistics,
    export_chat,
    get_session_duration,
    app_version,
    about_project,
)


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
        self.root.geometry("980x720")
        self.root.minsize(900, 650)
        self.root.configure(bg="#F4F8FF")

        # -----------------------------
        # Fonts
        # -----------------------------
        self.title_font = ("Segoe UI", 20, "bold")
        self.subtitle_font = ("Segoe UI", 11)
        self.header_font = ("Segoe UI", 11, "bold")
        self.chat_font = ("Segoe UI", 11)
        self.input_font = ("Segoe UI", 11)
        self.small_font = ("Segoe UI", 9)

        # -----------------------------
        # Colors
        # -----------------------------
        self.primary_color = "#10407A"
        self.secondary_color = "#3C7DD9"
        self.accent_color = "#5A9CF5"
        self.background = "#F4F8FF"
        self.card_bg = "#FFFFFF"
        self.chat_bg = "#EAF1FB"
        self.entry_bg = "#FFFFFF"
        self.text_color = "#16314A"
        self.user_bubble = "#C7DDF8"
        self.bot_bubble = "#F2F7FF"
        self.button_color = "#3C7DD9"
        self.button_hover = "#2A5EA8"
        self.clear_color = "#DF5353"
        self.clear_hover = "#B83A3A"

        # -----------------------------
        # Layout
        # -----------------------------
        self.create_header()
        self.create_chat_area()
        self.create_toolbar()
        self.create_input_area()
        self.create_status_bar()
        self.update_session_timer()
        self.bind_shortcuts()

        # -----------------------------
        # Welcome Experience
        # -----------------------------
        self.display_message("StudyMate", self.get_welcome_text())

    # ============================================================
    # Header
    # ============================================================

    def create_header(self):
        self.header_frame = tk.Frame(self.root, bg=self.primary_color, height=110)
        self.header_frame.pack(fill=tk.X)

        title_container = tk.Frame(self.header_frame, bg=self.primary_color)
        title_container.pack(side=tk.LEFT, padx=24, pady=18)

        title_label = tk.Label(
            title_container,
            text="StudyMate",
            font=self.title_font,
            fg="white",
            bg=self.primary_color
        )
        title_label.pack(anchor=tk.W)

        subtitle_label = tk.Label(
            title_container,
            text="AI Study Assistant · IBM Internship Project",
            font=self.subtitle_font,
            fg="#D7E2F2",
            bg=self.primary_color
        )
        subtitle_label.pack(anchor=tk.W, pady=(6, 0))

        action_container = tk.Frame(self.header_frame, bg=self.primary_color)
        action_container.pack(side=tk.RIGHT, padx=24, pady=18)

        self.about_button = tk.Button(
            action_container,
            text="About",
            bg=self.button_color,
            fg="white",
            activebackground=self.button_hover,
            font=self.header_font,
            relief=tk.FLAT,
            cursor="hand2",
            command=self.show_about
        )
        self.about_button.pack(side=tk.LEFT, padx=6)
        self.about_button.bind("<Enter>", lambda e: self.on_button_hover(self.about_button, self.button_hover))
        self.about_button.bind("<Leave>", lambda e: self.on_button_hover(self.about_button, self.button_color, leave=True))

        self.stats_button = tk.Button(
            action_container,
            text="Statistics",
            bg=self.button_color,
            fg="white",
            activebackground=self.button_hover,
            font=self.header_font,
            relief=tk.FLAT,
            cursor="hand2",
            command=self.show_statistics
        )
        self.stats_button.pack(side=tk.LEFT, padx=6)
        self.stats_button.bind("<Enter>", lambda e: self.on_button_hover(self.stats_button, self.button_hover))
        self.stats_button.bind("<Leave>", lambda e: self.on_button_hover(self.stats_button, self.button_color, leave=True))

        self.export_button = tk.Button(
            action_container,
            text="Export Chat",
            bg=self.button_color,
            fg="white",
            activebackground=self.button_hover,
            font=self.header_font,
            relief=tk.FLAT,
            cursor="hand2",
            command=self.export_chat_history
        )
        self.export_button.pack(side=tk.LEFT, padx=6)
        self.export_button.bind("<Enter>", lambda e: self.on_button_hover(self.export_button, self.button_hover))
        self.export_button.bind("<Leave>", lambda e: self.on_button_hover(self.export_button, self.button_color, leave=True))

    # ============================================================
    # Chat Area
    # ============================================================

    def create_chat_area(self):
        self.chat_frame = tk.Frame(self.root, bg=self.background)
        self.chat_frame.pack(fill=tk.BOTH, expand=True, padx=18, pady=(10, 0))

        self.chat_area = scrolledtext.ScrolledText(
            self.chat_frame,
            wrap=tk.WORD,
            font=self.chat_font,
            bg=self.chat_bg,
            fg=self.text_color,
            insertbackground=self.text_color,
            relief=tk.FLAT,
            borderwidth=0,
            padx=14,
            pady=14,
            state="disabled"
        )
        self.chat_area.pack(fill=tk.BOTH, expand=True)

        self.chat_area.tag_config(
            "sender",
            foreground="#10407A",
            font=("Segoe UI", 10, "bold")
        )
        self.chat_area.tag_config(
            "timestamp",
            foreground="#6A7D9A",
            font=("Segoe UI", 8)
        )
        self.chat_area.tag_config(
            "bot_bubble",
            background="#F2F7FF",
            foreground="#16314A",
            lmargin1=14,
            lmargin2=14,
            rmargin=100,
            spacing1=4,
            spacing3=10,
            font=self.chat_font,
            wrap=tk.WORD
        )
        self.chat_area.tag_config(
            "user_bubble",
            background="#DCE9FF",
            foreground="#16314A",
            lmargin1=100,
            lmargin2=14,
            rmargin=14,
            spacing1=4,
            spacing3=10,
            font=self.chat_font,
            justify=tk.RIGHT,
            wrap=tk.WORD
        )
        self.chat_area.tag_config(
            "typing",
            foreground="#6A7D9A",
            font=("Segoe UI", 10, "italic")
        )

    # ============================================================
    # Toolbar
    # ============================================================

    def create_toolbar(self):
        self.toolbar_frame = tk.Frame(self.root, bg=self.card_bg, height=48)
        self.toolbar_frame.pack(fill=tk.X, padx=18, pady=(8, 0))

        helper_text = (
            "Keyboard: Enter=Send · Ctrl+Enter=Send · Ctrl+S=Export · "
            "Ctrl+A=About · Ctrl+T=Statistics · Esc=Focus Input"
        )

        helper_label = tk.Label(
            self.toolbar_frame,
            text=helper_text,
            font=self.small_font,
            fg="#4D637A",
            bg=self.card_bg
        )
        helper_label.pack(side=tk.LEFT, padx=14, pady=12)

    # ============================================================
    # Input Area
    # ============================================================

    def create_input_area(self):
        self.input_frame = tk.Frame(self.root, bg=self.card_bg, height=90)
        self.input_frame.pack(fill=tk.X, padx=18, pady=(0, 10))

        self.user_input = tk.Entry(
            self.input_frame,
            font=self.input_font,
            bg=self.entry_bg,
            fg=self.text_color,
            insertbackground=self.text_color,
            relief=tk.FLAT,
            width=1,
            bd=1,
            highlightthickness=1,
            highlightbackground="#DCE6F2",
            highlightcolor=self.secondary_color
        )
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(14, 10), pady=14, ipady=10)
        self.user_input.bind("<Return>", self.send_message)

        self.send_button = tk.Button(
            self.input_frame,
            text="Send",
            bg=self.button_color,
            fg="white",
            activebackground=self.button_hover,
            font=self.header_font,
            relief=tk.FLAT,
            cursor="hand2",
            command=self.send_message,
            width=12
        )
        self.send_button.pack(side=tk.LEFT, padx=(0, 8), pady=14)
        self.send_button.bind("<Enter>", self.on_enter_send)
        self.send_button.bind("<Leave>", self.on_leave_send)

        self.clear_button = tk.Button(
            self.input_frame,
            text="Clear",
            bg=self.clear_color,
            fg="white",
            activebackground=self.clear_hover,
            font=self.header_font,
            relief=tk.FLAT,
            cursor="hand2",
            command=self.clear_chat,
            width=12
        )
        self.clear_button.pack(side=tk.LEFT, padx=(0, 14), pady=14)
        self.clear_button.bind("<Enter>", self.on_enter_clear)
        self.clear_button.bind("<Leave>", self.on_leave_clear)

    # ============================================================
    # Display Message
    # ============================================================

    def display_message(self, sender, message):
        """
        Display messages inside the chat area.
        """
        timestamp = get_current_time()
        sender_tag = "user_bubble" if sender == "You" else "bot_bubble"

        self.chat_area.config(state="normal")
        self.chat_area.insert(tk.END, f"{sender}", "sender")
        self.chat_area.insert(tk.END, f" • {timestamp}\n", "timestamp")
        self.chat_area.insert(tk.END, f"{message}\n\n", sender_tag)
        self.chat_area.config(state="disabled")
        self.chat_area.see(tk.END)
        self.set_status("Ready")

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

        self.display_message("You", user_text)
        self.user_input.delete(0, tk.END)
        self.focus_input()

        self.set_status("StudyMate is typing...")
        self.send_button.config(state=tk.DISABLED)

        self.root.after(600, lambda: self.fetch_bot_response(user_text))

    def fetch_bot_response(self, user_text):
        try:
            response = self.bot.get_response(user_text)
        except Exception as error:
            response = f"Error: {error}"

        self.animate_bot_response(response)

    def animate_bot_response(self, response):
        timestamp = get_current_time()
        self.chat_area.config(state="normal")
        self.chat_area.insert(tk.END, "StudyMate", "sender")
        self.chat_area.insert(tk.END, f" • {timestamp}\n", "timestamp")
        self.chat_area.config(state="disabled")
        self._animate_text(response, 0)

    def _animate_text(self, message, index):
        self.chat_area.config(state="normal")

        if index < len(message):
            self.chat_area.insert(tk.END, message[index], "bot_bubble")
            self.chat_area.see(tk.END)
            self.chat_area.config(state="disabled")
            self.root.after(18, lambda: self._animate_text(message, index + 1))
        else:
            self.chat_area.insert(tk.END, "\n\n", "bot_bubble")
            self.chat_area.config(state="disabled")
            self.send_button.config(state=tk.NORMAL)
            self.set_status("Ready")

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
        self.set_status("Chat cleared")

    # ============================================================
    # Button Hover Effects
    # ============================================================

    def on_button_hover(self, button, color, leave=False):
        if leave:
            button.config(bg=self.button_color if button != self.clear_button else self.clear_color)
        else:
            button.config(bg=color)

    def on_enter_send(self, event):
        self.send_button.config(bg=self.button_hover)

    def on_leave_send(self, event):
        self.send_button.config(bg=self.button_color)

    def on_enter_clear(self, event):
        self.clear_button.config(bg=self.clear_hover)

    def on_leave_clear(self, event):
        self.clear_button.config(bg=self.clear_color)

    # ============================================================
    # Shortcuts and focus
    # ============================================================

    def bind_shortcuts(self):
        self.root.bind("<Control-Return>", self.send_message)
        self.root.bind("<Control-s>", lambda event: self.export_chat_history())
        self.root.bind("<Control-a>", lambda event: self.show_about())
        self.root.bind("<Control-t>", lambda event: self.show_statistics())
        self.root.bind("<Escape>", lambda event: self.focus_input())

    def focus_input(self):
        """
        Keeps the cursor inside the input field.
        """
        self.user_input.focus_set()

    # ============================================================
    # About, Statistics and Export
    # ============================================================

    def show_about(self):
        """
        Displays the About dialog.
        """
        messagebox.showinfo("About StudyMate", about_project())
        self.set_status("About dialog opened")

    def show_statistics(self):
        """
        Displays chat statistics.
        """
        stats = get_chat_statistics()
        message = (
            f"Total Messages : {stats['messages']}\n"
            f"Student Messages : {stats['user_messages']}\n"
            f"Bot Replies : {stats['bot_messages']}"
        )
        messagebox.showinfo("StudyMate Statistics", message)
        self.set_status("Statistics displayed")

    def export_chat_history(self):
        """
        Exports the current chat history.
        """
        result = export_chat()
        if result:
            messagebox.showinfo("Export Chat", "Chat history exported successfully.")
            self.set_status("Chat exported")
        else:
            messagebox.showwarning("Export Chat", "No chat history found to export.")
            self.set_status("Export failed")

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
            text=f"{app_version()} · Ready · Session {get_session_duration()}",
            bd=1,
            relief=tk.FLAT,
            anchor=tk.W,
            font=self.small_font,
            bg="#FFFFFF",
            fg="#4D637A",
            padx=12,
            pady=8
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def set_status(self, text):
        """
        Updates the status bar text.
        """
        if hasattr(self, "status_bar"):
            self.status_bar.config(text=f"{app_version()} · {text} · Session {get_session_duration()}")

    def update_session_timer(self):
        """
        Refreshes the session duration in the footer each second.
        """
        if hasattr(self, "status_bar"):
            current_text = self.status_bar.cget("text")
            parts = current_text.split(" · ")
            status_text = parts[1] if len(parts) > 1 else "Ready"
            self.status_bar.config(text=f"{app_version()} · {status_text} · Session {get_session_duration()}")
        self.root.after(1000, self.update_session_timer)

    def get_welcome_text(self):
        """
        Returns polished welcome text for the initial message.
        """
        return (
            "Welcome to StudyMate! 👋\n\n"
            "Your AI-powered study assistant is ready to help you learn faster.\n\n"
            "Try one of these prompts:\n"
            "- What is Python?\n"
            "- Give me a study tip\n"
            "- Convert 85 to CGPA\n"
            "- Tell me a motivational quote\n"
            "- Help\n\n"
            "Type your question below and press Enter to begin."
        )

    # ============================================================
    # Run Application
    # ============================================================

    def run(self):
        """
        Starts the GUI application.
        """
        self.focus_input()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
