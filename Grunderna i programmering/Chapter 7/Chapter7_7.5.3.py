#!/usr/bin/env python3

print("I will ask you for 2 numbers and will then tell you how big their product is")
first_number = float(input("Please supply the first number: "))
second_number = float(input("...and not the second number: "))

product = first_number * second_number

#%.1f means a float with 1 decimal and points forward to the variable
if (product < 50):
    print("The product %.1f is a small number" %(product))
elif (product > 100):
    print("The product %.1f is a medium sized number" %(product))
elif (product > 200) and (product < 500):
    print("The product %.1f is a large number" %(product))
else:
     print("The product %.1f is a gigantic number" %(product))