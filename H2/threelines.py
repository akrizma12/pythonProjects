# Write a program draws the picture within the box shown at the right (but don't draw the box.)

# Each line is of length 200 and separated from the next line by 30 units.
# The bottom right end of the lowest line is at (0,0) (the turtle's home location),
# and all lines have a pen width of 3.
# (HTT4 has a code example that shows how to set the pen width for a turtle.)
# Be sure to have wn.exitonclick() as the last statement of your program.

import turtle

point1 = (0, 0)                 #Starting point, first line x axis
point2 = (-200, 0)              #First line y axis
point3 = (-200, 30)             #Second line x axis
point4 = (0, 30)                #Second line y axis
point5 = (0, 60)                #Third line x axis
point6 = (-200, 60)             #Third line y axis

window = turtle.Screen()
window.bgcolor('light green')

turtle = turtle.Turtle()
turtle.color("blue")
turtle.pensize(3)

turtle.penup()                  #no drawing when moving
turtle.goto(point1)

turtle.pendown()                #drawing when moving
turtle.goto(point2)

turtle.penup()
turtle.goto(point3)

turtle.pendown()
turtle.goto(point4)

turtle.penup()
turtle.goto(point5)

turtle.pendown()
turtle.goto(point6)

turtle.hideturtle()         #this hides arrow
window.exitonclick()        #Be sure to have wn.exitonclick()
