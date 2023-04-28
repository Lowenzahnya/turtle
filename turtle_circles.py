import turtle
import colorsys

turtle.shape('turtle')
turtle.bgcolor('black')
turtle.tracer(3, 25)
size = 0
h = 0

while True:
    for i in range(75):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        h += 0.1
        turtle.color(c)
        turtle.circle(size)
        turtle.left(5)
        size = size + 3
