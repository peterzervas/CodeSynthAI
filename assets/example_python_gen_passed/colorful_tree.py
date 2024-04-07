import turtle
import colorsys


def draw_tree(branch_length, angle, depth):
    if depth == 0:
        return
    turtle.forward(branch_length)
    turtle.right(angle)
    draw_tree(branch_length - 10, angle, depth - 1)
    turtle.left(2 * angle)
    draw_tree(branch_length - 10, angle, depth - 1)
    turtle.right(angle)
    turtle.backward(branch_length)


def main():
    turtle.setup(width=800, height=600)
    turtle.speed(0)
    turtle.bgcolor('black')
    turtle.color('white')
    turtle.left(90)
    turtle.up()
    turtle.backward(100)
    turtle.down()
    draw_tree(100, 30, 10)
    turtle.exitonclick()


if __name__ == '__main__':
    main()
