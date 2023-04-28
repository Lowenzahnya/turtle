from turtle import *
from random import randint

bgcolor('black')

ada = Turtle()
ada.color('red')
ada.shape('turtle')
ada.penup()
ada.setpos(-500, 100)
ada.pendown()

leon = Turtle()
leon.color('blue')
leon.shape('turtle')
leon.penup()
leon.setpos(-500, 70)
leon.pendown()

ashley = Turtle()
ashley.color('orange')
ashley.shape('turtle')
ashley.penup()
ashley.setpos(-500, 40)
ashley.pendown()

kris = Turtle()
kris.color('indigo')
kris.shape('turtle')
kris.penup()
kris.setpos(-500, 10)
kris.pendown()

for i in range(170):
    ada.forward(randint(1, 10))
    leon.forward(randint(1, 10))
    kris.forward(randint(1, 10))
    ashley.forward(randint(1, 10))
