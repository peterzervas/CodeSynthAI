import turtle

class Bullet(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('triangle')
        self.color('yellow')
        self.penup()
        self.speed(0)
        self.hideturtle()
        self.setheading(90)
        self.state = 'ready'
        self.speed = 20

    def fire(self):
        if self.state == 'ready':
            self.state = 'fire'
            self.showturtle()
            x = player.xcor()
            y = player.ycor() + 10
            self.setposition(x, y)

    def move(self):
        if self.state == 'fire':
            y = self.ycor()
            y += self.speed
            self.sety(y)

            # Check if bullet has gone off the screen
            if y > 275:
                self.reset()

    def reset(self):
        self.hideturtle()
        self.state = 'ready'

    def is_collision(self, other):
        return self.distance(other) < 20
