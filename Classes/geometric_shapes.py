#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

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
        elif self.perimeter and self.area:
            length = self.calculate_length_from_area_and_perimeter()
            return length
        elif self.width: #If we only get a width we consider it a square and set L = W
            return self.width
        elif self.area or self.perimeter:  #if only one of these is given we threat it as a square due to lack of sufficient solving methods
            if self.area:
                return math.sqrt(self.area)
            if self.perimeter:
                return self.perimeter / 4
    
    def calculate_width(self):
        if self.area and self.length:
            return self.area / self.length
        elif self.perimeter and self.length:
            return (self.perimeter / 2) - self.length
        elif not self.perimeter and not self.area: #If we only get a lenght we consider it a square and set W = L
            return self.length
    
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