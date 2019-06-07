#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#TODO: All indata, utdata windows could probably be done in an OOP manner to shorten the code
#TODO: Text generation logic could possibly be put into geometric_shapes.py and either ran on their own as functions or be added to the objects
#TODO: Reflect on function names and find a standard that is robust and works
#TODO: Figure out scrollbars

import tkinter
import geometric_shapes
import math
from tkinter import ttk, messagebox
from functools import partial

root = tkinter.Tk()

def choose_shape(n):
    def raise_promise():
        messagebox.showerror(title="Ej tillgänglig", message="Denna form är ännu inte färdigprogrammerad, kommer i nästa version!")

    if n == "Kvadrat":
        calculate_square()
    elif n == "Rektangel":
        calculate_rectangle()
    elif n == "Triangel":
        raise_promise()
    elif n == "Cirkel":
        calculate_circle()
    else:
        raise_promise()
        
def calculate_rectangle():
    def create_object():
        #Massage the data so the object can be created
        #TODO: Figure out if this can be done in a loop instead
        try:
            l = float(rectangle_length.get())
        except:
            l = None
        try:
            w = float(rectangle_width.get())
        except:
            w = None
        try:
            P = float(rectangle_perimeter.get())
        except:
            P = None
        try:
            A = float(rectangle_area.get())
        except:
            A = None
        
        #Create the rectangle object based on the rectangle class
        rectangle = geometric_shapes.Rectangle(l=l, w=w, P=P, A=A)
        
        rectangle_input_window.destroy()

        return rectangle
    
    def rectangle_generate_text(rectangle):
    #This function looks at the object and input from the user and generates a solution that only shows the pertinent information
        return "We are the knights that say ni"

    def find_rectangle_coordinates(rectangle):
        length = rectangle.length
        width = rectangle.width

        #To ensure that the rectangle fits within the given space (340x340) some calculations must be done
        #Building upon the square drawing and the fact that it was of an appropriate size we can extrapolate that a rectangle with diagonal < 255 pixels is a good fit
        #If the diagonal is less than 127 (approx half of the maximum) the rectangle will look very small
        #TODO: Remove the logging entries below once we're sure they aren't needed anymore
        is_calculating = True
        counter = 0
        while is_calculating:
            counter += 1
            print("Performing run: ", counter) #LOGGING ONLY
            diagonal = math.sqrt(length**2 + width**2)
            if diagonal > 127 and diagonal < 255:
                is_calculating = False
            elif diagonal < 127:
                length *= 2
                width *= 2
                print("Raising to: ", length, width) #LOGGING ONLY
            elif diagonal > 255:
                length /= 2
                width /= 2
                print("Lowering to: ", length, width)#LOGGING ONLY

        #The rectangle is always drawn from the point x1,y1 = 80,120 so we only need to find x2,y2 which is
        #x1 + length, y1 + width

        x2 = 80 + length
        y2 = 120 + width

        return x2, y2

    def inform_user():
        rectangle = create_object()

        #Create the window that displays the rectangle and calculations to the user
        rectangle_window = tkinter.Toplevel(root)
        
        #Set the windows parameters
        rectangle_window.title("Utdata")
        rectangle_window.geometry("800x380+250+125")

        #Create the drawing canvas and set its parameters
        rectangle_canvas = tkinter.Canvas(rectangle_window,width=340, height=340, relief="sunken", bg="white")
        rectangle_canvas.grid(column=0, row=0, sticky="nw", padx=10, pady=20)

        #Since rectangles come in different shapes we need to calculate the correct coordinates
        rectangle_coordinates = find_rectangle_coordinates(rectangle)

        #Create the rectangle
        rectangle_canvas.create_rectangle(80,120,rectangle_coordinates[0],rectangle_coordinates[1],width=2,fill="red")

        #Create the widgets that display the sidelength
        rectangle_length_widget = tkinter.Label(rectangle_canvas, text=round(rectangle.length, 2))
        rectangle_width_widget = tkinter.Label(rectangle_canvas, text=round(rectangle.width, 2))

        #Do some mathmagical things to make the informations position mostly correct
        #Works for numbers up to 6 digits before they move out of scope
        #TODO: Add logic to make this behave differently when there is more than 6 digits
        x1 = 70 - 5*len(str(rectangle.length))

        #Define the widgets position inside the canvas
        rectangle_canvas.create_window(x1,(120 + ((rectangle_coordinates[1]-120)/2)),window=rectangle_width_widget)
        rectangle_canvas.create_window(80+((rectangle_coordinates[0]-80)/2),(rectangle_coordinates[1]+16),window=rectangle_length_widget)


        #Configure the textwidgets
        for child in [rectangle_length_widget, rectangle_width_widget]:
            child.config(font = ("Arial", 14))
            child.config(fg="white",bg="black")
        
        #Generate the informational text with solution to the problem
        rectangle_solution = rectangle_generate_text(rectangle)

        #Create a label to put the solution into and configure it
        rectangle_losning = ttk.Label(rectangle_window, text = rectangle_solution)
        rectangle_losning.config(font = ("Arial", 11), anchor = "nw", justify = "left", width = 45)
        rectangle_losning.config(background = "white", relief = "sunken", wraplength = 410)
        rectangle_losning.grid(column = 1, row = 0, sticky = "news", padx = 10, pady = 10)

    def rectangle_gui(information_window): #Creates a gui for input data and collection of said data
        
        information_window.title("Indata")

        #Create labels and entries for each datapoint we want to collect
        #rectangle_entry is a special case since we want to set focus to it
        ttk.Label(information_window,text="Bas").grid(column=1, row=1, sticky="w")
        rectangle_entry = ttk.Entry(information_window, width=7,textvariable=rectangle_length)
        rectangle_entry.focus_set()
        rectangle_entry.grid(column=2, row=1)
        ttk.Label(information_window,text="l.e.").grid(column=3, row=1, sticky="E")

        ttk.Label(information_window,text="Höjd").grid(column=1, row=2, sticky="w")
        ttk.Entry(information_window, width=7,textvariable=rectangle_width).grid(column=2, row=2)
        ttk.Label(information_window,text="l.e.").grid(column=3, row=2, sticky="E")

        ttk.Label(information_window,text="Omkrets").grid(column=1, row=3, sticky="w")
        ttk.Entry(information_window, width=7,textvariable=rectangle_perimeter).grid(column=2, row=3)
        ttk.Label(information_window,text="l.e.").grid(column=3, row=3, sticky="E")

        ttk.Label(information_window,text="Area").grid(column=1, row=4, sticky="w")
        ttk.Entry(information_window, width=7,textvariable=rectangle_area).grid(column=2, row=4)
        ttk.Label(information_window,text="a.e.").grid(column=3, row=4, sticky="E")

        #TODO: bind the enter key to trigger the button
        ttk.Button(information_window,text="Beräkna",command=inform_user).grid(column=2, row=5)

        #Make the GUI nice and roomy
        for child in information_window.winfo_children():
            child.grid_configure(padx=20,pady=20)

    #Add variables for entry and running logic
    rectangle_length = tkinter.StringVar()
    rectangle_width = tkinter.StringVar()
    rectangle_area = tkinter.StringVar()
    rectangle_perimeter = tkinter.StringVar()

    #Create the input window
    rectangle_input_window = tkinter.Toplevel(root)

    #Run the GUI
    rectangle_gui(rectangle_input_window)

def calculate_circle():
    def create_object():
        #Massage the data so the object can be created
        #TODO: Figure out if this can be done in a loop instead
        try:
            r = float(circle_radius.get())
        except:
            r = None
        try:
            C = float(circle_circumference.get())
        except:
            C = None
        try:
            A = float(circle_area.get())
        except:
            A = None
        
        #Create the circle object based on the rectangle class
        circle = geometric_shapes.Circle(r=r, C=C, A=A)
        
        circle_input_window.destroy()

        return circle
    
    def circle_generate_text(circle):    
        def generate_t2():
            if circle_radius.get():
                return f"\nr = radie = {round(circle.radius, 2)} l.e."
            else:
                return ""

        def generate_t3():
            if circle_circumference.get():
                return f"\nO = omkrets = {round(circle.circumference, 2)} l.e."
            else:
                return ""
            
        def generate_t4():
            if circle_area.get():
                return f"\nA = area = {round(circle.area, 2)} a.e."
            else:
                return ""

        def calculate_radius_t7():
            if not circle_radius and not circle_circumference:
                return f"\nr = \u221A({round(circle.area, 2)}/\u03c0) = {round(circle.radius, 2)} l.e."
            elif not circle_radius and not circle_area:
                return f"\nr = {round(circle.circumference, 2)}/(2*\u03c0) = {round(circle.radius, 2)} l.e."
            else:
                return ""

        t_1 = "Värden"

        t_2 = generate_t2()

        t_3 = generate_t3()

        t_4 = generate_t4()

        t_5 = "\n\nFormler""\nd = diameter = 2 * radie""\nr = radie""\nO = Omkrets = 2 * r * \u03c0""\nA = Area = r\u00b2 * \u03c0 = r * r * \u03c0"\
        "\nr = Omkrets/(\u03c0 * 2)\n""eller\n""r = \u221A(Area/\u03c0)""\n\nBeräkning"

        t_6 = f"\nO = 2 * {round(circle.radius, 2)} * \u03c0 = {round(circle.circumference, 2)} l.e."\
        f"\nA = {round(circle.radius, 2)} * {round(circle.radius, 2)} * \u03c0 = {round(circle.area, 2)} a.e."
        
        t_7 = calculate_radius_t7()

        losning = t_1 + t_2 + t_3 + t_4 + t_5 + t_6 + t_7

        return losning

    def inform_user():
        circle = create_object()

        #Create the window that displays the circle and calculations to the user
        circle_window = tkinter.Toplevel(root)
        
        #Set the windows parameters
        circle_window.title("Utdata")
        circle_window.geometry("800x380+250+125")

        #Create the drawing canvas and set its parameters
        circle_canvas = tkinter.Canvas(circle_window,width=340, height=340, relief="sunken", bg="white")
        circle_canvas.grid(column=0, row=0, sticky="nw", padx=10, pady=20)

        #Draw the circle
        #Since all circles are similar we can hard-code this shape and it'll always work
        circle_canvas.create_oval(80,80,260,260,width=2,fill="blue")
        
        #Draw the radius and diameter
        circle_canvas.create_line(170,170,170,80,width=3)
        circle_canvas.create_line(80,170,260,170,width=3)

        #Create the widgets that display the radius and diameter information
        circle_radius_widget = tkinter.Label(circle_canvas, text=f"r={round(circle.radius, 2)}")
        circle_diameter_widget = tkinter.Label(circle_canvas, text=f"d={round(circle.diameter, 2)}")

        #Define the widgets position inside the canvas
        circle_canvas.create_window(205,130,window=circle_radius_widget)
        circle_canvas.create_window(170,195,window=circle_diameter_widget)

        #Configure the textwidgets
        for child in [circle_radius_widget, circle_diameter_widget]:
            child.config(font = ("Arial", 14))
            child.config(fg="white",bg="black")
        
        #Generate the informational text with solution to the problem
        circle_solution = circle_generate_text(circle)

        #Create a label to put the solution into and configure it
        circle_losning = ttk.Label(circle_window, text = circle_solution)
        circle_losning.config(font = ("Arial", 11), anchor = "nw", justify = "left", width = 45)
        circle_losning.config(background = "white", relief = "sunken", wraplength = 410)
        circle_losning.grid(column = 1, row = 0, sticky = "news", padx = 10, pady = 10)

    def circle_gui(information_window): #Creates a gui for input data and collection of said data
        
        information_window.title("Indata")

        #Create labels and entries for each datapoint we want to collect
        #radius_entry is handled differently since we want to set focus on it
        ttk.Label(information_window,text="Radie").grid(column=1, row=1, sticky="w")
        radius_entry = ttk.Entry(information_window, width=7,textvariable=circle_radius)
        radius_entry.focus_set()
        radius_entry.grid(column=2, row=1)
        ttk.Label(information_window,text="l.e.").grid(column=3, row=1, sticky="E")
        
        ttk.Label(information_window,text="Omkrets").grid(column=1, row=2, sticky="w")
        ttk.Entry(information_window, width=7,textvariable=circle_circumference).grid(column=2, row=2)
        ttk.Label(information_window,text="l.e.").grid(column=3, row=2, sticky="E")

        ttk.Label(information_window,text="Area").grid(column=1, row=3, sticky="w")
        ttk.Entry(information_window, width=7,textvariable=circle_area).grid(column=2, row=3)
        ttk.Label(information_window,text="a.e.").grid(column=3, row=3, sticky="E")

        ttk.Button(information_window,text="Beräkna",command=inform_user).grid(column=2, row=4)

        #Make the GUI nice and roomy
        for child in information_window.winfo_children():
            child.grid_configure(padx=20,pady=20)

    #Add variables for entry and running logic
    circle_radius = tkinter.StringVar()
    circle_circumference = tkinter.StringVar()
    circle_area = tkinter.StringVar()

    #Create the input window
    circle_input_window = tkinter.Toplevel(root)

    #Run the GUI
    circle_gui(circle_input_window)

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
    #This function looks at the object and input from the user and generates a solution that only shows the pertinent information
        def generate_t2():
            if square_side.get():
                return f"L = Längd = {round(square.length, 2)} l.e.\n"
            else:
                return ""

        def generate_t3():
            if square_perimeter.get():
                return f"O = Omkrets = {round(square.perimeter, 2)} l.e.\n"
            else:
                return""
        
        def generate_t4():
            if square_area.get():
                return f"A = Area = {round(square.area, 2)} a.e.\n"
            else:
                return""
        
        def generate_t6():
            if not square_side.get() and not square_area.get():
                return "s = sidlängd = Omkrets / 4\n"
            elif not square_side.get() and not square_perimeter.get():
                return "s = sidlängd = \u221AArea\n"
            elif not square_side.get():
                return "s = sidlängd = Omkrets / 4\n"\
                    "eller\n"\
                    "s = \u221AArea"
            else:
                return ""

        def generate_t8():
            if not square_side.get() and not square_area.get():
                return f"s = {round(square.perimeter, 2)} / 4 = {round(square.length, 2)} l.e."
            elif not square_side.get() and not square_perimeter.get():
                return f"s = \u221A{round(square.area, 2)} = {round(square.length, 2)} l.e."
            elif not square_side.get():
                return f"s = {square.perimeter} / 4 = {round(square.length, 2)} l.e."
            else:
                return ""
        
        t_1 = "\nVärden\n\n"
        
        t_2 = generate_t2()
    
        t_3 = generate_t3()
    
        t_4 = generate_t4()
        
        t_5 = "\n\nFormler\n\n"\
            "O = Omkrets = 4 * s = s + s + s + s\n"\
            "A = Area = s\u00b2 = s * s\n"\
        
        t_6 = generate_t6()

        t_7 = "\n\nBeräkning\n\n"\
            f"O = 4 * {round(square.length, 2)} = {round(square.perimeter, 2)} l.e.\n\n"\
            f"A = {round(square.length, 2)} * {round(square.length, 2)} = {round(square.area, 2)} a.e.\n\n"

        t_8 = generate_t8()

        losning = t_1 + t_2 + t_3 + t_4 + t_5 + t_6 + t_7 + t_8

        return losning

    def inform_user():
        square = create_object()

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
            child.config(font = ("Arial", 14))
            child.config(fg="white",bg="black")
        
        #Generate the informational text with solution to the problem
        square_solution = square_generate_text(square)

        #Create a label to put the solution into and configure it
        square_losning = ttk.Label(square_window, text = square_solution)
        square_losning.config(font = ("Arial", 11), anchor = "nw", justify = "left", width = 45)
        square_losning.config(background = "white", relief = "sunken", wraplength = 410)
        square_losning.grid(column = 1, row = 0, sticky = "news", padx = 10, pady = 10)

    def square_gui(information_window): #Creates a gui for input data and collection of said data
        
        information_window.title("Indata")

        #Create labels and entries for each datapoint we want to collect
        #square_entry is a special case since we want to set focus to it
        ttk.Label(information_window,text="Sidlängd").grid(column=1, row=1, sticky="w")
        square_entry = ttk.Entry(information_window, width=7,textvariable=square_side)
        square_entry.focus_set()
        square_entry.grid(column=2, row=1)
        ttk.Label(information_window,text="l.e.").grid(column=3, row=1, sticky="E")
        
        ttk.Label(information_window,text="Omkrets").grid(column=1, row=2, sticky="w")
        ttk.Entry(information_window, width=7,textvariable=square_perimeter).grid(column=2, row=2)
        ttk.Label(information_window,text="l.e.").grid(column=3, row=2, sticky="E")

        ttk.Label(information_window,text="Area").grid(column=1, row=3, sticky="w")
        ttk.Entry(information_window, width=7,textvariable=square_area).grid(column=2, row=3)
        ttk.Label(information_window,text="a.e.").grid(column=3, row=3, sticky="E")

        #TODO: bind the enter key to trigger the button
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