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

def user_input(): #We break this into its own function as to not bloat main with exception-catching
    values = []
    try:
        start = int(input("Vilken siffra vill du att ditt spann ska börja på?: "))
        stop = int(input("Vilken siffra vill du att ditt spann ska sluta på?: "))+1 #Add 1 to the user input so we're not off by one in the games randomint call
        
        if start > stop:
            print("Startvärdet måste vara mindre än stoppvärdet")
        else:
            values.append(start)
            values.append(stop)
        
        return values
    except ValueError:
        print("Du måste ange heltal, annars fungerar inte spelet.")
        quit()

def number_game(first_number,last_number): #This is the actual game, we call this and supply the range we want to randomize between
    CORRECT_ANSWER = random.randint(first_number,last_number)
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
                    return guess_counter
                else:
                    print("\nRätt! Talet jag tänkte på var", CORRECT_ANSWER, "och du kom på det efter", guess_counter, "gissningar")
                    return guess_counter
        except ValueError:
            print("Du måste ange heltal")

def open_data_store(): #Check if there is any saved data and if so, return it, else return what we expect for a first time user
    try:
        savefile = pickle.load(open('data_store.p','rb'))
        return savefile
    except FileNotFoundError: #We assume that no saved data = first time user
        savefile = {'FIRST_TIME':True, 'HIGH_SCORE':100}
        return savefile
    except PermissionError:
        print("Det går inte att öppna din sparfil, försäkra dig om att du har läsrättigheter i mappen du kör ifrån och försök igen")
        quit()

def save_game(savefile): #This is its own function since it's called on twice and repeat code = bad code
    try:
        pickle.dump(savefile,open('data_store.p','wb'))
    except PermissionError:
        print("Det går inte att spara din progression, försäkra dig om att du har skrivrättigheter till mappen där spelet ligger")

def main_menu():
    counter = 0
    try:
        choice = int(input("Vad vill du göra?"
        "\n1. Spela standardspelet"
        "\n2. Spela men med mitt egenvalda spann"
        "\n3. Veta hur snabbt jag vunnit som snabbast"
        "\n4. Återställa mina snabbaste lösning till standardvärdet (100)"
        "\n5. Avsluta programmet\n"))
        return choice
    except ValueError:
        counter += 1
        if counter <= 5:
            print("Du måste ange ett existerande alternativ, det finns inga överraskningar här" + "."*(counter+1))
        elif counter > 5 and counter <= 10:
            for i in range(0,counter-5):
                    print("Ge dig, det finns inget här, du ödslar bara tid")
            else:
                print("Ok, ok... du får en ledtråd -> DET FINNS INGET HÄR!")

def compare_to_highscore(old_hs, new_score): #Does some logic, congratulates if higher, asks to try harder if lower, returns new best score
    if old_hs < new_score:
        print("Tyvärr slog du inte ditt gamla rekord på", old_hs, "gissningar. Bättre lycka nästa gång!")
        return old_hs
    else:
        print("Grattis! Du har slagit ditt gamla rekord", old_hs, "gissningar, med dina",new_score, "gissningar. Det är", old_hs - new_score, "färre gissningar. Försök igen och se om du kan slå det!")
        return new_score

def main():
    #Check if there is a savefile, else create one
    DATA_STORE = open_data_store()

    welcome_text(DATA_STORE['FIRST_TIME'])

    if DATA_STORE['FIRST_TIME'] == True: #First time users get thrown directly into the game and only get one run
        score = number_game(1,101)
        print("Du har nu klarat standardspelet, nästa gång du kör programmet kommer du kunna göra mer.")
        DATA_STORE['FIRST_TIME'] = False
        DATA_STORE['HIGH_SCORE'] = score
        save_game(DATA_STORE)        
        quit()
    else: #Users with saved data get access to the menu
        while True:
            choice = main_menu()
            if choice == 1:
                score = number_game(1,101)
                DATA_STORE['HIGH_SCORE'] = compare_to_highscore(DATA_STORE['HIGH_SCORE'], score)
            elif choice == 2:
                user_range = user_input()
                score = number_game(user_range.pop(0),user_range.pop()) #There just has to be a better way to do this, using a tuple?
                DATA_STORE['HIGH_SCORE'] = compare_to_highscore(DATA_STORE['HIGH_SCORE'], score)
            elif choice == 3:
                print("Din snabbaste lösningen var", DATA_STORE['HIGH_SCORE'], "gissningar")
            elif choice == 4:
                DATA_STORE['HIGH_SCORE'] = 100
                print("Snabbaste lösning återställd")
            elif choice == 5:
                save_game(DATA_STORE)
                quit() 

main()