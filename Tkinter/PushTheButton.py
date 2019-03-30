#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
import random

nice_things = ["Du är bäst", "Jag älskar dig", "Du är söt", "Du förtjänar choklad varje dag", "Du är smart"]

def random_nice_thing():
    message = tk.Message(root,text=random.choice(nice_things))
    message.config(font=('times',32,'italic'))
    message.pack()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Snälla saker")
    button = tk.Button(root,text="Klicka på mig",command = random_nice_thing)
    button.pack()
    root.mainloop()