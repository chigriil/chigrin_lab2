import turtle
import math
turtle.shape('turtle')
fi_rad=0.1

for i in range (1, 100000):
    turtle.forward(i*fi_rad/10000)
    fi_deg=fi_rad*(math.pi/180)
    turtle.left(fi_deg)
    fi_rad+=0.1
    
