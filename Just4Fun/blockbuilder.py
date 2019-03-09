#!/usr/bin/env python3

#This is an attempt at creating a small pseudocode like experience for parts of a citybuilder in e.g. Minecraft for education
#The goal is to generate different kinds of houses on different streets
#This program will simply print what kind of house and on which street it is placed while a real implementation would acctually
#contain code which let robots/agents build said houses

#What I want
#A streetbuilder that constructs each street with random houses
#A district builder that constructs districts with multiple streets
#I would like each district to have a post office, a police station and a health care facility but no more than one of each
#A city to have 5 districts with user chosen names
#A city plan to printed as the end-product
#The user to choose a city name

import random

house_types = ['Red house', 'Blue House', 'Yellow House', 'Purple House', 'Pink House' ]
special_house_types = ['Police Station', 'Health Care', 'Post Office']

def housebuilder(): #This will choose a random house and print what kind it is. In the real implementation this would construct a house
    pass

def streetbuilder(): #This will construct a street
    pass

def districtbuilder(): #This will construct a district and contain logic for the special houses
    pass

def city_plan(): #This will print the finished city plan
    pass

def main(): #This is our citybuilder and will mostly be a bunch of loops which ends with a printing of the cityplan
    city_name = input("What would you like to call your city?: ")
    
    district_names = []
    number_of_districts = 5

    while len(district_names) < number_of_districts:
        district_name = input("Name one of your districts: ")
        district_names.append(district_name)
        print("Good choice! I'm sure that " + str(district_name) + " will be a fine district to live in.")
    
    print("Your districts are:")
    while not number_of_districts == -1:
        print(district_names[number_of_districts - 1])
        number_of_districts -= 1

main()