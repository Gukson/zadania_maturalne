f = open("dane_obrazki.txt", "r")

def Czy_poprawny(obrazek = []):
    licznik_poprawnych_w_wierszach = 0
    licznik_poprawnych_w_kolumnach = 0
    for x in range(20):
        temp = obrazek[x].count('1')
        if temp%2 == 0 and obrazek[x][20] == '0':
            licznik_poprawnych_w_wierszach += 1
        elif temp%2 != 0 and obrazek[x][20] == '1':
            licznik_poprawnych_w_wierszach += 1

    for y in range(20):
        temp_suma = 0
        for x in range(20):
            if obrazek[x][y] == '1':
                temp_suma += 1
        if temp_suma % 2 == 0 and obrazek[20][y] == "0":
            licznik_poprawnych_w_kolumnach += 1
        elif temp % 2 != 0 and obrazek[20][y] == "1":
            licznik_poprawnych_w_kolumnach += 1

    if licznik_poprawnych_w_kolumnach == 20 and licznik_poprawnych_w_wierszach == 20:
        return 1 #poprawny
    elif 20 - licznik_poprawnych_w_kolumnach == 1 or 20 - licznik_poprawnych_w_kolumnach == 0 and 20 - licznik_poprawnych_w_wierszach == 1 or 20 - licznik_poprawnych_w_wierszach == 0:
        return 2 #naprawialny
    else:
        return 3 #niepoperawny

def Czy_rekurencyjny(obrazek = []):
    check = 1
    for x in range(10):
        for y in range(10):
            if not obrazek[x][y] == obrazek[x][y+10] == obrazek[x+10][y+10] == obrazek[x+10][y]:
                check *= 0
    if check == 1:
        return True
    else:
        return False

def Czy_rewers(obrazek):
    licznik1 = 0
    licznik0 = 0
    for x in range(20):
        for y in range(20):
            if obrazek[x][y] == '1':
                licznik1+=1
            else:
                licznik0+=1
    if licznik1 > licznik0:
        return True
    else:
        return False

licznik_rewersow = 0
liczba_rekurencyjnych = 0
check2 = 0
obrazek_pierwszy = []
licznik_poprawnych = 0
licznik_naprawialnych = 0
licznik_niepoprawnych = 0
for x in range(200):
    obrazek = []
    for y in range(21):
        linijka = list(f.readline().rstrip())
        obrazek.append(linijka)
    if Czy_rewers(obrazek):
        licznik_rewersow+=1
    if Czy_rekurencyjny(obrazek):
        if check2 == 0:
            obrazek_pierwszy = obrazek
            check2 = 1
        liczba_rekurencyjnych +=1
    if Czy_poprawny(obrazek) == 1:
        licznik_poprawnych+=1
    elif Czy_poprawny(obrazek) == 2:
        licznik_naprawialnych +=1
    else:
        licznik_niepoprawnych+=1
    f.readline()
print(licznik_rewersow)
print(liczba_rekurencyjnych)
for z in range(20):
    print(obrazek_pierwszy[z][:-1])

print(licznik_poprawnych)
print(licznik_naprawialnych)
print(licznik_niepoprawnych)
