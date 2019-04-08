#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Assignement: Create a simple game with a GUI that is somehow related to mathematics
#This is attempt one where pack will be used and the mechanics are heavily fetched from example Dewey_kodexempel6.py from the course
#TODO: Change from pack to grid
#TODO: Have the words and their corresponding answer in a csv to make it easier to update
#TODO: Check if having so many global variables is needed, coul some be added to their respective functions?
#TODO: Add a guesscounter
#TODO: Add a main menu, could this be a frame with buttons which based on choice creates difference interfaces? Destroy the main_menu frame?
#TODO: Figure out an easter egg
#TODO: Add a button that lets the user start over or go back to the main menu.
#TODO: Add a version where the user writes the answer rather than choose it
#TODO: Ask the user for their name
#TODO: Add a high-score list

import tkinter
from tkinter import ttk, messagebox

root = tkinter.Tk()

score_frame = tkinter.Frame(root)
word_frame = tkinter.Frame(root)
button_frame =tkinter.Frame(root)
quit_frame = tkinter.Frame(root)

choice = tkinter.IntVar()
word = tkinter.StringVar()
word_index = tkinter.IntVar()
CHOICE_COMPARE = {1: "Addition", 2: "Subtraktion", 3: "Multiplikation", 4: "Division"} #Could this be put directly into the correct function?
score = tkinter.IntVar()

questions = {
    0:("Produkt", "Multiplikation"),
    1:("Differens", "Subtraktion"),
    2:("Summa", "Addition"),
    3:("Kvot", "Division")
    }

def main():
    global questions, word, word_index

    root.title("De fyra räknesätten")
    
    word_index.set(0)
    word.set(questions[word_index.get()][0])

    messagebox.showinfo("Regler", "Du kommer att få ett antal ord, ditt uppdrag är att veta vilket räknesätt de hör ihop med.\nLycka till!")
    create_interface()
    tkinter.mainloop()


def create_interface():
    create_score_view()
    create_word_view()
    create_radio_buttons()
    create_quit_frame()

def create_score_view():
    ttk.Label(score_frame,text="Poäng:").pack(side='left')
    ttk.Label(score_frame,textvariable=score).pack(side='right')
    score_frame.pack()

def create_word_view():
    ttk.Label(word_frame,text="Ord:").pack(side='left')
    ttk.Label(word_frame, textvariable=word).pack(side='right')
    word_frame.pack()

def create_radio_buttons():
    radio1 = tkinter.Radiobutton(button_frame, text="Addition", variable = choice, value = 1)
    radio2 = tkinter.Radiobutton(button_frame, text="Subtraktion", variable = choice, value = 2)
    radio3 = tkinter.Radiobutton(button_frame, text="Multiplikation", variable = choice, value = 3)
    radio4 = tkinter.Radiobutton(button_frame, text="Division", variable = choice, value = 4)

    radio1.pack(anchor=tkinter.W)
    radio2.pack(anchor=tkinter.W)
    radio3.pack(anchor=tkinter.W)
    radio4.pack(anchor=tkinter.W)
    button_frame.pack()  

def create_quit_frame():
    ttk.Button(quit_frame, text="Nästa", command=correct).pack(side='right')
    ttk.Button(quit_frame, text="Avsluta", command=quit_program).pack(side='left')
    quit_frame.pack()

def correct():
    global questions, CHOICE_COMPARE, word_index

    if questions[word_index.get()][1] == CHOICE_COMPARE[choice.get()]:
        global score, word
        
        score.set(score.get() + 1)
        #messagebox.showinfo("Rätt!", message="Du klarade denna, men klarar du nästa?")
        
        word_index.set(word_index.get() + 1) #TODO: Add logic to make this stop when word_index > len(questions)
        word.set(questions[word_index.get()][0])

    else:
        messagebox.showinfo("Fel", message="Om du inte kan ordet, titta i kapitlet 'Verktygslådan' längst bak i boken.\nEfter att du gjort det kan du ordet så försök igen.")

def quit_program(): #The traceback from this is horrible, TODO: Find a better way to quit
    root.destroy()

if __name__ == "__main__":
    main()