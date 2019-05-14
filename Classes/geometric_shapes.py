#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

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

        if None in [self.radius, self.area, self.circumference]:
            raise ValueError("There's None in my circle")

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
            raise ValueError("There's a None in my rectangles sides")
    
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
        for l in range(self.area):
            for w in range(self.perimeter):
                if (l * w == self.area) and (2 * l + 2 * w == self.perimeter):
                    return l


class Triangle:
    def __init__(self, a, b, c, height): #What is height in this context?
        self.side_a = a
        self.side_b = b
        self.side_c = c
        self.height = height
    
    def area(self):
        pass
    
    def circumference(self):
        pass

def main():
    pass

if __name__ == "__main__":
    main()