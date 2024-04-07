
import turtle

def draw_line(x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)

def draw_penrose_triangle():
    # Starting points for the Penrose triangle
    points = [(0, -100), (86.6, 50), (-86.6, 50)]
    
    turtle.speed(0)
    turtle.hideturtle()
    
    # Draw the outer triangle
    for i in range(3):
        draw_line(*points[i], *points[(i+1)%3])
    
    # Inner details for the Penrose triangle illusion
    inner_points = [(43.3, -25), (0, 50), (-43.3, -25)]
    for i in range(3):
        draw_line(*points[i], *inner_points[i])
        draw_line(*inner_points[i], *points[(i+2)%3])
    
    turtle.done()

def main():
    draw_penrose_triangle()

if __name__ == "__main__":
    main()
