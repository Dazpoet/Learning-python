#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

class Square:
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
        if bool(self.area) and bool(self.width):
            return self.area / self.width
        elif bool(self.perimeter) and bool(self.width):
            return (self.perimeter / 2) - self.width
        elif bool(self.perimeter) and bool(self.area):
            return
    
    def calculate_width(self):
        if bool(self.area) and bool(self.length):
            return self.area / self.length
        elif bool(self.perimeter) and bool(self.length):
            return (self.perimeter / 2) - self.length
    
    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return 2*(self.length + self.width)


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