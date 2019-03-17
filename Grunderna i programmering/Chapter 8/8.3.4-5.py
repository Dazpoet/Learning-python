#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Assignement
#Make a program that keeps track of 3 different bank accounts based on user input
#The account balances must be saved between sessions
#Use try-except to catch potential errors

#We will use pickle to handle the files
import pickle
import time

def welcome_text():
    print("Welcome to DAZ, Daz Accountmanagement Zone.\nIn this program you can keep track of your expenditures and savings.")

def account_status (account_dict):
    for i, j in account_dict.items():
        print(i, j)
        time.sleep(1)

def add_account(account_dict):
    name = input("What would you like the name of your account to be?: ")
    value = float(input("How much money do you have in that account?: "))
    account_dict[name] = value
    print("You have added the account", name, "with the initial sum", value)
    return account_dict

def remove_account(account_dict):
    pass

def withdraw_from_account(account_dict):
    print("These are your current accounts:")
    for i in account_dict.keys():
        print(i)

    name = input("Which account would you like to withdraw from? ")
    value = float(input("How much would you like to withdraw? "))
    account_dict[name] -= value
    print("You withdrew", value, "from account", name)

    return account_dict

def add_to_account(account_dict):
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
        elif choice == 6:
            pickle.dump(accounts,open('accounts.p','wb'))
            quit()
        else:
            print("\nYou must choose one of the options 1 through 6.")


main()
