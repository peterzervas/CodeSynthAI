# Code for drawing a colored tree with recursion using lines# Function to draw a colored tree with recursion using lines

import turtle

def draw_tree(branch_length, color):
    if branch_length > 5:
        turtle.pencolor(color)
        turtle.forward(branch_length)
        turtle.right(20)
        draw_tree(branch_length - 15, color)
        turtle.left(40)
        draw_tree(branch_length - 15, color)
        turtle.right(20)
        turtle.backward(branch_length)


turtle.speed(0)
turtle.bgcolor('black')
turtle.left(90)
turtle.up()
turtle.backward(100)
turtle.down()
draw_tree(75, 'green')
turtle.done()
