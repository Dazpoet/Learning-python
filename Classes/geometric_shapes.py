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
        #value_2 = constant - disc #This isn't needed but I'm a completionist

        return value_1


"""    
    def calculate_length_from_area_and_perimeter(self): #We never want to end up here! This is a horrible place and I hope you brought scotch
        #TODO: Refactor this part to avoid code-reuse
        #TODO: Try to figure out a better logic for this entire function
        def get_perimeter_exponent(num): #gets an exponent for converting a float to an int using int(<float>*(10**exponent))
            if num < 1: #if the perimeter is less than 1 this will fix it
                exponent = len(str(num)) - 2 #remove the comma and account for count starting at 0
                return exponent
            elif isinstance(num, int): #if the perimeter is an int the exponent can be the length of it because the integer will be small
                exponent = len(str(num))
                return exponent
            else:
                raise ValueError("Cannot calculate perimeter exponent")

        def find_length(area, perimeter):
            for l in range(area + 1):
                for w in range(perimeter + 1):
                    if (l * w == area) and (2 * l + 2 * w == perimeter):
                        return l

        def amount_of_decimals(num): #returns the amount of decimals in a float
            amount = len(str(num)) - str(num).find(".") - 1 #-1 accounts for starting the count at 0

            return amount

        if isinstance(self.area, int) and isinstance(self.perimeter, int): #If both area and perimeter are ints this is easy-peasy
            l = find_length(self.area, self.perimeter)
            return l
        elif (self.area < 1) or (self.perimeter < 1): #if area or perimeter is below 1 we need to apply some tricks to get things working
            exp_perimeter = get_perimeter_exponent(self.perimeter)
            
            if exp_perimeter == 1: #This is a special case were the the perimeter is a value below 10
                exp_area = 2
            else:
                exp_area = exp_perimeter**2 #area scale = lenght scale squared TODO: Figure out if this ever triggers

            perimeter_int = int(self.perimeter * (10**exp_perimeter))
            area_int = int(self.area * (10**exp_area))

            l = find_length(area_int, perimeter_int)
            correct_l = l * (10**(-exp_perimeter))

            return correct_l
        elif isinstance(self.perimeter, float) or isinstance(self.area, float): #if either of these is a float it won't work with find_length() so we need to massage them a bit
            #TODO: Kill this abomination
            #Set the stage for the coming if-logic
            decimals_in_area, decimals_in_perimeter, perimeter_int, area_int = None, None, None, None

            #Check if we can lazy convert the perimeter to an int
            try:
                perimeter_int = int(str(self.perimeter))
            except ValueError:
                decimals_in_perimeter = amount_of_decimals(self.perimeter) 
            
            #Check if we can lazy convert the area to an int
            try:
                area_int = int(str(self.area))
            except ValueError:
                decimals_in_area = amount_of_decimals(self.area)

            #If both could be lazy converted we do the thing
            if perimeter_int and area_int:
                l = find_length(area_int, perimeter_int)
                return l
            elif decimals_in_perimeter and decimals_in_area:
                if decimals_in_perimeter > decimals_in_area:
                    exp_perimeter = decimals_in_perimeter
                    if exp_perimeter == 1: #This is a special case were the the perimeter length is a value below 10
                        exp_area = 2
                    else:
                        exp_area = exp_perimeter**2 #area scale = lenght scale squared

                    perimeter_int = int(self.perimeter * (10**exp_perimeter))
                    area_int = int(self.area * (10**exp_area))

                    l = find_length(area_int, perimeter_int)
                    correct_l = l * (10**(-exp_perimeter))

                    return correct_l
                else: #when the area has more decimals
                    pass
            elif decimals_in_perimeter and not decimals_in_area: #If only the perimeter is a float we multiply and use the same method as when one was a float, this is code re-use and needs to be refactored
                exp_perimeter = decimals_in_perimeter
                if exp_perimeter == 1: #This is a special case were the the perimeter length is a value below 10
                    exp_area = 2
                else:
                    exp_area = exp_perimeter**2 #area scale = lenght scale squared

                perimeter_int = int(self.perimeter * (10**exp_perimeter))
                area_int = int(self.area * (10**exp_area))

                l = find_length(area_int, perimeter_int)
                correct_l = l * (10**(-exp_perimeter))

                return correct_l
            elif decimals_in_area and not decimals_in_perimeter: #This is a tricky case which I haven't solved yet so for now it raises an error
                raise ValueError("Why are you a bad person, please only use integers for area if the perimeter is an integer")
"""



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