import turtle

# Function to draw the Koch curve snowflake using recursion
def koch_curve_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve_snowflake(t, order-1, size/3)
            t.left(angle)

# Set up the turtle
t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-150, 90)
t.pendown()

# Draw the snowflake
for i in range(3):
    koch_curve_snowflake(t, 4, 300)
    t.right(120)

t.hideturtle()
turtle.done()