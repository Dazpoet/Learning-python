#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Assignement:
#Create an implementation of the game "Gissa mitt tal" where the user is
#tasked with finding a random number between 1-100
#Use try-except to catch errors

import pickle
import random
import sys

def welcome_text(isfirst): #We call on this to welcome the user, if its their first time we inform them about progression
    print("Välkommen till spelet 'Gissa mitt tal'"
        "\nDu kommer att få gissa vilket tal jag tänker på. Talet är som standard mellan 1 och 100."
        "\nNär du gissar kommer jag att berätta om svaret är högre eller lägre än det du gissat"
        "\nFörsök att lista ut numret på så få gissnigar som möjligt")
    if isfirst:
        print("\nNär du klarat utmaningen en gång kommer det finnas fler möjligheter.")
    else:
        print("\nVälj hur du vill spela ur menyn.")

def easter_egg(): #Easter egg for the initiated
    print ("\n\nDu hittade den magiska Dazrullen!")
    print("""              _
  .--""--.___.._
 (  <__>  )     `-.
 |`--..--'|      <|
 |       :|       /
 |       :|--""-./
 `.__  __;' o!O
     ""     

------------------------------------------------
This ASCII art was fetched from http://www.ascii-art.de/ascii/t/toiletpaper.txt
Artist: Ojoshiro

If you are the copyright-holder of this art and would like it removed please open an issue at:
https://github.com/Dazpoet/Learning-python/issues and it will be removed with due haste.
""")

def user_input(): #We break this into its own function as to not bloat main with exception-catching
    values = []
    while True:
        try:
            start = int(input("Vilken siffra vill du att ditt spann ska börja på?: "))
            stop = int(input("Vilken siffra vill du att ditt spann ska sluta på?: "))

            if start > stop:
                print("Startvärdet måste vara mindre än stoppvärdet. Starta om och försök igen")
            else:
                values.append(start)
                values.append(stop)
                return values
        except ValueError:
            print("Du måste ange heltal, annars fungerar inte spelet.")
        except (EOFError, KeyboardInterrupt):
            sys.exit("\nAvslutar programmet")

def number_game(first_number,last_number): #This is the actual game, we call this and supply the range we want to randomize between
    CORRECT_ANSWER = random.randint(first_number,last_number)
    guess_counter = 0

    while True:
        try:
            guess = int(input("\nGissa på ett nummer så ska jag berätta om det är rätt eller ge dig en ledtråd: "))
            guess_counter += 1
            if guess > CORRECT_ANSWER:
                if guess_counter == 1:
                    print("\nTalet jag tänker på är lägre än", guess, "Du har gissat", guess_counter, "gång")
                else:
                    print("\nTalet jag tänker på är lägre än", guess, "Du har gissat", guess_counter, "gånger")
            elif guess < CORRECT_ANSWER:
                if guess_counter == 1:
                    print("\nTalet jag tänker på är högre än", guess, "Du har gissat", guess_counter, "gång")
                else:
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
        except (EOFError, KeyboardInterrupt):
            sys.exit("\nAvslutar programmet")

def open_data_store(): #Check if there is any saved data and if so, return it, else return what we expect for a first time user
    try:
        savefile = pickle.load(open('data_store.p','rb'))
        return savefile
    except FileNotFoundError: #We assume that no saved data = first time user
        savefile = {'FIRST_TIME':True, 'HIGH_SCORE':100}
        return savefile
    except PermissionError:
        print("Det går inte att öppna din sparfil, försäkra dig om att du har läsrättigheter i mappen du kör ifrån och försök igen")
        sys.exit(1)

def save_game(savefile): #This is its own function since it's called on twice and repeat code == bad code
    try:
        pickle.dump(savefile,open('data_store.p','wb'))
    except PermissionError:
        print("Det går inte att spara din progression, försäkra dig om att du har skrivrättigheter till mappen där spelet ligger")

def main_menu():
    counter = 0
    while True: #We add this loop so the counter will work
        try:
            choice = int(input("\nVad vill du göra?"
            "\n1. Spela standardspelet"
            "\n2. Spela men med mitt egenvalda spann"
            "\n3. Veta hur snabbt jag vunnit som snabbast"
            "\n4. Återställa mina snabbaste lösning till standardvärdet (100)"
            "\n5. Avsluta programmet\n"))
            return choice
        except ValueError: #The code below could be put into it's own function but I've chosen not to since I like toying with hiding things in errors
            counter += 1
            if counter <= 5:
                print("Du måste ange ett existerande alternativ, det finns inga överraskningar här" + "."*(counter+1))
            elif counter > 5 and counter <= 10:
                for i in range(0,counter-5):
                        print("Ge dig, det finns inget här, du ödslar bara tid")
                else:
                    print("Ok, ok... du får en ledtråd -> DET FINNS INGET HÄR!")
            elif counter == 15:
                easter_egg()
        except (EOFError, KeyboardInterrupt):
            sys.exit("\nAvslutar programmet")

def compare_to_highscore(old_hs, new_score): #Does some logic, congratulates if higher, asks to try harder if lower, returns new best score
    if old_hs < new_score:
        print("Tyvärr slog du inte ditt gamla rekord på", old_hs, "gissningar. Bättre lycka nästa gång!")
        return old_hs
    elif new_score == 1:
        print("Eftersom det nu är omöjligt att slå ditt rekord av", new_score, "gissning så rekommenderar jag att du nollställer räknaren och utmanar dig själv med svårare spann")
    elif old_hs == new_score:
        print("Du tangerade ditt gamla rekord", old_hs, "gissningar. Försök igen för att se om du kan slå det också.")
        return old_hs
    else:
        print("Grattis! Du har slagit ditt gamla rekord", old_hs, "gissningar, med dina",new_score, "gissningar. Det är", old_hs - new_score, "färre gissningar. Försök igen och se om du kan slå det!")
        return new_score

def main():
    DATA_STORE = open_data_store()

    welcome_text(DATA_STORE['FIRST_TIME'])

    if DATA_STORE['FIRST_TIME'] == True: #First time users get thrown directly into the game and only get one run
        score = number_game(1,101)
        DATA_STORE['FIRST_TIME'] = False
        DATA_STORE['HIGH_SCORE'] = score
        save_game(DATA_STORE)
        #Restart to make sure we catch potential erros with the savefile before the user has a lot of progress to lose
        sys.exit("Du har nu klarat standardspelet, nästa gång du kör programmet kommer du kunna göra mer.")
    else: #Users with saved data get access to the menu
        while True:
            choice = main_menu() #The menu itself is sectioned of into a function
            if choice == 1: #The following choices are kept in main for better readability
                score = number_game(1,100)
                DATA_STORE['HIGH_SCORE'] = compare_to_highscore(DATA_STORE['HIGH_SCORE'], score)
            elif choice == 2:
                user_range = user_input()
                score = number_game(user_range.pop(0),user_range.pop()) #There just has to be a better way to do this, using a tuple?
                DATA_STORE['HIGH_SCORE'] = compare_to_highscore(DATA_STORE['HIGH_SCORE'], score)
            elif choice == 3:
                print("Din snabbaste lösningen var", DATA_STORE['HIGH_SCORE'], "gissningar")
            elif choice == 4:
                DATA_STORE['HIGH_SCORE'] = 100
                print("Snabbaste lösning återställd till 100")
            elif choice == 5:
                save_game(DATA_STORE)
                sys.exit(0)

main()