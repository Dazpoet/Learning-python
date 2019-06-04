#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter
import geometric_shapes
from tkinter import ttk, messagebox
from functools import partial

root = tkinter.Tk()

def create_game(n):
    if n == 1:
        create_game_1()
    elif n == 2:
        create_game_2()
    elif n == "Kvadrat":
        calculate_square()

def calculate_square():
    def create_object():
        try:
            l = int(side.get())
        except:
            l = None
        
        try:
            A = int(area.get())
        except:
            A = None

        try:
            P = int(perimeter.get())
        except:
            P = None

        square=geometric_shapes.Rectangle(l=l, A=A, P=P)

        information_window.destroy()

        return square

    def inform_user():
        square = create_object()
        print(vars(square))



    side = tkinter.StringVar()
    area = tkinter.StringVar()
    perimeter = tkinter.StringVar()

    information_window = tkinter.Toplevel(root)
    information_window.title("Mata in information")

    ttk.Label(information_window,text="Sidlängd").grid(column=1, row=1, sticky="w")
    ttk.Label(information_window,text="Area").grid(column=1, row=2, sticky="w")
    ttk.Label(information_window,text="Omkrets").grid(column=1, row=3, sticky="w")

    ttk.Label(information_window,text="l.e.").grid(column=3, row=1, sticky="E")
    ttk.Label(information_window,text="a.e.").grid(column=3, row=2, sticky="E")
    ttk.Label(information_window,text="l.e.").grid(column=3, row=3, sticky="E")

    side_entry = ttk.Entry(information_window, width=7,textvariable=side).grid(column=2, row=1)
    area_entry = ttk.Entry(information_window, width=7,textvariable=area).grid(column=2, row=2)
    perimeter_entry = ttk.Entry(information_window, width=7,textvariable=perimeter).grid(column=2, row=3)

    ttk.Button(information_window,text="Beräkna",command=inform_user).grid(column=2, row=4)

    for child in information_window.winfo_children():
        child.grid_configure(padx=20,pady=20)

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
    root.title("Wille och Mackans geometriprogram")
    root.geometry("800x380+250+125")
    #I keep seeing these, I hope they do something good, more info here https://stackoverflow.com/questions/45847313/what-does-weight-do-in-tkinter
    #root.columnconfigure(0, weight=1)
    #root.rowconfigure(0,weight=1)

    button_frame = ttk.Frame(root)
    button_frame.grid(column = 0, row = 0, sticky = "nw")

    buttons = ["Kvadrat", "Kub", "Rektangel", "Rätblock", "Cirkel", "Sfär", "Romb", "Parallellogram", "Liksidig triangel"]

    for index, button in enumerate(buttons):
        message = button
        #Put the buttons next to eachother in two seperate columns
        if index % 2 == 0:
            ttk.Button(button_frame, text = message, command = partial(create_game, (button))).grid(column = 0, row = index, sticky = "news")
        else:
            ttk.Button(button_frame, text = message, command = partial(create_game, (index + 1))).grid(column = 1, row = (index - 1), sticky = "news")

    text = "I detta program lär du dig om geometriska former\n\n"\
        "Programmet tar fram information om olika geometriska former baserat på information du redan har.\n\n"\
        "Ett exempel är att du kan få reda på en kvadrats omkrets genom att mata in dess area.\n\n"\
        "Programmet använder sig av längdenheter (l.e.) och areaenheter (a.e.) i sina beräkningar.\n\n"\
        "Klicka på en av knapparna till vänster för att fylla i information du har"

    info_text = ttk.Label(button_frame, text = text)
    info_text.config(font = ("Arial", 12), anchor = "n", justify = "left", width = 45)
    info_text.config(background = "white", relief = "sunken", wraplength = 410)
    info_text.grid(column = 2, row = 0, rowspan = 10, sticky = "news")

    for child in button_frame.winfo_children():
        child.grid_configure(padx = 20, pady = 10)

def main():
    build_gui()
    
    root.mainloop()

if __name__ == "__main__":
    main()