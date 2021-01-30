import turtle
import random


class Block(turtle.Turtle):
    def __init__(self):
        super(Block, self).__init__
        self.block = turtle.Turtle()
        self.block_X = random.randint(-380, 380)
        self.block_Y = random.randint(-250, 280)
        self.block.shape("square")
        self.block.penup()
        self.color = self.color_maker()
        self.block.color(self.color)
        self.dynamics()

    def color_maker(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = (r, g, b)
        return color

    def dynamics(self, speed_X = 0.5):
        self.speed_X = speed_X
        self.block_X -= self.speed_X
        self.block.goto(x=self.block_X, y=self.block_Y)
        if self.block_X < -400:
            self.block_X = 400
            self.block_Y = random.randint(-250, 280)
    def Xcor(self):
        return self.block_X
    def Ycor(self):
        return self.block_Y
