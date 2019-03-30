#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

#Assignement: Create a sieve for primes which takes user input on the lowest and highest number and find all primes between the two
#Inspiration taken from https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

#Query user for input
first_number = int(input("Ange ett heltal större än 1 från vilket du vill börja lista primtal?: "))
last_number = int(input("Vid vilket heltalsvärde vill du sluta leta efter primtal?: ")) + 1 #Add +1 to acctually get the number the user wants

#Below something called dict comprehension is used and I was inspired from https://docs.python.org/3/tutorial/datastructures.html#dictionaries
values = {i: True for i in range(first_number,last_number)} #This generates the array (dictionary) with indexes and boolean values mentioned in sieve pseudocode

#We want to perform the following for each integer between 2 and the floor of sqrt(n) since the method requires no values larger than sqrt(n)
for i in range (2,math.floor(math.sqrt(last_number))):
    if values[i] == True:
        index_of_non_prime = []
        n = 0

        #There is no do-until functionallity in python but the below works in a similar way and was fectched from https://stackoverflow.com/questions/1662161/is-there-a-do-until-in-python
        while True: #This might be just as doable with "while not j > last_number"?
            j = i**2 + n*i #I considered naming j "index" but felt it would be confusing with the latter for loop. TODO: Make up a better variable name
            index_of_non_prime.append(j)
            n += 1
            if j > last_number:
                break
        for index in index_of_non_prime:
            values[index] = False

prime_values = []
for prime in range(first_number,last_number):
    if values[prime] == True:
        prime_values.append(prime)

print(prime_values)

#for prime in range (first_number,last_number):
#    if values[prime] == True:
#        print(prime, end=" ")