f = open("liczby.txt", "r")
w = open("wyniki.txt", "w")

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

def odwroc_liczbe(liczba):
    liczba = str(liczba)
    liczba2 = ''
    for x in range(len(liczba),0,-1):
        liczba2+=liczba[x-1]
    liczba2 = int(liczba2)
    return liczba2

def palindron_check(liczba):
    liczba = str(liczba)
    if liczba == str(odwroc_liczbe(liczba)):
        return True
    else:
        return False

def mnozenie_liczb(liczba):
    liczba = str(liczba)
    temp = list(liczba)
    out = 1
    for x in range(0,len(temp)):
        out *= int(temp[x])
    return out


def power_calculator(liczba,maks_moc,mini_moc):
    baze_liczba = liczba
    power = 1
    while True:
        if mnozenie_liczb(liczba) >= 10:
            liczba = mnozenie_liczb(liczba)
            power+=1
        else:
            if power == 1:
                if baze_liczba > maks_moc:
                    maks_moc = baze_liczba
                if baze_liczba < mini_moc:
                    mini_moc = baze_liczba
            break
    return power,maks_moc,mini_moc

def rozklad(liczba):
    tab = []
    while True:
        if czy_pierwsza(liczba):
            tab.append(int(liczba))
            break
        for x in range(2,(int(liczba**0.5)+1)):
            if czy_pierwsza(x) and liczba%x == 0:
                liczba = liczba/x
                tab.append(x)
                break
    return tab
maks_moc = 0
mini_moc = 100000000000
power_data = []
czynn = []
licznik_zadanie1 = 0
licznik_zadanie2 = 0
for x in range(0,1000):
    liczba = int(f.readline())
    suma = liczba + odwroc_liczbe(liczba)
    pwr = power_calculator(liczba,maks_moc,mini_moc)
    maks_moc = pwr[1]
    mini_moc = pwr[2]
    power_data.append(pwr[0])
    if palindron_check(suma):
        licznik_zadanie2+=1
    czynniki = rozklad(liczba)
    czynniki = list(set(czynniki))
    czynniki.sort()
    if len(czynniki) == 3 and 2 not in czynniki:
        licznik_zadanie1 += 1

w.write("zad 59.1\n")
w.write(str(licznik_zadanie1))
w.write("\n")
w.write("zad 59.2\n")
w.write(str(licznik_zadanie2))
w.write("\n")
pwr_ilosc = [0,0,0,0,0,0,0,0]
for x in range (len(power_data)):
    pwr_ilosc[power_data[x]-1]+=1
w.write("zad 59.3\n")
w.write(f"1 - {pwr_ilosc[0]}\n")
w.write(f"2 - {pwr_ilosc[1]}\n")
w.write(f"3 - {pwr_ilosc[2]}\n")
w.write(f"4 - {pwr_ilosc[3]}\n")
w.write(f"5 - {pwr_ilosc[4]}\n")
w.write(f"6 - {pwr_ilosc[5]}\n")
w.write(f"7 - {pwr_ilosc[6]}\n")
w.write(f"8 - {pwr_ilosc[7]}\n\n")
w.write(f"Minimalna liczba o mocy jeden jest rowna: {mini_moc}\n")
w.write(f"Maksymalna liczba o mocy jeden jest rowna: {maks_moc}")

f.close()