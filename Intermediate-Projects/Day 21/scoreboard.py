from turtle import Turtle

# Define the constants at the top so the class can use them
ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")     
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.current_score = 0  
        self.update_text()

    def update_text(self):
        self.clear()            
        self.write(f"Score = {self.current_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.current_score += 1 
        self.update_text()      
    
    def game_over(self):
        self.goto(0, 0)
        # Fixed: Now using the defined constants
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
