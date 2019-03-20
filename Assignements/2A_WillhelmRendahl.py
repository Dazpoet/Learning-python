#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Assignement:
#Create an implementation of the game "Gissa mitt tal" where the user is
#tasked with finding a random number between 1-100
#TODO: Try what happens when first_number > last_number in number_game, does it break?

import pickle
import random

def welcome_text(isfirst):
    print("Välkommen till spelet 'Gissa mitt tal'"
        "\nDu kommer att få gissa vilket tal jag tänker på. Talet är som standard mellan 1 och 100."
        "\nNär du gissar kommer jag att berätta om svaret är högre eller lägre än det du gissat"
        "\nFörsök att lista ut numret på så få gissnigar som möjligt")
    if isfirst:
        print("\nNär du klarat utmaningen en gång kommer det finnas fler möjligheter.")
    else:
        print("\nVälj hur du vill spela ur menyn.")

def number_game(first_number,last_number):
    CORRECT_ANSWER = random.randint(first_number,last_number) #Lastnumber must be e.g. 101 when the user selects 100, fix that in input
    guess_counter = 0

    while True:
        try:
            guess = int(input("\nGissa på ett nummer så ska jag berätta om det är rätt eller ge dig en ledtråd"))
            guess_counter += 1
            if guess > CORRECT_ANSWER:
                print("\nTalet jag tänker på är lägre än", guess, "Du har gissat", guess_counter, "gånger")
            elif guess < CORRECT_ANSWER:
                print("\nTalet jag tänker på är högre än", guess, "Du har gissat", guess_counter, "gånger")
            else:
                if guess_counter == 1:
                    print("\nDu måste ha fuskat! Jag tänkte på", CORRECT_ANSWER, "och du kom på det på första försöket. Är du en tankeläsare?")
                    break
                else:
                    print("\nRätt! Talet jag tänkte på var", CORRECT_ANSWER, "och du kom på det efter", guess_counter, "gisningar")
                    break
        except ValueError:
            print("Du måste ange heltal")
def main_menu():
    pass
    return None

def main():
    try:
        FIRST_TIME = pickle.load(open('first_time.p','rb')) #We check this to see if the user has unlocked the whole program
    except FileNotFoundError:
        FIRST_TIME = True

    welcome_text(FIRST_TIME)

    if FIRST_TIME == True:
        number_game(1,101)
        print("Du har nu klarat standardspelet, nästa gång du kör programmet kommer du kunna göra mer...")
        FIRST_TIME = False
        pickle.dump(FIRST_TIME,open('first_time.p','wb'))
    else:
        while True:
            choice = main_menu()

main()