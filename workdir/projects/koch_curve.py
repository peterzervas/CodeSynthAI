import turtle

# Function to create the koch curve
def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order-1, size/3)
            t.left(angle)

# Set up the turtle
t = turtle.Turtle()
t.speed(0)
t.color('white')
t.screen.bgcolor('blue')

# Move the turtle to starting position
t.penup()
t.goto(-150, 90)
t.pendown()

# Draw the koch curve snowflake shape
for i in range(3):
    koch_curve(t, 4, 300)
    t.right(120)

t.hideturtle()
turtle.done()