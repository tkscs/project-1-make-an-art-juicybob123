import turtle
x = 1
# to make able to reflect
turtle.tracer(0, 0)
n = 1
y = 2
j = 1
# If y = 1 it draws one side of the court.
# If y = 2 it drwas the full court.

def draw_half_circle( direction):
    for loop in range (180):
        turtle.left(1* direction)
        turtle.backward(1 * direction)

def draw_half_court( direction ):
    turtle.right(90 * direction)

    turtle.penup()
    turtle.forward(250 * direction)
    turtle.backward(500* direction)
    turtle.forward(200*direction)
    turtle.left(90 * direction)
    turtle.pendown()
    draw_half_circle(direction)
    turtle.penup()
    turtle.setpos((-400)* direction,50)
    turtle.pendown()

    turtle.backward(200*direction)
    turtle.right(270*direction)
    turtle.forward(100*direction)
    turtle.right(90*direction)
    turtle.forward(200*direction)
    turtle.backward(200*direction)
    for loop in range (360):
        turtle.forward(0.87*direction)
        turtle.right(1*direction)
    turtle.forward(200*direction)
    turtle.right(90*direction)
    turtle.forward(350*direction)
    turtle.backward(600*direction)
    turtle.forward(100*direction)
    turtle.left(90*direction)
    turtle.backward(100*direction)
    for loop in range (180):
        turtle.backward(3.5*direction)
        turtle.left(1*direction)
    turtle.backward(103*direction)
    turtle.left(90*direction)
    turtle.forward(100*direction)
    turtle.right(90*direction)
    turtle.forward(400*direction)
    turtle.right(90*direction)
    turtle.forward(600*direction)
    turtle.right(90*direction)
    turtle.forward(400*direction)
    turtle.backward(400*direction)
    turtle.left(90*direction)    

draw_half_court( 1 )
turtle.setpos(0,0)
turtle.left(90)

if y == 2: 
    draw_half_court( -1 )
    #turtle.left(90)

turtle.update()

turtle.exitonclick()
