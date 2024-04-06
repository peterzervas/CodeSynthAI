import turtle

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score}', align='center', font=('Courier', 24, 'normal'))

    def increase_score(self):
        self.score += 10
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER', align='center', font=('Courier', 40, 'normal'))
