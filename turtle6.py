import turtle
turtle.shape('turtle')

n=int(input())

for i in range(1, n+1):
    turtle.forward(100)
    turtle.stamp()
    turtle.left(180)
    turtle.forward(100)
    turtle.left(180)
    turtle.right(360/n)

