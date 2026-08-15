from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(
            padx=20,
            pady=20,
            bg=THEME_COLOR
        )

        # ---------------- SCORE ---------------- #

        self.score_label = Label(
            text="Score: 0",
            fg="white",
            bg=THEME_COLOR
        )
        self.score_label.grid(row=0, column=1)

        # ---------------- CANVAS ---------------- #

        self.canvas = Canvas(
            self.window,
            width=300,
            height=250
        )

        self.canvas_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )

        self.canvas.grid(
            column=0,
            row=1,
            columnspan=2,
            pady=50
        )

        # ---------------- BUTTON IMAGES ---------------- #

        self.right_button_image = PhotoImage(
            file="images/true.png"
        )

        self.wrong_button_image = PhotoImage(
            file="images/false.png"
        )

        # ---------------- BUTTONS ---------------- #

        self.right_button = Button(
            image=self.right_button_image,
            highlightthickness=0,
            command=self.true_pressed
        )
        self.right_button.grid(
            column=0,
            row=2
        )

        self.wrong_button = Button(
            image=self.wrong_button_image,
            highlightthickness=0,
            command=self.false_pressed
        )
        self.wrong_button.grid(
            column=1,
            row=2
        )

        # ---------------- FIRST QUESTION ---------------- #

        self.get_next_question()

        self.window.mainloop()

    # ---------------- GET NEXT QUESTION ---------------- #

    def get_next_question(self):
        self.canvas.config(bg="white")

        q_text = self.quiz.next_question()

        self.canvas.itemconfig(
            self.canvas_text,
            text=q_text
        )

    # ---------------- TRUE BUTTON ---------------- #

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    # ---------------- FALSE BUTTON ---------------- #

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    # ---------------- FEEDBACK ---------------- #

    def give_feedback(self, is_right):

        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        # Update score
        self.score_label.config(
            text=f"Score: {self.quiz.score}"
        )

        self.window.after(
            1000,
            self.get_next_question
        )