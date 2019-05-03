"""
 John Dewey - kodexempel 3
 Turtle graphics i Python
 En digital gradcirkel
"""

from turtle import * 

for vinkel in range(0, 360, 15):
    setheading(vinkel)
    forward(100)
    write(str(vinkel) + '°')
    backward(100)

turtle.exitonclick()