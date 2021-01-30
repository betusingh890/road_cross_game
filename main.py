import turtle
from bloks import Block
from car import Car
from math import sqrt
import sys
import os

display = turtle.Screen()
display.setup(width=800, height=600)
display.colormode(255)
display.bgcolor("black")
display.title("car cross game")
display.tracer(0)
car = Car()
pen = turtle.Turtle()
pen.color("white")
pen.hideturtle()
pen.penup()
pen.left(90)
pen.forward(240)
blocks = []
for i in range(18):
    new_block = Block()
    blocks.append(new_block)
score = 0
increase_speed = False
status = True
block_speed = 0.5


def distance(x, y, x2, y2):
    doori = sqrt((x - x2) ** 2 + (y - y2) ** 2)
    return doori


def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, *sys.argv)


with open("my_scores.json", "r") as file:
    content = file.read()
    high_score = int(content)

while status:
    display.listen()
    display.onkey(key="Up", fun=car.car_forward)
    display.onkey(key="Down", fun=car.car_backward)
    display.onkey(key="Right", fun=car.car_right)
    display.onkey(key="Left", fun=car.car_left)
    car.set_car()
    for block in blocks:
        block.dynamics(block_speed)

    if car.Ycor() > 280:
        score += 10
        pen.clear()
        car.car_Y = -280
        car.set_car()
        increase_speed = True
    if increase_speed:
        increase_speed = False
        block_speed += 0.2

    pen.write(f"score: {score} High score: {high_score} ", font=("Arial", 20, "normal"))
    for block in blocks:
        x = block.Xcor()
        y = block.Ycor()
        if distance(x, y, car.Xcor(), car.Ycor()) < 20:
            response = turtle.textinput("you lost", "you collided with a block, enter yes to play again").lower()
            if response == "yes":
                if score > int(high_score):
                    with open("my_scores.json", "w") as file:
                        file.write(str(score))
                restart_program()
            else:
                if score > int(high_score):
                    with open("my_scores.json", "w") as file:
                        file.write(str(score))
                sys.exit()

    display.update()

display.exitonclick()
