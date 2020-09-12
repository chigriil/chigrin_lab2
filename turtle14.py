import turtle
turtle.shape('turtle')
def star(n):
    i=0
    while i < n:
        turtle.forward(500)
        turtle.left(180-180/n)
        i+=1
n=int(input())
star(n)
        
