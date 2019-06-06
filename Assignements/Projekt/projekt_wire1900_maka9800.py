#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter
import geometric_shapes
from tkinter import ttk, messagebox
from functools import partial

root = tkinter.Tk()

def choose_shape(n):
    if n == "Kvadrat":
        calculate_square()

def calculate_square():
    def create_object():
        #Massage the data so the object can be created
        #TODO: Figure out if this can be done in a loop instead
        try:
            l = float(side.get())
        except:
            l = None
        try:
            P = float(perimeter.get())
        except:
            P = None
        try:
            A = float(area.get())
        except:
            A = None
        
        #Create the square object based on the rectangle class
        square = geometric_shapes.Rectangle(l=l, P=P, A=A)
        
        information_window.destroy()

        return square

    def inform_user():
        square = create_object()
        print(vars(square)) #This is only for logging purposes and should be removed once we get further
        #TODO: Add drawing and stuff here
        #TODO: Create function that generate the needed text

    def square_gui(information_window):
        
        information_window.title("Mata in information")

        #Create labels and entries for each datapoint we want to collect
        ttk.Label(information_window,text="Sidlängd").grid(column=1, row=1, sticky="w")
        ttk.Entry(information_window, width=7,textvariable=side).grid(column=2, row=1)
        ttk.Label(information_window,text="l.e.").grid(column=3, row=1, sticky="E")
        
        ttk.Label(information_window,text="Omkrets").grid(column=1, row=2, sticky="w")
        ttk.Entry(information_window, width=7,textvariable=perimeter).grid(column=2, row=2)
        ttk.Label(information_window,text="l.e.").grid(column=3, row=2, sticky="E")

        ttk.Label(information_window,text="Area").grid(column=1, row=3, sticky="w")
        ttk.Entry(information_window, width=7,textvariable=area).grid(column=2, row=3)
        ttk.Label(information_window,text="a.e.").grid(column=3, row=3, sticky="E")

        ttk.Button(information_window,text="Beräkna",command=inform_user).grid(column=2, row=4)

        for child in information_window.winfo_children():
            child.grid_configure(padx=20,pady=20)


    side = tkinter.StringVar()
    area = tkinter.StringVar()
    perimeter = tkinter.StringVar()

    information_window = tkinter.Toplevel(root)

    square_gui(information_window)

def build_gui():
    root.title("Wille och Mackans geometriprogram")
    root.geometry("800x380+250+125")

    button_frame = ttk.Frame(root)
    button_frame.grid(column = 0, row = 0, sticky = "nw")

    buttons = ["Kvadrat", "Kub", "Rektangel", "Rätblock", "Cirkel", "Sfär", "Romb", "Parallellogram", "Liksidig triangel"]

    for index, button in enumerate(buttons):
        message = button
        #Put the buttons next to eachother in two seperate columns
        if index % 2 == 0:
            ttk.Button(button_frame, text = message, command = partial(choose_shape, (button))).grid(column = 0, row = index, sticky = "news")
        else:
            ttk.Button(button_frame, text = message, command = partial(choose_shape, (button))).grid(column = 1, row = (index - 1), sticky = "news")

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