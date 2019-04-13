#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#TODO: Add an easter egg

import math
import sys
import time

#Assignement: Create a sieve for primes which takes user input on the lowest and highest number and find all primes between the two
#Inspiration taken from https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

def collect_sieve_data (): #This function collects user input for a starting and stopping value for the sieve calculations
        while True:
                try:
                        first_number = int(input("Ange ett heltal större än 1 från vilket du vill börja lista primtal?: "))
                        last_number = int(input("Vid vilket heltalsvärde vill du sluta leta efter primtal?: "))
                        if first_number > last_number:
                                print("Ditt startvärde måste vara större än ditt slutvärde")
                        elif first_number < 2:
                                print("Ditt startvärde måste vara större än 1, det finns inga primtal lägre än 2")
                        else:
                                return first_number, last_number
                except ValueError:
                        print("Du måste skriva in heltal")
                except (KeyboardInterrupt, EOFError): #I have yet to encounter someone who doesn't want to quit on these errors
                        sys.exit("Avslutar programmet")

def collect_single_int(): #Collects a single integer value that is >= 2
        while True:
                try:
                        single_int = int(input("Vilket tal vill du testa mot?: "))
                        if single_int < 2:
                                print("Det finns inga primtal lägre än 2")
                        else:
                                return single_int
                except ValueError:
                        print("Alla primtal är heltal")
                except (KeyboardInterrupt, EOFError):
                        sys.exit("Avslutar programmet")

def main_menu(): #The main manu for this specific program, returns an integer
        try:        
                choice = int(input("\nVad vill du göra?\n"
                        "1. Hitta alla primtal mellan två tal\n"
                        "2. Hitta alla primtalsfaktorer till ett givet tal\n"
                        "3. Ta reda på om ett tal är ett primtal eller ej\n"
                        "4. Avsluta programmet\n"))
                return choice
        except ValueError:
                print("Du måste ange ett heltalsalternativ som är antingen 1, 2 eller 3.")
        except (KeyboardInterrupt, EOFError):
                sys.exit("Avslutar programmet")

def sieve_of_eratosthenes(user_input): #This returns a tuple with time to perfom the action in ms first and a list of primes second
        start = time.perf_counter_ns()
        
        values = {i: True for i in range((user_input[1] + 1))} #This generates the array (dictionary) with indexes and boolean values mentioned in sieve pseudocode
        values[0] = values[1] = False #There are no primes below 2

        #We want to perform the following for each integer between 2 and the floor of sqrt(n) since the method requires no values larger than sqrt(n)
        for i in range(2, math.ceil(math.sqrt(user_input[1]) + 1 )):
                if values[i] == True:
                        for j in range(i**2, user_input[1] + 1, i):
                                values[j] = False
        
        #Create an empty list for primes
        prime_values = []
        #Add all the primes to a list
        for prime in range(user_input[0],(user_input[1] + 1)):
                if values[prime]:
                        prime_values.append(prime)

        stop = time.perf_counter_ns()
        calculation_time = (stop - start) / 1000000 #Returns the calculation time in milliseconds

        return calculation_time, prime_values

def sieve_of_eratosthenes_2(user_input): #Returns a tuple with performance time in ms and a list of primes based on user input
        start = time.perf_counter_ns()

        #Start by creating a list of booleans for all numbers between 2 and the maximum number the user inputted, these are all potential primes
        candidates = [True for _ in range(user_input[1] + 1)] #It doesn't work if this is range(2, user_input[1] + 1) and I have no idea why
        candidates[0:1] = [False, False] #The first two values must be false since there are no primes below 2

        for index in range(2, math.ceil(math.sqrt((user_input[1] + 1)))):
                if candidates[index]: #If the candidate is True we perform the below operations, since this always starts at 2 we're in the clear since that is always true
                        for i in range(index**2, (user_input[1] + 1), index): #When the candidate was true we remove all following multiples of it by stepping through candidates in steps equal to the size of candidate
                                candidates[i] = False #Set multiple, which is at index i, to false

        #Create an empty list of primes in which we'll input the true primes from candidates
        primes = []
        
        for i in range(user_input[0], user_input[1] + 1):
                if candidates[i]:
                        primes.append(i)

        stop = time.perf_counter_ns()

        calculation_time = (stop - start) / 1000000

        return calculation_time, primes

def primitive_sieve(user_input):
        start = time.perf_counter_ns()

        #Start by creating a list of booleans for all numbers between 2 and the maximum number the user inputted, these are all potential primes
        candidates = [True for _ in range(user_input[1] + 1)] #It doesn't work if this is range(2, user_input[1] + 1) and I have no idea why
        candidates[0:1] = [False, False] #The first two values must be false since there are no primes below 2

        for index in range(2, user_input[1] + 1):
                if not is_prime(index):
                        candidates[index] = False

        #Create an empty list of primes in which we'll input the true primes from candidates
        primes = []
        
        for i in range(user_input[0], user_input[1] + 1):
                if candidates[i]:
                        primes.append(i)

        stop = time.perf_counter_ns()

        calculation_time = (stop - start) / 1000000

        return calculation_time, primes

def find_prime_factors(number): #Finds the prime factors of a given number and return them as a list
        prime_factors = []

        #Start by finding all the 2s in the number, we do this specially since 2 is the only even prime
        while number % 2 == 0:
                prime_factors.append(2)
                number //= 2
        
        #With all 2s removed the remainder must be an odd number
        #We move through the odd numbers with a step lenght of 2 to make sure we don't hit an even one
        for i in range(3, math.floor(math.sqrt(number))+1, 2): #Why, pray tell, is the +1 needed here
                while number % i == 0:
                        prime_factors.append(i)
                        number //= i
        #If we're stuck with a number larger than 2 at the end that number must be a prime so we return it
        if number > 2:
                prime_factors.append(number)
        
        return prime_factors

def is_prime(number): #Tests if a number is a prime and returns a boolean
        for i in range (2, number):
                if number % i == 0: #If an integer i gives a modulus 0 it means the number isn't a prime
                        return False
        return True                

def main():
        while True:
                choice = main_menu()
                if choice == 1:        
                        user_input = collect_sieve_data()
                        primes = sieve_of_eratosthenes_2(user_input)
                        print(f"Beräkningen tog {round(primes[0], 2)} millisekunder och det finns {len(primes[1])} primtal mellan {user_input[0]} och {user_input[1]}, de är:\n", *primes[1], sep=" ", end="\n")
                elif choice == 2:
                        user_input = collect_single_int()
                        prime_factors = find_prime_factors(user_input)
                        print(f"Primtalsfaktorerna av {user_input} är: ", *prime_factors, sep=" ", end="\n")
                elif choice == 3:
                        user_input = collect_single_int()
                        prime = is_prime(user_input)
                        if prime:
                                print(f"{user_input} är ett primtal")
                        else:
                                print(f"{user_input} är inte ett primtal")
                elif choice == 4:
                        sys.exit()
                else:
                        print("Du måste välja ett värde 1, 2, 3 eller 4.")

def test_main():
        for _ in range(5):
                p1_wins = 0
                p2_wins = 0
                p3_wins = 0
                for i in range(1000):
                        testbas = 2, i
                                
                        primes_1 = sieve_of_eratosthenes(testbas)
                        primes_2 = sieve_of_eratosthenes_2(testbas)
                        primes_3 = primitive_sieve(testbas)

                        if primes_1[1] == primes_2[1]== primes_3[1]:
                                pass
                        else:
                                print("Annorlunda resultat i körning ", i)
                                print(primes_1[1], primes_2[1], primes_3, sep='\n')

                        if primes_1[0] < (primes_2[0] and primes_3[0]):
                                p1_wins += 1
                        elif primes_2[0] < (primes_1[0] and primes_3[0]):
                                p2_wins += 1
                        elif primes_3[0] < (primes_1[0] and primes_2[0]):
                                p3_wins += 1
                
                winner_dict = {"Dict":p1_wins, "List":p2_wins, "Primitive": p3_wins}
                
                print(winner_dict)

if __name__ == "__main__":
        test_main()