#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#TODO: All indata, utdata windows could probably be done in an OOP manner to shorten the code

import tkinter
import geometric_shapes
from tkinter import ttk, messagebox
from functools import partial

root = tkinter.Tk()

def choose_shape(n):
    if n == "Kvadrat":
        calculate_square()

def calculate_rectangle():
    pass

def calculate_circle():
    pass

def calculate_isoceles_triangle():
    pass

def calculate_square():
    def create_object():
        #Massage the data so the object can be created
        #TODO: Figure out if this can be done in a loop instead
        try:
            l = float(square_side.get())
        except:
            l = None
        try:
            P = float(square_perimeter.get())
        except:
            P = None
        try:
            A = float(square_area.get())
        except:
            A = None
        
        #Create the square object based on the rectangle class
        square = geometric_shapes.Rectangle(l=l, P=P, A=A)
        
        square_input_window.destroy()

        return square

    def inform_user():
        square = create_object()
        #TODO: Add drawing and stuff here
        #TODO: Create function that generate the needed text

        #Create the window that displays the square and calculations to the user
        square_window = tkinter.Toplevel(root)
        
        #Set the windows parameters
        square_window.title("Utdata")
        square_window.geometry("800x380+250+125")

        #Create the drawing canvas and set its parameters
        square_canvas = tkinter.Canvas(square_window,width=340, height=340, relief="sunken", bg="white")
        square_canvas.grid(column=0, row=0, sticky="nw", padx=10, pady=20)

        #Create the square (rectangle)
        #Since all squares are similar we can hard-code this shape and it'll always work
        square_canvas.create_rectangle(80,80,260,260,width=2,fill="red")

        #Create the widgets that display the sidelength
        square_side1_widget = tkinter.Label(square_canvas, text=square.length)
        square_side2_widget = tkinter.Label(square_canvas, text=square.length)

        #Do some mathmagical things to make the informations position mostly correct
        #Works for numbers up to 6 digits before they move out of scope
        #TODO: Add logic to make this behave differently when there is more than 6 digits
        x1 = 70 - 5*len(str(square.length))

        #Define the widgets position inside the canvas
        square_canvas.create_window(x1,170,window=square_side1_widget)
        square_canvas.create_window(170,280,window=square_side2_widget)

        #Configure the text
        for child in [square_side1_widget, square_side2_widget]:
            child.config(font = ("Arial", 18))
            child.config(fg="white",bg="black")


    def square_gui(information_window):
        
        information_window.title("Indata")

        #Create labels and entries for each datapoint we want to collect
        ttk.Label(information_window,text="Sidlängd").grid(column=1, row=1, sticky="w")
        ttk.Entry(information_window, width=7,textvariable=square_side).grid(column=2, row=1)
        ttk.Label(information_window,text="l.e.").grid(column=3, row=1, sticky="E")
        
        ttk.Label(information_window,text="Omkrets").grid(column=1, row=2, sticky="w")
        ttk.Entry(information_window, width=7,textvariable=square_perimeter).grid(column=2, row=2)
        ttk.Label(information_window,text="l.e.").grid(column=3, row=2, sticky="E")

        ttk.Label(information_window,text="Area").grid(column=1, row=3, sticky="w")
        ttk.Entry(information_window, width=7,textvariable=square_area).grid(column=2, row=3)
        ttk.Label(information_window,text="a.e.").grid(column=3, row=3, sticky="E")

        ttk.Button(information_window,text="Beräkna",command=inform_user).grid(column=2, row=4)

        #Make the GUI nice and roomy
        for child in information_window.winfo_children():
            child.grid_configure(padx=20,pady=20)

    #Add variables for entry and running logic
    square_side = tkinter.StringVar()
    square_area = tkinter.StringVar()
    square_perimeter = tkinter.StringVar()

    #Create the input window
    square_input_window = tkinter.Toplevel(root)

    #Run the GUI
    square_gui(square_input_window)

def build_gui():
    root.title("Wille och Mackans geometriprogram")
    root.geometry("800x380+250+125")

    button_frame = ttk.Frame(root)
    button_frame.grid(column = 0, row = 0, sticky = "nw")

    buttons = ["Kvadrat",
            "Kub",
            "Rektangel",
            "Rätblock",
            "Cirkel",
            "Sfär",
            "Romb",
            "Parallellogram",
            "Triangel"
            ]

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