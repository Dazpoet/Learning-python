#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Assignement: Create a simple game with a GUI that is somehow related to mathematics
#This is attempt one where pack will be used and the mechanics are heavily fetched from example Dewey_kodexempel6.py from the course
#TODO: Change from pack to grid
#TODO: Check if having so many global variables is needed, coul some be added to their respective functions?
#TODO: Add a main menu, could this be a frame with buttons which based on choice creates difference interfaces? Destroy the main_menu frame to move forward?
#TODO: Figure out an easter egg, need a picture of a toilet roll
#TODO: Add a button that lets the user start over or go back to the main menu.
#TODO: Add a version where the user writes the answer rather than choose it
#TODO: Ask the user for their name
#TODO: Add a high-score list

import tkinter
from tkinter import ttk, messagebox
import csv
import os
import random

root = tkinter.Tk()

score_frame = tkinter.Frame(root)
guess_frame = tkinter.Frame(root)
word_frame = tkinter.Frame(root)
button_frame =tkinter.Frame(root)
quit_frame = tkinter.Frame(root)

choice = tkinter.IntVar()
word = tkinter.StringVar()
word_index = tkinter.IntVar()
score = tkinter.IntVar()
guesses = tkinter.IntVar()

questions = {}
number_of_questions = 0

def main():
    global questions, word, word_index, guesses

    root.title("De fyra räknesätten")
    root.geometry("300x200")
    
    questions = generate_questions(4)
    print(questions)
    guesses.set(0)
    word_index.set(0)
    word.set(questions[word_index.get()][0])

    create_interface()
    messagebox.showinfo("Regler", "Du kommer att få ett antal ord, ditt uppdrag är att veta vilket räknesätt de hör ihop med.\nLycka till!")
    tkinter.mainloop()

def generate_questions(n): #Returns a dictionary with an index and n matching pairs of question,answer tuples
    global number_of_questions

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = dir_path + "\indata.csv"
    
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        input_data = [row for row in csv.reader(csvfile)]

    number_of_questions = len(input_data) - 1 #-1 to account for the headers

    input_data_random_sample_of_lenght_n = random.sample(input_data[1:len(input_data)], k=(n+1)) #This variable name is a real mouthful, but very telling of what it is

    questions = {}

    for i in range(len(input_data_random_sample_of_lenght_n)):
        questions[i] = tuple(input_data_random_sample_of_lenght_n[i])
    
    return questions

def create_interface():
    create_score_view()
    create_guess_view()
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

def create_guess_view():
    ttk.Label(guess_frame,text="Antal gissningar: ").pack(side='left')
    ttk.Label(guess_frame,textvariable=guesses).pack(side='right')
    guess_frame.pack()

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
    quit_frame.pack(side='bottom')

def correct():
    global questions, word_index, choice, number_of_questions

    CHOICE_COMPARE = {1: "Addition", 2: "Subtraktion", 3: "Multiplikation", 4: "Division"}

    if questions[word_index.get()][1].lower() == CHOICE_COMPARE[choice.get()].lower():
        global score, word, guesses
        
        score.set(score.get() + 1)
        
        if not word_index.get() == len(questions) - 1:
            word_index.set(word_index.get() + 1)
            word.set(questions[word_index.get()][0])
            guesses.set(guesses.get() + 1)
        else:
            message = f"Du har koll på matteorden i den här omgången, du tog alla frågor på {guesses.get()} försök!\
            \nStarta programmet igen för att få köra en omgång till med en annan blandning ord.\
            \nProgrammet innehåller {number_of_questions} ord så chansen finns att du stöter på några nya ord nästa gång"
            messagebox.showinfo(message=message)
            quit_program()
    else:
        messagebox.showinfo("Fel", message="Om du inte kan ordet, titta i kapitlet 'Verktygslådan' längst bak i boken.\nEfter att du gjort det kan du ordet så försök igen.")

def quit_program():
    root.destroy()

if __name__ == "__main__":
    main()