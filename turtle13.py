import turtle
import math
turtle.shape('turtle')
turtle.speed(10)
turtle.penup()
turtle.goto(200, 0)
turtle.left(90)
turtle.pendown()
def okr1(R):
    i=0
    while i<360:
        turtle.forward(R)
        turtle.left(5)
        i+=5
def okr2(R):
    i=0
    while i<360:
        turtle.forward(R)
        turtle.right(5)
        i+=5
def poluokr(r):
    k=0
    while k<180:
        turtle.backward(r)
        turtle.right(5)
        k+=5

turtle.fillcolor('yellow')
turtle.begin_fill()
okr1((50/9)*math.pi)
turtle.end_fill()

turtle.penup()
turtle.goto(-70, 70)
turtle.fillcolor('blue')
turtle.begin_fill()
okr1(3)
turtle.end_fill()

turtle.penup()
turtle.goto(70, 70)
turtle.fillcolor('blue')
turtle.begin_fill()
okr2(3)
turtle.end_fill()

turtle.penup()
turtle.goto(0,50)
turtle.pendown()
turtle.width(30)
turtle.backward(70)

turtle.penup()
turtle.goto(115, -40)
turtle.pendown()
turtle.pencolor('red')
poluokr(10)

