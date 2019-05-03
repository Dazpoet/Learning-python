"""
 John Dewey - kodexempel 6
 Grafiska gränssnitt med tkinter
 Radioknappar och tkmessagebox
 (kanske något för en frågesport)
"""

import tkinter
from tkinter import messagebox

main_window = tkinter.Tk()
top_frame = tkinter.Frame(main_window)
bottom_frame = tkinter.Frame(main_window)
radio_var = tkinter.IntVar()


def main():
    main_window.title('Exempel 6 - att välja ett alternativ')
    main_window.geometry('300x100+50+100')
    createRadioButtons()
    createButtons()
    tkinter.mainloop()

def createButtons():
    choice_button = tkinter.Button(top_frame, text='Visa val', command=show_choice)
    quit_button = tkinter.Button(top_frame, text='Avsluta', command=quit)
    choice_button.pack(side='left')
    quit_button.pack(side='right')
    top_frame.pack()

def createRadioButtons():
    global radio_var
    #radio_var.set(1)
    rb1 = tkinter.Radiobutton(bottom_frame, text='Val 1', variable = radio_var, value =1)
    rb2 = tkinter.Radiobutton(bottom_frame, text='Val 2', variable = radio_var, value =2)
    rb3 = tkinter.Radiobutton(bottom_frame, text='Val 3', variable = radio_var, value =3)
    rb1.pack()
    rb2.pack()
    rb3.pack()
    bottom_frame.pack()
    

def show_choice():
    messagebox.showinfo('Valinfo','Du markerade alternativ ' + str(radio_var.get()))

def quit():
    main_window.destroy()
    
if __name__ == '__main__': 
    main()    
    
