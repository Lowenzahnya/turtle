from turtle import *
import colorsys

bgcolor('black')
tracer(10)
pensize(3)
h = 0

while True:
    for i in range(300):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        h += 0.0065
        pencolor(c)
        fillcolor('black')
        begin_fill()
        for j in range(2):
            forward(i*1.2)
            right(60)
            forward(300)
            right(120)
        end_fill()
        right(121)
