from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0

        # Move to top-left corner
        self.goto(-280, 260)

        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-280, 260)   # Go back before writing
        self.write(
            f"Score: {self.score}",
            align="left",
            font=("Arial", 18, "normal")
        )

    def game_over(self):
        self.goto(0, 0)        # Center of the screen
        self.write(
            "GAME OVER",
            align="center",
            font=("Arial", 24, "bold")
        )

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset_board(self):
        self.score = 0         # Use = not ==
        self.update_score()
