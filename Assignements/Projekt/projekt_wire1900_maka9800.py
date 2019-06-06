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
    elif n == "Rektangel":
        calculate_rectangle()
    elif n == "Triangel":
        calculate_isoceles_triangle()
    elif n == "Cirkel":
        calculate_circle()

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
    
    def square_generate_text(square):
        def generate_t2():
            if square_side.get():
                return f"L = Längd = {round(square.length, 2)} l.e.\n"
            else:
                return ""

        def generate_t3():
            if square_perimeter.get():
                return f"O = Omkrets = {round(square.perimeter, 2)} l.e.\n\n"
            else:
                return""
        
        def generate_t4():
            if square_area.get():
                return f"A = Area = {round(square.area, 2)} a.e.\n\n"
            else:
                return""
        
        def generate_t6():
            if not square_side.get() and not square_area.get():
                return f"s = {round(square.perimeter, 2)} / 4 = {round(square.length, 2)} l.e."
            elif not square_side.get() and not square_perimeter.get():
                return f"s = \u221A{round(square.area, 2)} = {round(square.length, 2)} l.e."
            elif not square_side.get():
                return f"s = {square.perimeter} / 4 = {round(square.length, 2)} l.e."
            else:
                return ""
        
        t_1 = "Värden\n\n"
        
        t_2 = generate_t2()
    
        t_3 = generate_t3()
    
        t_4 = generate_t4()
        
        t_5 = "Formler\n\n"\
            "O = Omkrets = 4 * s = s + s + s + s\n"\
            "A = Area = s\u00b2 = s * s\n\n"\
            "s = sidlängd\n\n"\
            "s = Omkrets/4\n"\
            "eller\n"\
            "s = \u221AArea\n\n"\
            "Beräkning\n\n"\
            f"O = 4 * {round(square.length, 2)} = {round(square.perimeter, 2)} l.e.\n\n"\
            f"A = {round(square.length, 2)} * {round(square.length, 2)} = {round(square.area, 2)} a.e.\n\n"

        t_6 = generate_t6()

        losning = t_1 + t_2 + t_3 + t_4 + t_5 + t_6

        return losning

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
        square_side1_widget = tkinter.Label(square_canvas, text=round(square.length, 2))
        square_side2_widget = tkinter.Label(square_canvas, text=round(square.length, 2))

        #Do some mathmagical things to make the informations position mostly correct
        #Works for numbers up to 6 digits before they move out of scope
        #TODO: Add logic to make this behave differently when there is more than 6 digits
        x1 = 70 - 5*len(str(square.length))

        #Define the widgets position inside the canvas
        square_canvas.create_window(x1,170,window=square_side1_widget)
        square_canvas.create_window(170,280,window=square_side2_widget)

        #Configure the textwidgets
        for child in [square_side1_widget, square_side2_widget]:
            child.config(font = ("Arial", 18))
            child.config(fg="white",bg="black")
        
        #Generate the informational text with solution to the problem
        square_solution = square_generate_text(square)

        #Create a label to put the solution into and configure it
        square_losning = ttk.Label(square_window, text = square_solution)
        square_losning.config(font = ("Arial", 12), anchor = "n", justify = "left", width = 40)
        square_losning.config(background = "white", relief = "sunken", wraplength = 410)
        square_losning.grid(column = 1, row = 0, sticky = "news", padx = 10, pady = 20)

    def square_gui(information_window): #Creates a gui for input data and collection of said data
        
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