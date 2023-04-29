import turtle
import colorsys

turtle.title("тест")
turtle.tracer(3)
turtle.hideturtle()
turtle.bgcolor('black')
h = 0

for i in range(500):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    h += 0.05
    turtle.color(c)
    turtle.forward(50+i)
    turtle.right(91)

turtle.mainloop()