import tkinter

ruta = tkinter.Tk()
ruta.title("Exempel 4")
ruta.geometry("300x50+50+100")

halsning = tkinter.Label(ruta, text="Jag är en label")
halsning.pack()

knapp = tkinter.Button(ruta, text = "Hej, jag är en knapp", highlightbackground = 'green')
knapp.pack()

tkinter.mainloop()