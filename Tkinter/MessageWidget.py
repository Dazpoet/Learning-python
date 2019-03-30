import tkinter as tk
import math

def simple_calc (from_user):
    return_value = math.sqrt(from_user)
    return return_value

def main():
    root = tk.Tk()
    msg = tk.Message(root, text=(str(simple_calc(16)) + " is the square root of 16"))
    msg.config(bg='red', font=('arial', 32, 'bold'))
    msg.pack()
    tk.mainloop()

if __name__ == "__main__":
    main()