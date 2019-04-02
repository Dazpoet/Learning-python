#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Mission: Using the functions from the console version, create a GUI application that performs a few basic operations

import TreA_WillhelmRendahl as primemodule
from tkinter import *
from tkinter import ttk

def do_magic():
    user_input = int(first_number.get()), int(last_number.get() + 1)
    primes.set(primemodule.sieve_of_eratosthenes(user_input))

#Create the alpha and the omega, root as the nerds call it
root = Tk()
root.title("Optimus") #The best prime

#These tell the window to adapt to sizechanges based on input, I think
root.columnconfigure(0, weight=1)
root.rowconfigure(0,weight=1)

#create the primary frame we'll work in
main_frame = ttk.Frame(root)
main_frame.grid(column=0, row=0, sticky=(N, W, S, E))

#We need some variables which will be called upon to send information into functions
first_number = IntVar()
last_number = IntVar()

#Need a variable which will show information to the user
primes = StringVar()

#Label explaing the first field
ttk.Label(main_frame, text="Starting Number").grid(column=1, row=1, sticky=W)
#Entry field for the first number and it's placement
first_number_entry = ttk.Entry(main_frame,width=1, textvariable=first_number)
first_number_entry.grid(column=1, row=2, sticky=W)

#Label explaining the second field
ttk.Label(main_frame, text="Last Number").grid(column=2, row=1, sticky=W)
#Entry field for the last number and it's placement
last_number_entry = ttk.Entry(main_frame, width=2, textvariable=last_number)
last_number_entry.grid(column=2, row=2, sticky=W)

ttk.Label(main_frame, textvariable=primes).grid(column=1, row=3, columnspan=2)
ttk.Button(main_frame, text="Find the primes", command=do_magic).grid(column=3, row=3, sticky=E)

for child in main_frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()