import sys


phrase = sys.argv[1]
dane = []

while True:
    linia = input()
    if linia == "koniec":
        break
    if linia == "":
        continue
    dane.append(linia)


lista_wychowawcow = set()
lista_klas = set()
lista_nauczyczycieli = set()
lista_uczniow = set()
wychowawcy = []
nauczyciele = []
uczniowie = []
osoby = ["uczen", "nauczyciel", "wychowawca"]

for idx in range(len(dane)):
    if dane[idx] == osoby[2]:
        id = dane[idx + 1]
        wychowawcy.append(id)
        lista_wychowawcow.add(id)
        klasy = []
        oddzial = 0
        j = idx + 2
        while True:
                oddzial = dane[j]
                lista_klas.add(oddzial)
                klasy.append(oddzial)
                j = j + 1
                if dane[j] == "nauczyciel" or \
                    dane[j] == "uczen" or \
                    dane[j] == "wychowawca":
                    break
        wychowawcy.append(klasy)

for idx in range(len(dane)):
    if dane[idx] == osoby[1]:
        id = dane[idx + 1]
        nauczyciele.append(id)
        lista_nauczyczycieli.add(id)
        przedmiot = dane[idx + 2]
        nauczyciele.append(przedmiot)
        klasy = []
        oddzial = 0
        j = idx + 3
        while True:
            oddzial = dane[j]
            lista_klas.add(oddzial)
            klasy.append(oddzial)
            j = j + 1
            if dane[j] == "nauczyciel" or dane[j] == "uczen" \
                    or dane[j] == "wychowawca":
                break
        nauczyciele.append(klasy)

for idx in range(len(dane)):
    if dane[idx] == osoby[0]:
        id = dane[idx + 1]
        uczniowie.append(id)
        lista_uczniow.add(id)
        klasa = dane[idx + 2]
        lista_klas.add(klasa)
        uczniowie.append(klasa)
a= "1a"
if phrase in lista_klas:
    for idx in range(len(wychowawcy)):
        b = wychowawcy[idx]
        if a in b:
            print(wychowawcy[idx - 1])
    for idx in range(len(uczniowie)):
        if uczniowie[idx] == phrase:
            print(uczniowie[idx - 1])
elif phrase in lista_wychowawcow:
    b = wychowawcy[(wychowawcy.index(phrase))+1]
    for idx in range(len(uczniowie)):
        if uczniowie[idx] in b:
            print(uczniowie[idx-1])
elif phrase in lista_nauczyczycieli:
    c = []
    for idx in range(len(nauczyciele)):
        b = nauczyciele[idx]
        if phrase in b:
            c = nauczyciele[idx + 2]
    z = set()
    for i in range(len(c)):
        d = c[i]
        for j in range(len(wychowawcy)):
            b = wychowawcy[j]
            if d in b:
                e = wychowawcy[j - 1]
                z.add(e)
    for i in z:
        print(i)
elif phrase in lista_uczniow:
    for idx in range(len(uczniowie)):
        if uczniowie[idx] == phrase:
            b = uczniowie[idx + 1]
    for idx in range(len(nauczyciele)):
        c = nauczyciele[idx]
        if b in c:
            print(nauczyciele[idx - 1])
            print(nauczyciele[idx - 2])
else:
    print('Wpisane dane nie figurują w bazie szkolnej.')
