# Random Walk Simulation

import turtle
import random

# Create five turtles and put them into a Python List
num_turtles = 5
turtles = []
for _ in range(num_turtles):
    new_turtle = turtle.Turtle()
    turtles.append(new_turtle)

# Define the constant number of steps for each turtle to move forward
step_size = 20

# Main simulation loop
for _ in range(100):
    for t in turtles:
        t.left(random.randint(0, 360))
        t.forward(step_size)

import turtle
import random

# Create five turtles
turtles = []
for _ in range(5):
    new_turtle = turtle.Turtle()
    turtles.append(new_turtle)

# Set up the screen
screen = turtle.Screen()
screen.title("Random Walk Simulation")
screen.setup(width=600, height=600)

# Simulate random walk for 100 iterations
for _ in range(100):
    for current_turtle in turtles:
        # Move the turtle forward by 20 units
        current_turtle.forward(20)
        # Turn the turtle in a random direction (0-360 degrees)
        current_turtle.right(random.randint(0, 360))

# Keep the window open
turtle.done()
