import tkinter as tk
from tkinter import messagebox

class PersonalityTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Which Engineer Are You?")
        self.root.geometry("600x400")
        self.root.configure(bg="#FFD700")

        # Title
        self.title_label = tk.Label(root, text="Find Out Which Engineer You Are!", font=("Comic Sans MS", 20, "bold"), bg="#FFD700", fg="#FF4500")
        self.title_label.pack(pady=20)

        # Questions
        self.questions = [
            "What do you prefer?",
            "Choose your favorite tool:",
            "How do you solve problems?",
            "What excites you the most?"
        ]

        self.options = [
            ["Building things", "Designing", "Coding", "Analyzing data"],
            ["Hammer", "Blueprint", "Laptop", "Calculator"],
            ["Hands-on approach", "Strategizing", "Debugging", "Theoretical analysis"],
            ["Robots", "Bridges", "Algorithms", "Heat engines"]
        ]

        self.answers = []
        self.current_question = 0

        self.question_label = tk.Label(root, text=self.questions[self.current_question], font=("Comic Sans MS", 16), bg="#FFD700", fg="#008B8B")
        self.question_label.pack(pady=10)

        self.option_buttons = []
        for option in self.options[self.current_question]:
            button = tk.Button(root, text=option, font=("Comic Sans MS", 14), bg="#FF7F50", fg="white", width=25, command=lambda opt=option: self.next_question(opt))
            button.pack(pady=5)
            self.option_buttons.append(button)

    def next_question(self, answer):
        self.answers.append(answer)
        self.current_question += 1

        if self.current_question < len(self.questions):
            self.update_question()
        else:
            self.show_result()

    def update_question(self):
        self.question_label.config(text=self.questions[self.current_question])

        for i, button in enumerate(self.option_buttons):
            button.config(text=self.options[self.current_question][i])

    def show_result(self):
        personality_type = self.calculate_personality_type()
        result_message = f"You are a {personality_type} Engineer!"
        messagebox.showinfo("Result", result_message)
        self.root.quit()

    def calculate_personality_type(self):
        # Simple logic to determine personality type based on answers
        if "Building things" in self.answers or "Hammer" in self.answers:
            return "Mechanical"
        elif "Designing" in self.answers or "Blueprint" in self.answers:
            return "Civil"
        elif "Coding" in self.answers or "Laptop" in self.answers:
            return "Software"
        elif "Analyzing data" in self.answers or "Calculator" in self.answers:
            return "Data"

if __name__ == "__main__":
    root = tk.Tk()
    app = PersonalityTestApp(root)
    root.mainloop()
