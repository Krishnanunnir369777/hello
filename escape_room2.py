import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import time
import random

class DigitalEscapeRoom:
    def __init__(self, root):
        self.root = root
        self.root.title("Escape the Room!")
        self.root.geometry("800x600")
        self.root.configure(bg="#2E4053")

        self.current_question = 0
        self.progress = 0

        # Question Data
        self.questions = [
            "I speak without a mouth and hear without ears. What am I?",
            "The more of this there is, the less you see. What is it?",
            "I have keys but no locks. I have a space but no room. What am I?",
            "What can travel around the world while staying in a corner?"
        ]
        self.answers = ["echo", "darkness", "keyboard", "stamp"]

        # UI Elements
        self.create_ui()

    def create_ui(self):
        self.title_label = tk.Label(self.root, text="Can You Escape?", font=("Helvetica", 24, "bold"), bg="#2E4053", fg="#F7DC6F")
        self.title_label.pack(pady=20)

        self.question_label = tk.Label(self.root, text=self.questions[self.current_question], font=("Helvetica", 16), bg="#2E4053", fg="#F7DC6F", wraplength=700)
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(self.root, font=("Helvetica", 14), width=40)
        self.answer_entry.pack(pady=20)

        self.submit_button = tk.Button(self.root, text="Submit Answer", font=("Helvetica", 14), bg="#117A65", fg="white", command=self.check_answer)
        self.submit_button.pack(pady=20)

        self.feedback_label = tk.Label(self.root, text="Progress: 0%", font=("Helvetica", 14), bg="#2E4053", fg="#F7DC6F")
        self.feedback_label.pack(pady=20)

        self.hint_label = tk.Label(self.root, text="", font=("Helvetica", 12, "italic"), bg="#2E4053", fg="#EC7063")
        self.hint_label.pack(pady=10)

    def check_answer(self):
        user_answer = self.answer_entry.get().strip().lower()
        if user_answer == self.answers[self.current_question]:
            self.progress += 25
            self.feedback_label.config(text=f"Progress: {self.progress}%")
            self.current_question += 1
            if self.current_question < len(self.questions):
                self.update_question()
            else:
                self.show_escape_animation()
        else:
            self.show_horror_scene()

    def update_question(self):
        self.question_label.config(text=self.questions[self.current_question])
        self.answer_entry.delete(0, tk.END)
        self.hint_label.config(text=f"Hint: {self.get_hint()}")

    def get_hint(self):
        hints = {
            0: "I am a sound that repeats.",
            1: "It makes night more mysterious.",
            2: "You type on me every day.",
            3: "I can go on a letter."
        }
        return hints.get(self.current_question, "")

    def show_escape_animation(self):
        self.title_label.config(text="Congratulations! You've Escaped!", fg="#28B463")
        self.question_label.config(text="You're free now! Run before the door closes!", fg="#28B463")
        self.answer_entry.pack_forget()
        self.submit_button.pack_forget()
        self.feedback_label.pack_forget()
        self.hint_label.pack_forget()

        for i in range(10):
            self.root.update_idletasks()
            self.title_label.config(font=("Helvetica", 24, "bold", "italic"), fg=self.random_color())
            time.sleep(0.2)

        messagebox.showinfo("Escaped!", "You successfully escaped the room!")
        self.root.quit()

    def show_horror_scene(self):
        horror_image = Image.open("horror.jpg")  # Replace with your horror image path
        horror_photo = ImageTk.PhotoImage(horror_image)
        self.hint_label.config(image=horror_photo)
        self.hint_label.image = horror_photo
        self.root.update_idletasks()
        time.sleep(3)
        messagebox.showwarning("Oh No!", "You didn't escape... The room is closing in!")
        self.root.quit()

    def random_color(self):
        return f'#{random.randint(0, 0xFFFFFF):06x}'

if __name__ == "__main__":
    root = tk.Tk()
    app = DigitalEscapeRoom(root)
    root.mainloop()
