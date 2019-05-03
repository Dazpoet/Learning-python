"""
 John Dewey - kodexempel 5
 Grafiska gränssnitt med tkinter
 Funktionsanrop och filsparning
"""

import tkinter

root = tkinter.Tk()
inputEntry = tkinter.Entry(root, width = 60, bg='white', font=('helvetica', 14))
infoLabel = tkinter.Label(root, height = 3, width=30,text='Skriv in den text du vill bearbeta', font=('helvetica', 14), bg='purple', fg='white')

def main():
    setGUI()
    root.mainloop()

def setGUI():
    root.title('X5 - Funktionsanrop i tkinter')
    root.geometry("400x275")
    infoLabel.grid(row=0, rowspan=2, columnspan=4, pady=5)
    inputEntry.grid(row=4, rowspan=3, columnspan=10, pady=2)
    inputEntry.insert(0, 'TestText')
    inputEntry.focus_set()
    tkinter.Button(root, width = 20, text = "Konvertera ",highlightbackground = "GREY",command = konvertera).grid(row=8, columnspan=2, padx=2, pady=5)
    tkinter.Button(root, width = 20, text = "Invertera", highlightbackground = "YELLOW",command=invertera).grid(row=10, columnspan=2, pady=5)
    tkinter.Button(root, width = 20, text = "Persistentiera" ,highlightbackground = "PURPLE",command=filSpara).grid(row=12, columnspan=2, pady=5)
    tkinter.Button(root, width = 20, text = "Terminera",highlightbackground = "RED",command=root.destroy).grid(row=14, rowspan=8, columnspan=9, pady=20)

def importera():
    text = str(inputEntry.get())
    return text

def konvertera():
    text = importera()
    text = text.lower()
    inputEntry.delete ( 0, len(text))
    inputEntry.insert(0, text)
    
    
def invertera():
    text = importera()
    text = text.swapcase()
    inputEntry.delete ( 0, len(text))
    inputEntry.insert(0, text)

def filSpara():
    text = importera()   
    try:
        myFile = open('text.txt', 'a')
        myFile.write(text + '\n')
    except IOError:
        print('Det gick inte att skriva till angiven fil.')
         

if __name__ == "__main__":
    main()



