THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.root = Tk()
        self.root.config(bg=THEME_COLOR, padx=20, pady=20)
        self.root.title("Quizzler")

        self.score_label = Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1, padx=20, pady=20)

        self.canvas = Canvas(width=350, height=250)
        self.text_q = self.canvas.create_text(
            175,
            125,
            text="",
            width=280,
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
            )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.false = PhotoImage(file="images/false.png")
        self.true = PhotoImage(file="images/true.png")

        self.true_button = Button(image=self.true, highlightthickness=0, command=self.true_p)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=self.false, highlightthickness=0, command=self.false_p)
        self.false_button.grid(row=2, column=1)

        self.next_question()

        self.root.mainloop()

    def next_question(self):
        question = self.quiz.next_question()
        self.canvas.itemconfig(self.text_q, text=question)

    def true_p(self):
        if self.quiz.check_answer("True") == True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.root.after(1000, self.move)

    def false_p(self):
        if self.quiz.check_answer("True") == True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.root.after(1000, self.move)

    def move(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.text_q)
            message = f"You've completed the quiz\nYour final score was: {self.quiz.score}/{self.quiz.question_number}"
            self.canvas.itemconfig(self.text_q, text=message)
