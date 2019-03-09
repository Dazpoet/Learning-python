#!/usr/bin/env python3

#This is an attempt at creating a small pseudocode like experience for parts of a citybuilder in e.g. Minecraft for education
#The goal is to generate different kinds of houses on different streets
#This program will simply print what kind of house and on which street it is placed while a real implementation would acctually
#contain code which let robots/agents build said houses

#What I want
#A streetbuilder that constructs each street with random houses
#A district builder that constructs districts with multiple streets
#A city to have 5 districts with user chosen names
#A city plan to printed as the end-product
#The user to choose a city name
#TODO: I would like each district to have a post office, a police station and a health care facility but no more than one of each
#TODO: catch exceptions

import random
import time

def house_builder(): #This will choose a random house and print what kind it is. In the real implementation this would construct a house
    normal_house_types = ['Red house', 'Blue House', 'Yellow House', 'Purple House', 'Pink House' ]
    index = random.randint(0,(len(normal_house_types) - 1))
    print(normal_house_types[index])

def street_builder(street): #This will construct a street
    number_of_houses = 5
    while not number_of_houses == 0:
        house_builder()
        number_of_houses -= 1

    print()

def district_builder(district): #This will construct a district

    street_names = ['1st St', '2nd St', '3rd St', '4th St', '5th St']

    for street in street_names:
        print(str(street) + " contains the following houses: ")
        street_builder(street)
        time.sleep(2)

def main(): #This is our citybuilder and will mostly be a bunch of loops which ends with a printing of the cityplan
    city_name = input("What would you like to call your city?: ")
    
    district_names = []
    try:
        number_of_districts = int(input("How many districts would you like your city to have? "))
    except ValueError:
        print("Your number must be an integer")
        quit()

    while len(district_names) < number_of_districts: #We name our districts TODO: Provide a nice counter with how many we have done/have left to do
        district_name = input("Name one of your districts: ")
        district_names.append(district_name)
        print("Good choice! I'm sure that " + str(district_name) + " will be a fine district to live in.")
    
    print("Your City " + str(city_name) + " will have the districts:")
    while not number_of_districts == 0:
        print(district_names[number_of_districts - 1])
        number_of_districts -= 1
    time.sleep(2)
    print()

    for district in district_names:
        print("Constructing the district " + str(district) + " in city " + str(city_name))
        print()
        print(str(district))
        district_builder(district)
        time.sleep(2)
        print()


main()