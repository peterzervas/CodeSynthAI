# Python script to draw 50 random Rhombus shapes using Turtle and Random library
import turtle
import random

turtle.speed(0)

turtle.bgcolor('black')

for _ in range(50):
    size = random.randint(50, 200)
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(random.random(), random.random(), random.random())
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(size)
        turtle.right(45)
        turtle.forward(size)
        turtle.right(135)
    turtle.end_fill()

turtle.done()
