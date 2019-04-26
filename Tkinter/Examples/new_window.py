import tkinter as tk

def create_window():
    def destroy():
        window.destroy()
    window = tk.Toplevel(root)
    c = tk.Button(window, text="Destroy", command=destroy)
    c.pack()

root = tk.Tk()
b = tk.Button(root, text="Create new window", command=create_window)
b.pack()

root.mainloop()