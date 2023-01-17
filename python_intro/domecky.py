from turtle import forward, backward, left, right, exitonclick, penup, pendown, goto
from math import sqrt
from random import randint

def house(a):
    c = sqrt(2*a**2)
    left(90)
    forward(a)
    right(135)
    forward(c)
    left(135)
    forward(a)
    left(90)
    forward(a)
    right(135)
    forward(c/6)
    left(45)
    forward(a/3)
    right(90)
    forward(a/6)
    right(90)
    forward(a/6)
    left(135)
    forward(c/6)
    right(90)
    forward(c/2)
    right(90)
    forward(c)
    left(135)
    forward(a)

penup()
goto(-400, 0)
pendown()

for i in range(15):
    house(randint(10,100))
exitonclick()