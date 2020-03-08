import turtle

window = turtle.Screen()
window.bgcolor('light green')

turtle = turtle.Turtle()
turtle.pensize(3)
turtle.pencolor('blue')

N = 4

side = 20

x = -10
y = -10


def drawSquares():
    global x, y, side
    for i in range(N):
        point = (x, y)
        turtle.penup()
        turtle.goto(point)
        turtle.pendown()
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)
        x = x - 10
        y = y - 10
        side = side + 20


def main():
    drawSquares()


if __name__ == '__main__':
    main()

window.exitonclick()
