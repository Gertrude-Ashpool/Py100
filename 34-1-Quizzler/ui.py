from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")

        self.window.config(padx=20, pady=20)
        self.window.config(bg=THEME_COLOR)

        # Score Label
        self.score_label = Label(text="Score: 0", fg="white", background=THEME_COLOR, font=("Arial", 16, "normal"))
        self.score_label.grid(row=0, column=1)

        # Question Canvas
        self.canvas = Canvas(width=300, height=250, highlightthickness=0, background='white')
        self.question_text = (
            self.canvas.create_text(
                150, 125,
                width=270,
                text="Question goes here. And you will answer...",
                fill=THEME_COLOR,
                font=('Arial', 20, 'italic')
            )
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)

        # Check Button
        check_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=check_image, highlightthickness=0, command=self.respond_true)
        self.true_button.grid(row=2, column=0)

        # X Button
        cross_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=cross_image, highlightthickness=0, command=self.respond_false)
        self.false_button.grid(row=2, column=1)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(background="White")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def respond_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def respond_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background="Lime")
        else:
            self.canvas.config(background="Tomato")
        self.window.after(1000, self.next_question)





# self.canvas.itemconfig(self.question_text, text="{q_text}")
