import tkinter as tk
import random
import sys
import subprocess
import os
import time

# ---------- Key for unlocking ----------
SECRET_KEY = "1234"

# ---------- RESTART SYSTEM ----------
def restart_program():
    python = sys.executable
    subprocess.Popen([python] + sys.argv)
    os._exit(0)

# ---------- Random ass glitches no one asked for :sob: ----------
def glitch_text(text):
    chars = "!@#$%^&*()_+-=[]{}|;:,.<>?/"
    return "".join(
        c if random.random() > 0.25 else random.choice(chars)
        for c in text
    )


# ---------- APP ----------
class App:
    def __init__(self):
        self.success = False
        self.ready = False

        self.root = tk.Tk()
        self.root.title("terminal")

        self.root.attributes("-fullscreen", True)
        self.root.attributes("-topmost", True)

        self.root.configure(bg="black")

        self.build_ui()
        self.bind_keys()


        self.root.after(2000, self.enable_focus_watch)

        self.root.mainloop()

    # ---------- UI ----------
    def build_ui(self):
        frame = tk.Frame(self.root, bg="black")
        frame.pack(expand=True)

        tk.Label(
            frame,
            text="Fsociety > Terminal",
            font=("Courier", 26, "bold"),
            fg="#00ff9d",
            bg="black"
        ).pack(pady=20)

        tk.Label(
            frame,
            text="system console",
            font=("Courier", 12),
            fg="#555",
            bg="black"
        ).pack()

        self.entry = tk.Entry(
            frame,
            font=("Courier", 16),
            justify="center",
            bg="#111",
            fg="#00ff9d",
            insertbackground="#00ff9d",
            relief="flat",
            width=25
        )
        self.entry.pack(pady=20, ipady=6)

        self.status = tk.Label(
            frame,
            text="",
            font=("Courier", 14),
            fg="red",
            bg="black"
        )
        self.status.pack()

        tk.Button(
            frame,
            text="Submit",
            command=self.check_key,
            font=("Courier", 14),
            fg="#00ff9d",
            bg="black",
            relief="flat",
            activebackground="black",
            activeforeground="white"
        ).pack(pady=10)

    # ---------- KEY CHECK ----------
    def check_key(self):
        if self.entry.get() == SECRET_KEY:
            self.success = True
            self.status.config(text=glitch_text("ACCESS GRANTED"))
            self.root.after(800, self.root.destroy)
        else:
            self.status.config(text="WRONG KEY")

    # ---------- FOCUS SYSTEM ----------
    def enable_focus_watch(self):
        self.ready = True
        self.watch_focus()

    def watch_focus(self):

        if not self.ready or self.success:
            return

        if self.root.focus_displayof() is None:
            self.status.config(text=glitch_text("FOCUS LOST... REBOOTING"))
            self.root.after(1200, restart_program)
            return

        self.root.after(300, self.watch_focus)

    # ---------- KEYS ----------
    def bind_keys(self):
        self.root.bind("<Return>", lambda e: self.check_key())
        self.root.bind("<Escape>", lambda e: restart_program())
        self.root.protocol("WM_DELETE_WINDOW", restart_program)


# ---------- RUN ----------
if __name__ == "__main__":
    App()
