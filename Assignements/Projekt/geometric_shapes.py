#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import random

#TODO: Consider negative numbers
#TODO: Add x0, y0 as attributes
#TODO: Consider precision and rounding, done in class or when using the results?

class Circle:
    def __init__(self, r=None, A=None, C=None):
        self.radius = r
        if r:
            self.diameter = 2*r
        self.area = A
        self.circumference = C

        if not r:
            self.radius = self.calculate_radius()
            self.diameter = 2*self.radius
        if not A:
            self.area = self.calculate_area()
        if not C:
            self.circumference = self.calculate_circumference()

    def calculate_radius(self):
        radius = None

        if self.area:
            radius = math.sqrt(self.area/math.pi)
        elif self.circumference:
            radius = self.circumference/(2*math.pi)
        
        return radius
    
    def calculate_area(self):
        area = math.pi * self.radius**2

        return area

    def calculate_circumference(self):
        circumference = math.pi * 2 * self.radius

        return circumference

class Rectangle:
    def __init__(self, l=None, w=None, A=None, P=None):
        self.length = l
        self.width = w
        self.area = A
        self.perimeter = P

        if not l:
            self.length = self.calculate_length()
        if not w:
            self.width = self.calculate_width()        
        if not A:
            self.area = self.calculate_area()
        if not P:
            self.perimeter = self.calculate_perimeter()
        
        if None in [self.length, self.width]:
            raise ValueError("There's a None side in this rectangle")
    
    def calculate_length(self):
        length = None

        if self.area and self.width:
            length = self.area / self.width
        elif self.perimeter and self.width:
            length = (self.perimeter / 2) - self.width
        elif self.perimeter and self.area:
            length = self.calculate_length_from_area_and_perimeter()
        elif self.width: #If we only get a width we consider it a square and set L = W
            length = self.width
        elif self.area or self.perimeter:  #if only one of these is given we threat it as a square due to lack of sufficient solving methods
            if self.area:
                length = math.sqrt(self.area)
            if self.perimeter:
                length = self.perimeter / 4

        return length

    def calculate_width(self):
        width = None
        
        if self.area and self.length:
            width = self.area / self.length
        elif self.perimeter and self.length:
            width = (self.perimeter / 2) - self.length
        elif not self.perimeter and not self.area: #If we only get a lenght we consider it a square and set W = L
            width = self.length

        return width
        
    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return 2*(self.length + self.width)

    def calculate_length_from_area_and_perimeter(self):
        #Since we have two unknowns and two known formulas
        #A = l * b
        #P = 2*(l * b)
        #we can find that
        #l = P/4 +- sqrt(P^2/16 - A)
        #where the two solutions will be the length and width of the rectangle

        constant = self.perimeter/4
        disc = math.sqrt(((self.perimeter**2)/16)-self.area)

        value_1 = constant + disc
        value_2 = constant - disc

        #Make sure everything seems correct
        assert value_1 * value_2 == self.area
        assert 2*value_1 + 2*value_2 == self.perimeter

        return value_1

class Triangle:
    def __init__(self, b=None, h=None, A=None): #Extremely simplified as an example
        self.base = b
        self.height = h
        self.area = A

        if not b:
            self.base = self.calculate_base
        if not h:
            self.height = self.calculate_height
        if not A:
            self.area = self.calculate_area
    
    def calculate_base(self):
        return 2*self.area/self.height

    def calculate_height(self):
        return 2*self.area/self.base

    def calculate_area(self):
        return (self.base*self.height)/2

if __name__ == "__main__":
    texts = [
        "Your mother was a hamster and your father smelt of elderberries",
        "Do you find it risible when I say the name... Biggus... Dickus...?",
        "Nobody expects the spanish inquisition!",
        "You must cut down the mightiest tree in the forest with...a herring!",
        "*fishslap to the face*",
        "No that's not dead, it's err... resting",
        "Bunch of monkeys on the ceiling, sir! Grab your egg-and-fours and let's get the bacon delivered!"
        ]
    print(random.choice(texts))