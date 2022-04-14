f = open("ciagi.txt", "r")
w = open("wyniki.txt", "w")
def Czy_dwie_obok(ciag):
    test = 1
    for x in range(1,len(ciag)):
        if ciag[x] == "1" and ciag[x-1] == "1":
            test*=0
    if test == 1:
        return False
    elif test == 0:
        return True

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


def Czy_polpierwsza(liczba):
    for x in range(2,(int(liczba**(1/2))+1)):
        if liczba%x == 0:
            if czy_pierwsza(x) and czy_pierwsza(liczba/x):
                return True
    return False

def Czy_dwucykliczny(ciag):
    part1 = ''
    part2 = ''
    if len(ciag)%2 == 0:
        part1 = ciag[:len(ciag)//2]
        part2 = ciag[len(ciag)//2:]
        if part1 == part2:
            return True
    return False

licznik = 0
licznik1 = 0
zad1 = []
for x in range(1000):
    ciag = f.readline().rstrip()
    if Czy_dwucykliczny(ciag) == True:
        zad1.append(ciag)
    if not Czy_dwie_obok(ciag):
        licznik+=1
    liczba = int(ciag,2)
    if Czy_polpierwsza(liczba):
        licznik1+=1
w.write("zadanie 63.1\n")
for x in range(len(zad1)):
    w.write(f"{zad1[x]}\n")
w.write(f"zadanie 63.2\n{licznik}\n")
w.write(f"zadanie 63.3\n{licznik1}\n")


