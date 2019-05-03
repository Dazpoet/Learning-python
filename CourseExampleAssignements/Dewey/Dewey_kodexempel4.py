"""
 John Dewey - kodexempel 4
 Grafiska gränssnitt med tkinter
 Exempel med tkinter.Label (etikett)
 och tkinter.Button (knapp)
"""
import tkinter

#Skapa själva fönstret
ruta = tkinter.Tk()
ruta.title('Exempel 4')
ruta.geometry('300x50+50+100')

#Skapa och lägg in en etikett
halsning = tkinter.Label(ruta, text='Jag är en tkinter.Label')
halsning.pack()

#Skapa och lägg in en etikett
knapp = tkinter.Button(ruta, text='Hej, jag är en knapp', highlightbackground='green', fg='white')
knapp.pack(fill=tkinter.X)

#Visa fönstret och dess komponenter
tkinter.mainloop()


