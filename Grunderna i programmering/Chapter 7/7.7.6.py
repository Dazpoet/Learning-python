#!/usr/bin/env python3
#Create a program that asks for a given number and prints that many letters of the alphabet

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",\
    "r", "s", "t", "u", "v", "w", "q", "x", "y", "z", "å", "ä", "ö"]

while True:
    try:
        amount = int(input("How many letters of the alphabet would you like to see?: "))
        if (amount >= 0) and (amount <= 30):
            break
        else:
            print("You must supply an integer between 0 and 30")
    except ValueError:
        print("That's not a number")

for i in range(amount):
        print(letters[i], end=" ")
print() #we add a print at the end just to get a better looking output