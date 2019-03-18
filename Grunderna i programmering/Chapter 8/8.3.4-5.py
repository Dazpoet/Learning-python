#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#TODO: I would like each account to have an index for easy selection rather than having to print the entire name for each operation
    #Could this be done putting each account as it's own dictionary corresponding to an index key in the primary dictionary?
    #Something like ['1':['Accountname':'Sum']]
    #Could the index number be generated using something like len(dict.keys()+1) maybe to abstract it away from the user?
    #Need to figure out how to work on a dict inside a dict

import pickle
import time
import os

def welcome_text():
    print("Welcome to DAZ, Daz Accountmanagement Zone.\nIn this program you can keep track of your expenditures and savings.")

def account_status (account_dict): #Prints the accountname and amount of money in each account
    for i, j in account_dict.items():
        print(i, j)
        time.sleep(1)

def easter_egg(): #Easter egg for the initiated
    print ("\n\nYou found the magical Dazrulle!")
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
https://github.com/Dazpoet/Learning-python/issues and it will be removed with due haste.\n\n
""")

def print_accounts(account_dict):
    print("These are your current accounts:")
    for i in account_dict.keys():
        print(i)

def add_account(account_dict): #Is called to add another account, also checks if easter egg should be triggered
    try:
        name = input("What would you like the name of your new account to be?: ")
        if name == "daZ_poet":
            print("You've choosen a clearly superior accountname and will be rewarded!")
            easter_egg()
        
        value = float(input("How much money do you have in that account?: "))
        account_dict[name] = value
        print("You have added the account", name, "with the initial sum", value)
    except ValueError:
        print("Your values must be proper numbers using \".\" as the delimiter")
    
    return account_dict

def remove_account(account_dict): #Removes an account
    print_accounts(account_dict)
    try:
        name = input("Which account would you like to remove? ")
        del account_dict[name]
        print("Removed account", name)
    except KeyError:
        print("You must enter the name of an existing account")

    return account_dict

def withdraw_from_account(account_dict): #Let's the user withdraw from an account
    print_accounts(account_dict)
    try:
        name = input("Which account would you like to withdraw from? ")
        value = float(input("How much would you like to withdraw? "))
        account_dict[name] -= value
        print("You withdrew", value, "from account", name)
    except ValueError:
        print("Your values must be proper numbers using \".\" as the delimiter")
    except KeyError:
        print("You must enter the name of an existing account")
    
    return account_dict

def add_to_account(account_dict): #Let's the user add to an account
    print_accounts(account_dict)
    try:
        name = input("Which account would you like to add to? ")
        value = float(input("How much would you like to add? "))
        account_dict[name] += value
        print("You added", value, "to account", name)
    except ValueError:
        print("Your values must be proper numbers using \".\" as the delimiter")
    except KeyError:
        print("You must enter the name of an existing account")

    return account_dict

def user_choices():
    try:
        choice = int(input("""\nWhat would you like to do?\n
            1. See the status of your accounts\n
            2. Add to an account\n
            3. Withdraw from an account\n
            4. Add an account\n
            5. Remove an account\n
            6. Quit\n"""))
        return choice
    except ValueError:
        print("You must choose a valid option")

def main():
    welcome_text()

    #Check if user have saved data, else treat user as a new user
    try:
        accounts = pickle.load(open('accounts.p', 'rb'))
    except FileNotFoundError:
        print("\nIt seems we have no data on your accounts, please answer the following questions to create your first account")
        accounts = {}
        accounts = add_account(accounts)
    
    while True:
        #Ask what the user would like to do
        choice = user_choices()
    
        #Perform the requested operation
        if choice == 1:
            account_status(accounts)
        elif choice == 2:
            accounts = add_to_account(accounts)
        elif choice == 3:
            accounts = withdraw_from_account(accounts)
        elif choice == 4:
            accounts = add_account(accounts)
        elif choice == 5:
            accounts = remove_account(accounts)
        elif choice == 6:
            #Check if the user has any accounts, if so save them, if not make sure to treat next start as a first time
            #TODO: See if this could be done by having a TRUE/FALSE switch saved in a file instead to avoid OS specific problems
            if len(accounts) < 1 and os.path.isfile("accounts.p"):
                os.remove("accounts.p")
            else:
                pickle.dump(accounts,open('accounts.p','wb'))
            quit()
        else:
            print("\nYou must choose one of the options 1 through 6.")

main()