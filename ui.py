from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
CORRECT_COLOR = "#11EC64"
WRONG_COLOR = "#FF6A4C"
FONT_NAME = "Courier"


class QuizzUI:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)

        false_image = PhotoImage(file="images/false.png")
        true_image = PhotoImage(file="images/true.png")

        self.score_label = Label(font=(FONT_NAME, 30, "bold"), bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        self.set_score()
        self.canvas = Canvas(
            width=600,
            height=400,
            bg="white",
            highlightthickness=0
        )

        self.canvas_text = self.canvas.create_text(300,
                                                   200,
                                                   width=450,
                                                   fill=THEME_COLOR,
                                                   font=("Ariel", 20, "italic"))

        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_button = Button(image=true_image, command=self.true_button_call)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=false_image, command=self.false_button_call)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.canvas_text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.canvas_text, text="You have reached the end of the quizz!")
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")

    def check_user_answer(self, answer):
        if self.quiz.check_answer(answer):
            self.set_score()
            self.canvas.config(bg=CORRECT_COLOR)
        else:
            self.canvas.config(bg=WRONG_COLOR)
        self.window.after(2000, self.get_next_question)

    def set_score(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def true_button_call(self):
        self.check_user_answer(True)

    def false_button_call(self):
        self.check_user_answer(False)
