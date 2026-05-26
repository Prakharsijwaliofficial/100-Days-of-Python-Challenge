from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)
def right():
    tim.right(20)
def left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
def backward():
    tim.backward(10)
def clear():
    tim.clear
    tim.penup()
    tim.home()
screen.listen()
screen.onkey(key = "d", fun = right)
screen.onkey(key = "w", fun = move_forward)
screen.onkey(key = "a", fun = left)
screen.onkey(key = "s", fun = backward)
screen.exitonclick()
