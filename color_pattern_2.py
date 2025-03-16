# PROJECT 6 - PATTERN 2: Flower Color Pattern 1 

from turtle import *
import colorsys

tracer(1)
speed(0.5)
h = 0.7
bgcolor("black")
pensize(5)

penup()
goto(0, 100)
pendown()

for i in range(150):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    color(c)
    h += 0.004
    circle(150 - i, 90)
    lt(90)
    lt(20)
    circle(150 - i, 90)
    lt(18)

done()
