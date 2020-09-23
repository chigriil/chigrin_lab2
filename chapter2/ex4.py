from random import randint
import turtle as t
t.penup()
t.goto(-100,100)
t.left(270)
t.pendown()
for i in range (1,5):
    t.forward(200)
    t.left(90)
t.penup()
t.goto(0, 0)
t.hideturtle()
number_of_turtles = 10
pool = [t.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.shapesize(0.5, 0.5)
    unit.goto(randint(-100, 100), randint(-100, 100))
    unit.speed(10)
    unit.seth(randint(0,360))
while True:
    for unit in pool:
        if abs(unit.xcor())>100:
            unit.seth(180-unit.heading())
        if abs(unit.ycor())>100:
            unit.seth(360-unit.heading())
        unit.fd(10*0.2)