#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import turtle 

#Name my turtle
nils = turtle.Turtle()

def draw_square(startx,starty): #Given a starting position in the form x,y this draws a cube with each corner going to the left
    nils.up() #Make sure we don't draw any unnecessary lines
    nils.setpos(startx,starty) #Set nils to the correct position
    nils.setheading(0) #Set nils to the expected heading
    nils.down() #Put the pen down so we can start drawing

    #Draw the square
    for _ in range(4):
        nils.forward(100)
        nils.left(90)

def draw_diagonals(positions): #Given a list of tuples containing positions in x,y format draw diagonals of lenght 50 at a 45 degree angle from each corner
    nils.setheading(45) #We want each line to be in a 45 degree heading
    
    for i in range(0,4):
        nils.up() #Take the pen up to make sure we don't draw any lines while "teleporting"
        nils.setpos(positions[i][0], positions[i][1]) #Set the position from where to draw
        nils.down() #Put the pen down
        nils.forward(50) #Draw the line

def main():
    corner_positions = [(0,0), (100,0), (0,100), (100,100)]

    draw_square(0,0)
    draw_diagonals(corner_positions)
    draw_square(35.36,35.36) #These were found using nils.pos() from the first corner, if we don't start here it looks bad

    turtle.exitonclick()

if __name__ == "__main__":
    main()