import tkinter as tk
from tkinter import messagebox
import time

class EscapeRoomGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Escape Room")
        self.root.geometry("500x500")
        self.time_start = time.time()

        self.timer_label = tk.Label(self.root, text="Time: 0", font=("Arial", 16))
        self.timer_label.pack(pady=20)

        self.question_label = tk.Label(self.root, text="Solve the riddle to escape!", font=("Arial", 18))
        self.question_label.pack(pady=20)

        self.riddle = tk.Label(self.root, text="I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?", font=("Arial", 14), wraplength=400)
        self.riddle.pack(pady=20)

        self.answer_entry = tk.Entry(self.root, font=("Arial", 14))
        self.answer_entry.pack(pady=20)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer, font=("Arial", 14))
        self.submit_button.pack(pady=20)

        self.message_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.message_label.pack(pady=20)

        self.timer_running = True
        self.update_timer()

    def update_timer(self):
        if self.timer_running:
            elapsed_time = int(time.time() - self.time_start)
            self.timer_label.config(text=f"Time: {elapsed_time} seconds")
            self.root.after(1000, self.update_timer)

    def check_answer(self):
        answer = self.answer_entry.get().strip().lower()
        if answer == "echo":
            self.timer_running = False
            elapsed_time = int(time.time() - self.time_start)
            self.message_label.config(text=f"Congratulations! You've escaped in {elapsed_time} seconds!", fg="green")
            messagebox.showinfo("Escaped!", f"Well done! You've escaped in {elapsed_time} seconds!")
            self.root.quit()
        else:
            self.message_label.config(text="Wrong answer! Try again.", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    game = EscapeRoomGame(root)
    root.mainloop()
