w = open("wyniki.txt", "w")
f = open("liczby.txt", "r")

def dzielniki_naturalne(liczba):
    dzielniki = []
    for x in range(1,liczba+1):
        if liczba%x == 0:
            dzielniki.append(x)
    return dzielniki

def nwd_i(a, b):
    while b:
        a, b = b, a%b
    return a

mniejszeod1000 = []
for x in range(200):
    liczba = int(f.readline())
    if liczba < 1000:
        mniejszeod1000.append(liczba)
f.close()
w.write("zadanie 60.1\n")
w.write(str(len(mniejszeod1000)))
w.write(" - ilość liczb mniejszych od 1000\n")
w.write(str(mniejszeod1000[len(mniejszeod1000) - 1]))
w.write(" i ")
w.write(str(mniejszeod1000[len(mniejszeod1000) - 2]))
w.write(" - 2 ostatnie liczby mniejsze od 1000 \n")
w.write("zad 60.2\n")

wszystkie = []
f = open("liczby.txt", "r")
for x in range(200):
    liczba = int(f.readline())
    tab = dzielniki_naturalne(liczba)
    tab.sort()
    wszystkie.append(liczba)
    if len(tab) == 18:
        w.write(str(liczba))
        w.write("  -")
        for y in range(len(tab)):
            w.write(f" {tab[y]}")
        w.write("\n")

wzgledne = []
for x in range(len(wszystkie)):
    index = 1
    for y in range(len(wszystkie)):
        if wszystkie[x] != wszystkie[y]:
            index *= nwd_i(wszystkie[x], wszystkie[y])
    if index == 1:
        wzgledne.append(wszystkie[x])
wzgledne.sort()
w.write("zad 60.3\n")
w.write(f"{wzgledne[len(wzgledne)-1]} - największa względnie pierwsza liczba w pliku")





