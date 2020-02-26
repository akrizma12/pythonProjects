import turtle


#actor is a turtle
def drawSquare(actor, x, y, length):
    actor.penup()
    actor.goto(x, y)
    actor.pendown()
    for n in range(4):
        actor.forward(length)
        actor.left(90)


window = turtle.Screen()
turtle1 = turtle.Turtle()
turtle1.hideturtle()
turtle1.pencolor('white')
turtle1.pensize(9)

len1 = 80
startx = -len1 // 2
starty = -len1 // 2

drawSquare(turtle1, startx, starty, len1)

len2 = 100
startx = -len2 // 2
starty = -len2 // 2
drawSquare(turtle1, startx, starty, len2)

window.exitonclick()





