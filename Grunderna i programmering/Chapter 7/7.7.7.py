#!/usr/bin/env python3
#I will try to redo my Scratchproject for drawing n-sided polygons
#Scratchproject can be found here: https://scratch.mit.edu/projects/284614579/
#This file use the same variablenames as the scratchproject
import turtle
import time

#We start with a small introduction and ask for a number of sides. We use a try/except block to avoid shenanigans

def main():
    print("This small program will draw you any n-sided polygon and show it for 3 seconds once done.")
    while True:
        try:
            countSides = int(input("How many sides would you like on your polygon? "))
            if countSides == 1:
                print("In swedish we would call that an \"Enhörning\" which is a unicorn, gratz on finding this easteregg")
            elif countSides < 3:
                print("I hope you're aware polygons are triangles and upwards? You must supply an integer of 3 or greater value")
            elif countSides >= 3:
                break
        except ValueError:
            print("Are you sure that's a number?")
        except:
            print("Something went horribly wrong")
    
    #This has to be here since we depend on it for the turtle to work
    countDegrees = 360/countSides
    #We calculate the sidelenght to use it as the turtles walking distance
    sL = calculate_sideLenght(countSides)
    
    print("Your polygon will be drawn in:")
    timer = 3
    while not timer < 1:
        print(timer)
        time.sleep(1)
        timer -= 1

    #We make the turtle draw based on the numbers calculated
    while countSides > 0:
        turtle.forward(sL)
        turtle.right(countDegrees)
        countSides -= 1
    turtle.write("Done!")
    #We sleep for a few seconds to let the user marvel at their awesome polygon
    time.sleep(3)

def calculate_sideLenght (countSides):
    #We use the following numbers because it easily fits on most screens 
    apothemLenght = 75
    areaSize = 22500
    sideLenght = (2*areaSize)/(countSides*apothemLenght)
    return sideLenght

main()