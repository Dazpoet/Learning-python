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

def build_gui():
    root.title("Testprogram")
    root.geometry("800x380+250+125") #This shouldn't be needed once a textbox is added on the side with instructions

    #I keep seeing these, I hope they do something good, more info here https://stackoverflow.com/questions/45847313/what-does-weight-do-in-tkinter
    #root.columnconfigure(0, weight=1)
    #root.rowconfigure(0,weight=1)

    button_frame = ttk.Frame(root)
    button_frame.grid(column = 0, row = 0, sticky = "nw")

    #text_frame = ttk.Frame(root)
    #text_frame.grid(column = 2, sticky = "ne")

    #buttons = [("Uppgift 1","create_game_1"), ("Uppgift 2","create_game_2")]
    buttons = ["Kvadrat", "Kub", "Rektangel", "Rätblock", "Cirkel", "Sfär", "Romb", "Parallellogram", "Liksidig triangel"]

    for index, button in enumerate(buttons):
        message = button
        #Put the buttons next to eachother in two seperate columns
        if index % 2 == 0:
            ttk.Button(button_frame, text = message, command = partial(create_game, (index + 1))).grid(column = 0, row = index, sticky = "news")
        else:
            ttk.Button(button_frame, text = message, command = partial(create_game, (index + 1))).grid(column = 1, row = (index - 1), sticky = "news")

    text = "Wille och Mackans supercoola geometriprogram"

    info_text = ttk.Label(button_frame, text = text)
    info_text.config(font = ("Arial", 12), anchor = "n", justify = "left", width = 45)
    info_text.config(background = "white", relief = "sunken", wraplength = 500)
    info_text.grid(column = 2, row = 0, rowspan = 10, sticky = "news")

    for child in button_frame.winfo_children():
        child.grid_configure(padx = 20, pady = 10)

    #for child in text_frame.winfo_children():
    #    child.grid_configure(padx = 20, pady = 20)

def main():
    build_gui()
    
    root.mainloop()

if __name__ == "__main__":
    main()