from turtle import *
import colorsys

bgcolor('black')
speed('fastest')
hideturtle()
pensize(2)
h = 0

for i in range(0, 300, 5):
    for j in range(4):
        left(90)
        forward(i+10)
    left(20)
    c = colorsys.hsv_to_rgb(h, 1, 1)
    h += 0.1
    pencolor(c)

mainloop()

