from tkinter import *
from random import randint
from tkinter import messagebox
def przycisk():
    messagebox.showinfo("Okno powitale", "Cześć")
okno=Tk()
okno.title("Kogni-ipsum")
okno.geometry("1080x640")
zdania = Label(okno, text="Wprowadź ilość zdań")
zdania.grid(row=0,column=0)
akapity = Label(okno, text="Wprowadź ilość akapitow")
akapity.grid(row=1, column=0)

przycisk1=Button(okno, text = "Generuj", command = przycisk)
przycisk1.grid(row=15, column=5)
okno.mainloop()
