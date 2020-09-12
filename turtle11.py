import turtle
turtle.speed(1000)

turtle.left(90)
turtle.shape('turtle')
def okr1(i,l):
    while i < 360:
        turtle.forward(l)
        turtle.left(1)
        i += 1
def okr2(i,l):
    while i < 360:
        turtle.forward(l)
        turtle.right(1)
        i += 1
for m in range (1, 15):
    okr1 (0, m/2)
    okr2 (0, m/2)
    
