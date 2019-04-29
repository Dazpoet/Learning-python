#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter
from tkinter import ttk, messagebox
from functools import partial

root = tkinter.Tk()

def create_game(n):
    if n == 1:
        create_game_1()
    elif n == 2:
        create_game_2()

def create_game_1():
    window = tkinter.Toplevel(root)
    window.title("Uppgift 1")
    def destroy_window():
        window.destroy()
    
    ttk.Button(window, text = "Push me!", command = destroy_window).grid(column = 0, row = 1, sticky = "S")
    ttk.Label(window, text = "Don't push the button").grid(column = 0, row = 0, sticky = "N")

    for child in window.winfo_children():
        child.grid_configure(padx = 20, pady = 5)

def create_game_2():
    window = tkinter.Toplevel()
    window.title("Uppgift 2")
    def destroy_window():
        window.destroy()
    
    ttk.Button(window, text = "Don't push me!", command = destroy_window).grid(column = 0, row = 1, sticky = "S")
    ttk.Label(window, text = "Push the button").grid(column = 0, row = 0, sticky = "N")

    for child in window.winfo_children():
        child.grid_configure(padx = 20, pady = 5)

def main():
    root.title("Testprogram")
    #root.geometry("480x360") #This shouldn't be needed once a textbox is added on the side with instructions

    #I keep seeing these, I hope they do something good
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0,weight=1)

    menu_frame = ttk.Frame(root)
    menu_frame.grid(column = 0, row = 0, sticky = "news")

    buttons = [("Uppgift 1","create_game_1"), ("Uppgift 2","create_game_2")]

    for index, button in enumerate(buttons):
        message = button[0]
        command = button[1]
        ttk.Button(menu_frame, text = message, command = partial(create_game, (index + 1))).grid(column = 0, row = index, sticky = "news")

    for child in menu_frame.winfo_children():
        child.grid_configure(padx = 20, pady = 10)

    root.mainloop()

if __name__ == "__main__":
    main()