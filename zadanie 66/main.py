w = open("wyniki_trojki.txt", "w")
f = open("trojki.txt", "r")
def czy_pierwsza(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    pierw = int(n**0.5) + 1
    for dzielnik in range(3, pierw, 2):
        if n % dzielnik == 0:
            return False
    return True

def zad1(liczby):
    suma = 0
    for i in range(2):
        temp = list(str(liczby[i]))
        for x in range(len(temp)):
            suma += int(temp[x])
    if suma == liczby[2]: return True
    else: return False

def zad2(liczby = []):
    temp = liczby.copy()
    temp.sort()
    if czy_pierwsza(temp[0]) and czy_pierwsza(temp[1]):
        if temp[0]*temp[1] == temp[2]: return True
        else: return False

def zad3(liczby = []):
    temp = liczby.copy()
    temp.sort()
    if (temp[0]**2) + (temp[1]**2) == (temp[2]**2): return True
    else: return False

def czy_trojkat(liczby=[]):
    temp = liczby.copy()
    temp.sort()
    if temp[0]+temp[1] > temp[2]: return True
    else: return False

zadanie1 = []
zadanie2 = []
zadanie3 = []
wszystkie = []
licznik = 0

def znajdz_pary(tab = [], wszystkie = []):
    pary = []
    for x in range(len(tab)):
        if not tab[x] in pary:
            index = wszystkie.index(tab[x])
            if wszystkie[index-1] in tab:
                pary.append(tab[x])
                pary.append(wszystkie[index-1])
            elif wszystkie[index+1] in tab:
                pary.append(tab[x])
                pary.append(wszystkie[index+1])
    return pary

temp = 0
maks = 0
for x in range(1000):
    liczby = f.readline().rstrip().split(" ")
    wszystkie.append(liczby)
    for x in range(len(liczby)):
        liczby[x] = int(liczby[x])
    if zad1(liczby):
        zadanie1.append(liczby)
    if zad2(liczby):
        zadanie2.append(liczby)
    if zad3(liczby):
        zadanie3.append(liczby)
    if czy_trojkat(liczby):
        licznik+=1
        temp +=1
    else:
        if temp > maks: maks = temp
        temp = 0
w.write(f"zad1\n")
for x in range(len(zadanie1)):
    w.write(f"{zadanie1[x]}\n")
w.write(f"zad2\n")
wynik3 = znajdz_pary(zadanie3,wszystkie)
for x in range(len(zadanie2)):
    w.write(f"{zadanie2[x]}\n")
w.write(f"zad3\n")
for x in range(len(wynik3)):
    w.write(f"{wynik3[x]}\n")
w.write(f"zad4\nLiczba licbz trojkatnych jest rowna {licznik}\n")
w.write(f"najdluzszy ciag liczb trojkatnych ma dlugosc {maks}\n")