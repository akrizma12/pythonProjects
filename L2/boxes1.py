import turtle

window = turtle.Screen()
window.bgcolor('light green')

len1 = 80
x = -len1 // 2
y = -len1 // 2

turtle = turtle.Turtle()
turtle.color("blue")
turtle.pensize(3)
turtle.penup()
turtle.goto(x, y)
turtle.pendown()

turtle.forward(len1)
turtle.left(90)
turtle.forward(len1)
turtle.left(90)
turtle.forward(len1)
turtle.left(90)
turtle.forward(len1)
turtle.left(90)

len2 = 100
x = -len2 // 2
y = -len2 // 2

turtle.color("blue")
turtle.pensize(3)
turtle.penup()
turtle.goto(x, y)
turtle.pendown()

turtle.forward(len2)
turtle.left(90)
turtle.forward(len2)
turtle.left(90)
turtle.forward(len2)
turtle.left(90)
turtle.forward(len2)
turtle.left(90)

window.exitonclick()





