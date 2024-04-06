import turtle

class Enemy(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.speed(0)
        self.goto(0, 250)
        self.speed = 2
        self.direction = 1

    def move(self):
        x = self.xcor()
        x += self.speed * self.direction
        self.setx(x)

        # Check for hitting the edge and reverse direction
        if self.xcor() > 280 or self.xcor() < -280:
            self.reverse_direction()

    def reverse_direction(self):
        self.direction *= -1
        y = self.ycor()
        y -= 20
        self.sety(y)

    def is_collision(self, other):
        return self.distance(other) < 20

    def reset_position(self):
        self.goto(0, 250)
