import turtle
import math

turtle.shape('turtle')
i=0

while i<10:
    for k in range (1,5):
        turtle.forward(50+10*2*i*math.sin(math.pi/4))
        turtle.left(90)
    turtle.penup()
    turtle.right(135)
    turtle.forward(10)
    turtle.left(135)
    turtle.pendown()
    i+=1
