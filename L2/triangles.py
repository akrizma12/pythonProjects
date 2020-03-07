import turtle

window = turtle.Screen()
window.bgcolor('light green')

len1 = 200
x = -100
y = - 87

turtle = turtle.Turtle()
turtle.color("blue")
turtle.pensize(3)
turtle.penup()
turtle.goto(x, y)
turtle.pendown()

turtle.forward(len1)
turtle.left(120)
turtle.forward(len1)
turtle.left(120)
turtle.forward(len1)
turtle.left(120)

len2 = 100

turtle.forward(len2)
turtle.left(60)
turtle.forward(len2)
turtle.left(120)
turtle.forward(len2)
turtle.left(120)
turtle.forward(len2)

window.exitonclick()