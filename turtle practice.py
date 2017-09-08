import turtle

def drawOctagon(side_length):
    for x in range(8):
        turtle.forward(side_length)
        turtle.left(45)

turtle.speed(5)

turtle.color("red")

turtle.begin_fill()

drawOctagon(100)

turtle.end_fill()

turtle.penup()

turtle.goto(400,0)

turtle.color("green")

turtle.pendown()

turtle.begin_fill()

drawOctagon(100)

turtle.end_fill()

turtle.penup()

turtle.goto(400,-300)

turtle.color("yellow")

turtle.pendown()

turtle.begin_fill()

drawOctagon(100)

turtle.end_fill()

turtle.penup()

turtle.goto(0,-300)

turtle.color("pink")

turtle.pendown()

turtle.begin_fill()

drawOctagon(100)

turtle.end_fill()

turtle.exitonclick()