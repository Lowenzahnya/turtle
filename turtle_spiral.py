from turtle import *

speed('fastest')
hideturtle()

colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
bgcolor('black')
for i in range(500):
    pencolor(colors[i % 6])
    pensize(i // 100 + 1)
    forward(i)
    left(59)
