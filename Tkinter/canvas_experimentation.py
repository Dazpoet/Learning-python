import tkinter
from tkinter import ttk

root = tkinter.Tk()
root.geometry("800x380+250+125")
window_frame = ttk.Frame(root).grid(column=0,row=0,sticky="nw")

canvas = tkinter.Canvas(window_frame,width=340, height=340, relief="sunken", bg="white")
canvas.grid(column=0,row=0, padx=10,pady=20)               
a= 80
b= 260
canvas.create_rectangle(a, a, b, b, width=2, fill='green')
c_int = 125788
c = 70-(5*len(str(c_int)))
d = 5    
     
side1_widget = tkinter.Label(canvas, text= c_int)
side2_widget = tkinter.Label(canvas,text= d)
#widget.pack()
canvas.create_window(c, 170, window=side1_widget)
canvas.create_window(170,280, window=side2_widget)

for child in [side1_widget, side2_widget]:
    child.config(font = ("Arial", 18))
    child.config(fg="white",bg="black")

text = "Blabla blubbe tack för krubbe, hugg in!"

info_text = ttk.Label(window_frame, text = text)
info_text.config(font = ("Arial", 12), anchor = "n", justify = "left", width = 40)
info_text.config(background = "white", relief = "sunken", wraplength = 410)
info_text.grid(column = 2, row = 0, rowspan = 10, sticky = "news", padx = 10, pady = 20)

root.mainloop()