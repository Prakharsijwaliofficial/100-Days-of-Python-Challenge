from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

food = Food()
snake = Snake()
screen = Screen()
scoreboard = Scoreboard()  

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("JSS Snake Game")
screen.tracer(0)
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()  
        # snake.extend() # Uncomment this if your Snake class has an extend method!

    # FIXED: Added the minus sign to the left X boundary check (-280)
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detech collision with tail.
    for segment in snake.segments[1:]:
        
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
