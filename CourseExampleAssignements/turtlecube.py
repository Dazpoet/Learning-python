#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import turtle 

nils = turtle.Turtle()

def draw_square(startx,starty):
    nils.up()
    nils.setpos(startx,starty)
    nils.setheading(0)
    nils.down()

    for _ in range(4):
        nils.forward(100)
        nils.left(90)

def draw_diagonals(positions):
    nils.setheading(45)
    
    for i in range(0,4):
        nils.up()
        nils.setpos(positions[i][0], positions[i][1])
        nils.down()
        nils.forward(50)

def main():
    corner_positions = [(0,0), (100,0), (0,100), (100,100)]

    draw_square(0,0)
    draw_diagonals(corner_positions)
    draw_square(35.36,35.36)

    turtle.exitonclick()

if __name__ == "__main__":
    main()