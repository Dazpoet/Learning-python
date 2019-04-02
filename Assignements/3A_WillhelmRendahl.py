#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys

#Assignement: Create a sieve for primes which takes user input on the lowest and highest number and find all primes between the two
#Inspiration taken from https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
#TODO: Simple GUI with buttons for each function
#TODO: Add performance-measuring timer using time.perf_counter_ns()
#TODO: Tell the user how many primes were found
#TODO: Figure out why the prime finder doesn't work for 36

def collect_sieve_data ():
        while True:
                try:
                        first_number = int(input("Ange ett heltal större än 1 från vilket du vill börja lista primtal?: "))
                        last_number = int(input("Vid vilket heltalsvärde vill du sluta leta efter primtal?: ")) + 1 #We add 1 to get what the user acctually wants
                        if first_number > last_number:
                                print("Ditt startvärde måste vara större än ditt slutvärde")
                        elif first_number < 2:
                                print("Ditt startvärde måste vara större än 1, det finns inga primtal lägre än 2")
                        else:
                                break
                except ValueError:
                        print("Du måste skriva in heltal")
                except (KeyboardInterrupt, EOFError): #I have yet to encounter someone who doesn't want to quit on these errors
                        sys.exit("Avslutar programmet")

        return first_number, last_number

def sieve_of_eratosthenes(user_input):
        #Below something called dict comprehension is used and I was inspired from https://docs.python.org/3/tutorial/datastructures.html#dictionaries
        values = {i: True for i in range(2,user_input[1])} #This generates the array (dictionary) with indexes and boolean values mentioned in sieve pseudocode
        index_of_non_primes = []

        #We want to perform the following for each integer between 2 and the floor of sqrt(n) since the method requires no values larger than sqrt(n)
        for i in range(2,math.floor(math.sqrt(user_input[1]))):
                if values[i] == True:
                        n = 0

                        while True: #This might be just as doable with "while not j > last_number"?
                                j = i**2 + n*i #I considered naming j "index" but felt it would be confusing with the latter for loop. TODO: Make up a better variable name
                                index_of_non_primes.append(j)
                                n += 1
                                if j > user_input[1]:
                                        break
                
        for index in index_of_non_primes:
                values[index] = False

        prime_values = []

        for prime in range(user_input[0],user_input[1]):
                if values[prime] == True:
                        prime_values.append(prime)

        return prime_values

def find_prime_factors(number):
        #Start by finding all the 2s in the number, we do this specially since 2 is the only even prime
        while number % 2 == 0:
                print(2)
                number //= 2
        
        #With all 2s removed the remainder must be an odd number
        #We move through the odd numbers between 3 and sqrt(number)+1
        for i in range(3, math.floor(math.sqrt(number))+1, 2):
                while number % i == 0:
                        print(i)
                        number //= i
        #If we're stuck with a number larger than 2 at the end that number must be a prime so we return it
        if number > 2:
                print(number)                

def main():
        
        choice = int(input("1. Såll\n2. Primtalsfaktorer\n"))
        if choice == 1:        
                user_input = collect_sieve_data()
                primes = sieve_of_eratosthenes(user_input)
                print(primes)
        elif choice == 2:
                user_input = int(input("Vilket tal vill du ha primtalsfaktorer för?: "))
                find_prime_factors(user_input)
                
if __name__ == "__main__":
        main()