
import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("blue")
t.color("white")
t.penup()
t.goto(-150, 90)
t.pendown()

for i in range(3):
    koch_snowflake(t, 4, 300)
    t.right(120)

turtle.done()
