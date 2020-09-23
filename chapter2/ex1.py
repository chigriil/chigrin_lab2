import turtle
from random import *
turtle.shape('turtle')
for i in range (10000):
    x = randint(0, 200)
    y = randint(0,360)
    turtle.forward(x)
    turtle.left(y)