f = open("dane_ulamki.txt", "r")
w = open("wyniki_ulamki.txt", "w")
min_ulamki = [[1,1]]
nieskracalne = []
zad3 = []
wszystkie = []
def dodawanie_ulamkow(u1 = [], u2 = []):
    mianownik = u1[1] * u2[1]
    licznik1 = u1[0] * u2[1]
    licznik2 = u2[0] * u1[1]
    licznik = licznik1 + licznik2
    u = [licznik,mianownik]
    while nwd(u[0], u[1]) != 1:
        temp = nwd(u[1], u[0])
        u[0] /= temp
        u[1] /= temp
    return u
def nwd(a, b):
    if b > 0:
        return nwd(b, a%b)
    return a
for x in range(1000):
    liczby = f.readline().rstrip().split(" ")
    for x in range(len(liczby)):liczby[x]=int(liczby[x])
    wszystkie.append(liczby)
    l = liczby
    if nwd(l[1],l[0])==1:
        nieskracalne.append(l)
        zad3.append(l)
    else:
        temp = nwd(l[1],l[0])
        l[0] /= temp
        l[1] /= temp
        zad3.append(l)
    ulamek = round(float(l[0] / l[1]),5)
    if ulamek < round(float(min_ulamki[0][0]/min_ulamki[0][1]),5):
        min_ulamki.clear()
        min_ulamki.append(l)
    elif ulamek == round(float(min_ulamki[0][0] / min_ulamki[0][1]),5):min_ulamki.append(l)
ulamek_suma = wszystkie[0]
for x in range(1,len(wszystkie)):
    ulamek_suma = dodawanie_ulamkow(ulamek_suma,wszystkie[x])
docelowy_mianownik = (2**2)*(3**2)*(5**2)*(7**2)*13
ulamek_suma[0] *= docelowy_mianownik
docelowy_licznik = ulamek_suma[0] / ulamek_suma[1]
mianowniki = []
for x in range(len(min_ulamki)):
    mianowniki.append(int(min_ulamki[x][1]))
mini = min(mianowniki)
for x in range(len(min_ulamki)):
    if mini in min_ulamki[x]: wynik = min_ulamki[x];break
w.write(f"zad1\n    {str(wynik)}\n")
w.write(f"zad2\n    {str(len(nieskracalne))}\n")
suma = sum(x[0] for x in zad3)
w.write(f"zad3\n    {str(suma)}\n")
w.write(f"zad4\n    {str(docelowy_licznik)}\n")