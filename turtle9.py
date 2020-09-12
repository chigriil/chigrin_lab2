import turtle                                         
import math

turtle.shape('turtle')
turtle.speed(10)
R=50
k=3
l=0
turtle.left(30)
def polygon(n,l):                                       
    for i in range (1, n+1):
        turtle.left(180-180*(n-2)/n)
        turtle.forward(2*(R+l)*math.sin(math.pi/(2*n)))

while k<11:
    polygon(k,l)
    turtle.penup()
    turtle.right(90*(k-2)/k)
    turtle.forward(20)
    turtle.pendown()
    k+=1
    l+=40
    turtle.left(90*(k-2)/k)


