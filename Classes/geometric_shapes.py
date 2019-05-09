#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys

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
    
    def calculate_length(self):
        if self.area and self.width:
            return self.area / self.width
        elif self.perimeter and self.width:
            return (self.perimeter / 2) - self.width
        elif self.area:
            return math.sqrt(self.area) #This should only ever trigger when we deal with perfect squares, otherways at least perimeter and area MUST be given
        elif self.perimeter and self.area:
            length = self.calculate_length_from_area_and_perimeter()
            return length
    
    def calculate_width(self):
        if self.area and self.length:
            return self.area / self.length
        elif self.perimeter and self.length:
            return (self.perimeter / 2) - self.length
    
    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return 2*(self.length + self.width)
    
    def calculate_length_from_area_and_perimeter(self):
        #A quadritic expression ax^2 + bx + c = 0
        #has the known solution x = (-b +-sqrt(b^2-4ac))/2a
        #
        #if the discriminant (sqrt(b^2-4a)) < 0 there are no real roots
        #elif the discriminant = 0 there is a single root
        #else there are two solutions such that
        #x1 = -b/2a + discriminant
        #x2 = -b/2a - discriminant
        #
        #Given an area and perimeter of a square such that
        #1. P = 2L + 2W
        #and
        #2. A = L * W
        #
        #1. gives 3.
        #W = (P-2L)/2
        #
        #3. in 2. gives
        #A/L = (P-2L)/2
        #which after multiplying with L on both sides give
        #
        #2L^2 - PL + 2A = 0
        #Which is a quadratic equation, since we deal with
        #geometric shapes no complex solutions will be useful
        
        length = None
        constant = self.perimeter/(4*self.area)
        d = math.sqrt((-(self.perimeter)**2 - 4*(2*2*self.area)))
        
        if d < 0:
            sys.exit("Why are there complex roots in my lengths?")
        elif d == 0:
            length = constant
        else:
            length1 = constant + d
            length2 = constant - d
            if length1 < 0:         #We don't want negative lengths
                length = length2
            elif length2 < 0:
                sys.exit("Why are there no positive lengths?")
            else:
                length = length1    #Length1 always wins if both at positive
        
        return length


class triangle:
    def __init__(self, b, h):
        self.base = b
        self.height = h
    
    def area(self):
        area = (self.base * self.height) / 2
        return area
    
    def circumference(self):
        side_length = math.sqrt(((self.base)/2)**2 + self.height**2)
        circumference = side_length*2 + self.base

        return circumference

def main():
    pass

if __name__ == "__main__":
    main()