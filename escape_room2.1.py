import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class EscapeRoomGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Funny Escape Room Game")
        self.root.geometry("800x600")
        self.root.configure(bg="#ADD8E6")
        
        self.questions = [
            "What has keys but can't open locks?",
            "I’m tall when I’m young, and I’m short when I’m old. What am I?",
            "What is full of holes but still holds water?",
            "What can travel around the world while staying in a corner?"
        ]
        
        self.answers = ["piano", "candle", "sponge", "stamp"]
        self.user_answers = []
        self.current_question = 0
        self.game_over = False

        # Title
        self.title_label = tk.Label(root, text="Can You Escape?", font=("Comic Sans MS", 24, "bold"), bg="#ADD8E6", fg="#FF4500")
        self.title_label.pack(pady=20)

        # Progress Display
        self.progress_label = tk.Label(root, text="Just started...", font=("Comic Sans MS", 18), bg="#ADD8E6", fg="#008B8B")
        self.progress_label.pack(pady=10)

        # Question
        self.question_label = tk.Label(root, text=self.questions[self.current_question], font=("Comic Sans MS", 18), bg="#ADD8E6", fg="#00008B", wraplength=700)
        self.question_label.pack(pady=20)

        # Answer Entry
        self.answer_entry = tk.Entry(root, font=("Comic Sans MS", 16), width=30)
        self.answer_entry.pack(pady=20)

        # Submit Button
        self.submit_button = tk.Button(root, text="Submit Answer", font=("Comic Sans MS", 16), bg="#FF7F50", fg="white", command=self.check_answer)
        self.submit_button.pack(pady=20)

    def check_answer(self):
        user_answer = self.answer_entry.get().strip().lower()
        self.user_answers.append(user_answer)

        if user_answer == self.answers[self.current_question]:
            self.update_progress("Just about to escape!")
        else:
            self.update_progress("Not escaped yet...")

        self.current_question += 1
        if self.current_question < len(self.questions):
            self.update_question()
        else:
            self.end_game()

    def update_question(self):
        self.question_label.config(text=self.questions[self.current_question])
        self.answer_entry.delete(0, tk.END)

    def update_progress(self, progress_text):
        self.progress_label.config(text=progress_text)

    def end_game(self):
        if self.user_answers == self.answers:
            self.show_victory_animation()
        else:
            self.show_horror_scene()

    def show_victory_animation(self):
        self.root.withdraw()
        victory_window = tk.Toplevel(self.root)
        victory_window.geometry("800x600")
        victory_window.title("You Escaped!")

        # Load and display a funny victory image
        img = Image.open("victory.jpg")  # You need to have an image named 'victory.jpg'
        img = img.resize((800, 600), Image.ANTIALIAS)
        victory_img = ImageTk.PhotoImage(img)
        victory_label = tk.Label(victory_window, image=victory_img)
        victory_label.image = victory_img  # Keep a reference to avoid garbage collection
        victory_label.pack()

        victory_message = tk.Label(victory_window, text="You Escaped! Congratulations!", font=("Comic Sans MS", 24), fg="#32CD32")
        victory_message.pack(pady=20)

        # Closing after some time with a funny message
        victory_window.after(3000, lambda: self.close_game(victory_window))

    def show_horror_scene(self):
        self.root.withdraw()
        horror_window = tk.Toplevel(self.root)
        horror_window.attributes('-fullscreen', True)
        horror_window.configure(bg="black")

        # Load and display a horror image
        img = Image.open("horror.jpg")  # You need to have an image named 'horror.jpg'
        img = img.resize((horror_window.winfo_screenwidth(), horror_window.winfo_screenheight()))
        horror_img = ImageTk.PhotoImage(img)
        horror_label = tk.Label(horror_window, image=horror_img)
        horror_label.image = horror_img  # Keep a reference to avoid garbage collection
        horror_label.pack()

        horror_message = tk.Label(horror_window, text="You Failed to Escape...", font=("Comic Sans MS", 36, "bold"), fg="red", bg="black")
        horror_message.pack(pady=50)

        # Play a scary sound or show something creepy
        horror_window.after(5000, lambda: self.close_game(horror_window))

    def close_game(self, window):
        window.destroy()
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = EscapeRoomGame(root)
    root.mainloop()
