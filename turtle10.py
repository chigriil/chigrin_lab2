import turtle
turtle.speed(100)
turtle.shape('turtle')
k=0
def okr(i):
    while i < 360:
        turtle.forward(1)
        turtle.left(1)
        i += 1
while k < 6:
    okr(0)
    turtle.right(60)
    k += 1
