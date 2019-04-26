import tkinter as tk

root = tk.Tk()

w1 = tk.Label(root, text="Hello World!").pack(side="right")
w2 = tk.Label(root, text="Hello TKinter").pack(side="left")


root.mainloop()