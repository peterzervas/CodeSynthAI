# Python Turtle Chess Board Project

import turtle

def draw_chess_board(board_size):
    '''Draws a chess board of the given size using Python Turtle'''    
    screen = turtle.Screen()
    screen.title('Turtle Chess Board')
    screen.setup(600, 600)

    for row in range(board_size):
        for col in range(board_size):
            if (row + col) % 2 == 0:
                color = 'white'
            else:
                color = 'black'
            turtle.begin_fill()
            turtle.fillcolor(color)
            turtle.penup()
            turtle.goto((col - board_size/2) * 50, (board_size/2 - row) * 50)
            turtle.pendown()
            for _ in range(4):
                turtle.forward(50)
                turtle.right(90)
            turtle.end_fill()

    turtle.done()

# Main code
if __name__ == '__main__':
    board_size = 8
    draw_chess_board(board_size)