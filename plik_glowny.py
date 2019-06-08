from tkinter import *
from random import randint
from tkinter import messagebox
def przycisk():
    messagebox.showinfo("Okno powitale", "Cześć")
okno=Tk()
okno.title("Kogni-ipsum")
okno.geometry("1080x640")
####
zdania = Label(okno, text="Wprowadź ilość zdań")
zdania.grid(row=0,column=0)
przycisk_zdania=Button(okno, text = "Generuj zdania", command = przycisk)
przycisk_zdania.grid(row=0,column=2)
pole_zdania= Entry(okno)
pole_zdania.grid(row=0,column=1)
####
akapity = Label(okno, text="Wprowadź ilość akapitow")
akapity.grid(row=1, column=0)
pole_akapity= Entry(okno)
pole_akapity.grid(row=1,column=1)
przycisk_akapity=Button(okno, text = "Generuj akapity", command = przycisk)
przycisk_akapity.grid(row=1, column=2)
okno.mainloop()
