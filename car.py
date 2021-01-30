import turtle


class Car(turtle.Turtle):
    def __init__(self):
        super(Car, self).__init__
        self.car = turtle.Turtle()
        self.car.color("white")
        self.car.shape("turtle")
        self.car.penup()
        self.car.left(90)
        self.car_X = 0
        self.car_Y = -280

    def car_forward(self):
        self.car_Y += 10

    def car_backward(self):
        self.car_Y -= 10

    def car_right(self):
        self.car_X += 4

    def car_left(self):
        self.car_X -= 4

    def set_car(self):
        self.car.goto(self.car_X, self.car_Y)

    def Ycor(self):
        return self.car.ycor()

    def Xcor(self):
        return self.car.xcor()
