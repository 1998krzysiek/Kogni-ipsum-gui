import random

def losowanie_zdan(lista_kogni,wybor):
    lista=[]
    for i in range(wybor):
        cytat=random.choice(lista_kogni)
        lista_kogni.remove(cytat)
        lista.append(cytat)
    rozwiazanie=''.join(lista)
    print(rozwiazanie)
def ilosc_akapitow(lista_kogni, wybor):
    for i in range(0, wybor):
        zdanie=random.choice(lista_kogni)
        lista_kogni.remove(zdanie)
        print(zdanie, '\n')
listaw=["Sprawdź to emipirycznie. ", "Amfetamina jest nieszkodliwa. ", "Jak kogni to tylko na UAM-ie. ", "Praca po kogni? Ja umiem wszystko. ", "Lubię palić marihuanę w nowych wcześniej nie znanych mi miejscach. ", "Meto to porażka. ", "Jasion to przemiła kobieta. ", "Idziesz na wykład do Grega? ", "Uczyłeś się na Algo? Bo ja będę ściągał chyba. ", "Niedługo będę was hackował. ", "Żałuję że nie było mnie na SSAK-U. ", "Zastanawiam się nad doktoratem z kogni. ", "Mariusz Urbański to klasa. ", "Nie zdałem meto. ", "Zdałem meto, mogę już umierać. ", "Toyota produkuje najlepsze samochody. ", "Pierwszy semestr na kogni jest sztosem. ", "Nie ulegał fałszywym heurystykom. ", "Tekst Loftus mnie rozwalił. ", "Opuścić zajęcia z Rasiem, to przypał. ", "Znam wszystkie rodzaje wnioskowań więc nie mów, że moje rozumowanie jest błędne. ", "Czy moglibyście wypełnić dla mnie ankietkę? ", "Nie mam czasu, uczę się na Meto. ", "Nie ogarniam SPSS-A. ", "Przeczytałeś teorię podwójnego kodowania Paivo. ", "Wolisz wcześniejszego czy późniejszego Wittgensteina. ", "Nie wyspałem się, ale mam dzisiaj wykład z Filo, więc sobie, to odbiję. ", "W 15 minut na Międzychodzką? Najwyżej się spóźnię. ", "Ty chodzisz na Algo czy na BPZ? ", "Dawaj do Zenona na piłeczkę, nie sprawdza nieobecności. ", "Co za farmazon mówił, że Zenon nie sprawdza nieobecności na w-fie? ", "Angielski z Kasprem, a komu to potrzebne. ", "Najwyżej wezmę warunek z PP? ", "A ten esej z Epi to na kiedy mamy zrobić? ", "O czym pisałeś esej z Epi? ", "Jakie jest twoje stanowisko w sporze o uniwersalia? ", "Pomożesz mi z MPK, bo nie ogarniam. ", "Ogarnę meto w jeden dzień. ", "Greg co gada. ", "Podobno warto iść na programowanie do Jukiego. ", "Podeślę Ci fajny filmik z Ted-a. ", "Język niemiecki? A komu to potrzebne. ", "Naming and grapsing common objects, to najlepszy artykuł jaki czytałem. ", "Ogarniamy w końcu tą prezentację na WDK? Jutro mamy deadline. ", "Tylko konceptualizm! ", "Tylko nominazim! ", "Lubię czytać Hume'a. ", "Robimy kogni obóz na Woodstock'u. ", "Czemu ja zapisałem się na w-f o ósmej to nie wiem. ", "Dlaczego ja zapisałem się na w-f na Morasko... "]
ilosc_akapitow(listaw, 3)
