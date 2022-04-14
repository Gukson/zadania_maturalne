import math

f = open("sygnaly.txt", "r")
p = open("przyklad.txt", "r")
w = open("wyniki4.txt", "w")
zad1 = ''
zad21 = ''
zad22 = 0
zad3 = []
for x in range(1,1001):
    check = 1
    tekst = f.readline().rstrip()
    lista = list(tekst)
    tekst2 = set(lista)
    if len(tekst2) > zad22:
        zad21 = tekst
        zad22 = len(tekst2)
    if x%40 == 0:
        zad1+=lista[9]
    for y in range(len(lista)):
        for z in range(len(lista)):
            if y != z:
                r = ord(lista[y]) - ord(lista[z])
                if math.fabs(r) > 10:
                    check *=0
    if check == 1:
        zad3.append(tekst)
w.write(f"zadanie 1: {zad1}\n")
w.write(f"zadanie 2: {zad21}  {zad22}\n")
w.write(f"zadanie 3:\n")
for x in range(len(zad3)):
    w.write(f"{zad3[x]}\n")