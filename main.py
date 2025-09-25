import turtle
x = 1
# to make able to reflect
turtle.tracer(0, 0)

y = 2
# If y = 1 it draws one side of the court.
# If y = 2 it drwas the full court.
def draw_half_circle():
    for loop in range (180):
        turtle.left(1* x)
        turtle.backward(1 * x)
for loop in range (y):
    turtle.right(90 * x)
    turtle.penup()
    turtle.forward(250 * x)
    turtle.backward(500* x)
    turtle.forward(200*x)
    turtle.left(90 * x)
    turtle.pendown()
    draw_half_circle()
    turtle.penup()
    turtle.setpos((-400)* x,50)
    turtle.pendown()
    turtle.backward(200*x)
    turtle.right(270*x)
    turtle.forward(100*x)
    turtle.right(90*x)
    turtle.forward(200*x)
    turtle.backward(200*x)
    for loop in range (360):
        turtle.forward(0.87*x)
        turtle.right(1*x)
    turtle.forward(200*x)
    turtle.right(90*x)
    turtle.forward(350*x)
    turtle.backward(600*x)
    turtle.forward(100*x)
    turtle.left(90*x)
    turtle.backward(100*x)
    for loop in range (180):
        turtle.backward(3.5*x)
        turtle.left(1*x)
    turtle.backward(103*x)
    turtle.left(90*x)
    turtle.forward(100*x)
    turtle.right(90*x)
    turtle.forward(400*x)
    turtle.right(90*x)
    turtle.forward(600*x)
    turtle.right(90*x)
    turtle.forward(400*x)
    turtle.backward(400*x)
    turtle.left(90*x)

    turtle.setpos(0,0)
    x = -1
    turtle.left(90)




turtle.update()

turtle.exitonclick()
