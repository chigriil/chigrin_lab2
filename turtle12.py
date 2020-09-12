import turtle

turtle.shape('turtle')
turtle.left(90)
def poluokr1():
    i=0
    while i < 180:
        turtle.forward(10)
        turtle.right(5)
        i += 5
def poluokr2():
    k=0
    while k < 180:
        turtle.forward(2)
        turtle.right(5)
        k+=5
for l in range (1, 16):
    poluokr1()
    poluokr2()

    
