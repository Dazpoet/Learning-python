#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Assignement:
#Create an implementation of the game "Gissa mitt tal" where the user is
#tasked with finding a random number between 1-100
#TODO: Try what happens when first_number > last_number in number_game, does it break?
#TODO: See if a high-score board can be added which shows the lowest number of guesses ever needed

import pickle
import random

def welcome_text(isfirst): #We call on this to welcome the user, if its their first time we inform them about progression
    print("Välkommen till spelet 'Gissa mitt tal'"
        "\nDu kommer att få gissa vilket tal jag tänker på. Talet är som standard mellan 1 och 100."
        "\nNär du gissar kommer jag att berätta om svaret är högre eller lägre än det du gissat"
        "\nFörsök att lista ut numret på så få gissnigar som möjligt")
    if isfirst:
        print("\nNär du klarat utmaningen en gång kommer det finnas fler möjligheter.")
    else:
        print("\nVälj hur du vill spela ur menyn.")

def number_game(first_number,last_number, best_score): #This is the actual game, we call this and supply the range we want to randomize between
    CORRECT_ANSWER = random.randint(first_number,last_number) #Lastnumber must be e.g. 101 when the user selects 100, fix that in input
    guess_counter = 0

    while True:
        try:
            guess = int(input("\nGissa på ett nummer så ska jag berätta om det är rätt eller ge dig en ledtråd: "))
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
    counter = 0
        try:
            choice = int(input(""))
        except ValueError:
            counter += 1
            if counter =< 5:
                print("Du måste ange ett existerande alternativ, det finns inga överraskningar här" + "."*(counter+1))
            elif counter > 5 and counter =< 10:
                for i in range(0,counter-5):
                    print("Ge dig, det finns inget här, du ödslar bara tid")
            else:
                print("Ok, ok... du får en ledtråd -> DET FINNS INGET HÄR!")

def main():
    try: #Check for a savefile
        DATA_STORE = pickle.load(open('data_store.p','rb'))
    except FileNotFoundError: #We assume that no saved data = first time user
        DATA_STORE = {'FIRST_TIME':True, 'HIGH_SCORE':None}

    #Import the needed data from the data store
    FIRST_TIME = DATA_STORE['FIRST_TIME']
    HIGH_SCORE = DATA_STORE['HIGH_SCORE']

    welcome_text(FIRST_TIME)

    if FIRST_TIME == True: #First time users get thrown directly into the game and only get one run
        number_game(1,101)
        print("Du har nu klarat standardspelet, nästa gång du kör programmet kommer du kunna göra mer...")
        DATA_STORE['FIRST_TIME'] = False
        pickle.dump(DATA_STORE,open('data_store.p','wb'))
        quit()
    else: #Users with saved data get access to the menu
        while True:
            choice = main_menu()

main()