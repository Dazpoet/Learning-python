#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Assignement
#Make a program that keeps track of 3 different bank accounts based on user input
#The account balances must be saved between sessions
    #Use pickle for file handling
#Use try-except to catch potential errors
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

def add_account(account_dict): #Is called to add another account
    name = input("What would you like the name of your account to be?: ")
    value = float(input("How much money do you have in that account?: "))
    account_dict[name] = value
    print("You have added the account", name, "with the initial sum", value)
    
    return account_dict

def remove_account(account_dict):
    print("These are your current accounts:")
    for i in account_dict.keys():
        print(i)

    name = input("Which account would you like to remove? ")
    del account_dict[name]
    print("Removed account", name)
    
    return account_dict

def withdraw_from_account(account_dict): #Let's the user withdraw from an account
    print("These are your current accounts:")
    for i in account_dict.keys():
        print(i)

    name = input("Which account would you like to withdraw from? ")
    value = float(input("How much would you like to withdraw? "))
    account_dict[name] -= value
    print("You withdrew", value, "from account", name)

    return account_dict

def add_to_account(account_dict): #Let's the user add to an account
    print("These are your current accounts:")
    for i in account_dict.keys():
        print(i)

    name = input("Which account would you like to add to? ")
    value = float(input("How much would you like to add? "))
    account_dict[name] += value
    print("You added", value, "to account", name)

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
            #Check if the user has any accounts, if so save them, if not make sure they will be treated as a new user on the next startup
            if len(accounts) < 1 and os.path.isfile(accounts.p):
                os.remove(accounts.p)
            else:
                pickle.dump(accounts,open('accounts.p','wb'))
            quit()
        else:
            print("\nYou must choose one of the options 1 through 6.")

main()