# Kevin Chen
# 09/08/17
# turtle practice
# draw four Octagon in four different colors.

import turtle


def drawOctagon(side_length, color):
    turtle.color(color)
    turtle.begin_fill()
    for x in range(8):
        turtle.forward(side_length)
        turtle.left(45)
    turtle.end_fill()


def moveTurtle(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


turtle.speed(5)


drawOctagon(100, "red")


moveTurtle(400, 0)


drawOctagon(100, "green")


moveTurtle(400, -300)


drawOctagon(100, "yellow")


moveTurtle(0, -300)


drawOctagon(100, "pink")


turtle.exitonclick()
