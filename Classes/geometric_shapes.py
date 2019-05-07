#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

class square:
    def __init__(self, l=None, w=None, A=None):
        self.width = w
        self.area = A
        if type(l) == None:
            self.length = calculate_length()
        else:
            self.length = l

    def area(self):
        return self.length * self.width
    
    def circumference(self):
        return 2*(self.length + self.width)
    
    def calculate_length(self):
        return self.area / self.width

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
    rectangle = square(2,6)
    triangular_shape = triangle(3,4)

    print(f"The rectangle with lenght {rectangle.length} and width of {rectangle.width} has an area of {rectangle.area()} and a circumference of {rectangle.circumference()}")

    print(triangular_shape.area())
    print(triangular_shape.circumference())

if __name__ == "__main__":
    main()