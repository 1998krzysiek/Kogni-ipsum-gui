from tkinter import *
from random import randint
from tkinter import messagebox
import baza
import random
baza=["Sprawdź to jeszcze emipirycznie. ", "Amfetamina jest nieszkodliwa. ", "Jak kogni to tylko na UAM-ie. ", "Praca po kogni? Ja umiem wszystko. ", "Lubię palić marihuanę w nowych wcześniej nie znanych mi miejscach. ", "Meto to porażka. ", "Jasion to przemiła kobieta. ", "Idziesz na wykład do Grega? ", "Uczyłeś się na Algo? Bo ja będę ściągał chyba. ", "Niedługo będę was hackował. ", "Żałuję że nie było mnie na SSAK-U. ", "Zastanawiam się nad doktoratem z kogni. ", "Mariusz Urbański to klasa. ", "Nie zdałem meto. ", "Zdałem meto, mogę już umierać. ", "Toyota produkuje najlepsze samochody. ", "Pierwszy semestr na kogni jest sztosem. ", "Nie ulegał fałszywym heurystykom. ", "Tekst Loftus mnie rozwalił. ", "Opuścić zajęcia z Rasiem, to przypał. ", "Znam wszystkie rodzaje wnioskowań więc nie mów, że moje rozumowanie jest błędne. ", "Czy moglibyście wypełnić dla mnie ankietkę? ", "Nie mam czasu, uczę się na Meto. ", "Nie ogarniam SPSS-A. ", "Przeczytałeś teorię podwójnego kodowania Paivo. ", "Wolisz wcześniejszego czy późniejszego Wittgensteina. ", "Nie wyspałem się, ale mam dzisiaj wykład z Filo, więc sobie, to odbiję. ", "W 15 minut na Międzychodzką? Najwyżej się spóźnię. ", "Ty chodzisz na Algo czy na BPZ? ", "Dawaj do Zenona na piłeczkę, nie sprawdza nieobecności. ", "Co za farmazon mówił, że Zenon nie sprawdza nieobecności na w-fie? ", "Angielski z Kasprem, a komu to potrzebne. ", "Najwyżej wezmę warunek z PP? ", "A ten esej z Epi to na kiedy mamy zrobić? ", "O czym pisałeś esej z Epi? ", "Jakie jest twoje stanowisko w sporze o uniwersalia? ", "Pomożesz mi z MPK, bo nie ogarniam. ", "Ogarnę meto w jeden dzień. ", "Greg co gada. ", "Podobno warto iść na programowanie do Jukiego. ", "Podeślę Ci fajny filmik z Ted-a. ", "Język niemiecki? A komu to potrzebne. ", "Naming and grapsing common objects, to najlepszy artykuł jaki czytałem. ", "Ogarniamy w końcu tą prezentację na WDK? Jutro mamy deadline. ", "Tylko konceptualizm! ", "Tylko nominazim! ", "Lubię czytać Hume'a. ", "Robimy kogni obóz na Woodstock'u. ", "Czemu ja zapisałem się na w-f o ósmej to nie wiem. ", "Dlaczego ja zapisałem się na w-f na Morasko... "]
def przycisk1():
    lista=[]
    for i in range(int(pole_zdania.get())):
        cytat=random.choice(baza)
        baza.remove(cytat)
        lista.append(cytat)
    rozwiazanie=''.join(lista)
    messagebox.showinfo("Wygenerowanie zdania", rozwiazanie)

def przycisk2():
    wartosc=int(pole_akapity.get())
    messagebox.showinfo("Parara",losowanie_zdan(lista_kogni, pole_akapity.get()))
okno=Tk()
okno.title("Kogni-ipsum")
okno.geometry("1080x640")
def losowanie_zdan(lista_kogni,wybor):
    lista=[]
    for i in range(wybor):
        cytat=random.choice(lista_kogni)
        lista_kogni.remove(cytat)
        lista.append(cytat)
    rozwiazanie=''.join(lista)
    return rozwiazanie , print(rozwiazanie)
def ilosc_akapitow(lista_kogni, wybor):
    for i in range(0, wybor):
        zdanie=random.choice(lista_kogni)
        lista_kogni.remove(zdanie)
        print(zdanie, '\n')

####
zdania = Label(okno, text="Wprowadź ilość zdań")
zdania.grid(row=2,column=0)
przycisk_zdania=Button(okno, text = "Generuj zdania", command = przycisk1)
przycisk_zdania.grid(row=2,column=2)
pole_zdania= Entry(okno)
pole_zdania.grid(row=2,column=1)
####
akapity = Label(okno, text="Wprowadź ilość akapitow")
akapity.grid(row=3, column=0)
pole_akapity= Entry(okno)
pole_akapity.grid(row=3,column=1)
przycisk_akapity=Button(okno, text = "Generuj akapity", command = przycisk2)
przycisk_akapity.grid(row=3, column=2)
okno.mainloop()
