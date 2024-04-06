import turtle

class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('blue')
        self.penup()
        self.speed(0)
        self.setposition(0, -250)
        self.setheading(90)
        self.speed = 15

    def go_left(self):
        x = self.xcor()
        x -= self.speed
        if x < -280:
            x = -280
        self.setx(x)

    def go_right(self):
        x = self.xcor()
        x += self.speed
        if x > 280:
            x = 280
        self.setx(x)
