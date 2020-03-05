import turtle

window = turtle.Screen()
window.bgcolor('light green')

triangle = turtle.Turtle()
triangle.color("blue")
triangle.pensize(3)

for i in range(3):
    triangle.forward(50)
    leftTurn = 360 / 3
    triangle.left(leftTurn)

for i in range(4):
    triangle.forward(50)
    leftTurn = 360 / 4
    triangle.left(leftTurn)

for i in range(6):
    triangle.forward(50)
    leftTurn = 360 / 6
    triangle.left(leftTurn)

for i in range(8):
    triangle.forward(50)
    leftTurn = 360 / 8
    triangle.left(leftTurn)

triangle.hideturtle()
window.exitonclick()
