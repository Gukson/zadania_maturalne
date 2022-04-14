w = open("wyniki.txt","w")
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
def fibinaci(n):
    ciag = [1,1]
    for x in range(2,n):
        ciag.append(ciag[x-2]+ciag[x-1])
    return ciag
zad2 = []
ciag = fibinaci(40)
w.write(f"zad1\n{ciag[9], ciag[19], ciag[29], ciag[39]}\n")
for x in range(len(ciag)):
    if czy_pierwsza(ciag[x]): zad2.append(ciag[x])
w.write(f"zad2\n{zad2}\n")
binarny = []
for x in range(len(ciag)):
    binarny.append(bin(ciag[x])[2:])
maks = (len(str(binarny[39])))
for x in range(len(binarny)):
    tekst = ''
    for y in range(maks - len(binarny[x])):
        tekst +='0'
    tekst+=binarny[x]
    binarny[x] = tekst
w.write("zad3\n")
for x in range(len(binarny)):
    w.write(f"{binarny[x]}\n")
licznik = []
temponary = binarny.copy()
for x in range(len(binarny)):
    temponary[x] = list(temponary[x])
    temp = 0
    for y in range(len(binarny[x])):
        if temponary[x][y] == '1':
            temp+=1
    if temp == 6:
        licznik.append(binarny[x])
w.write("zad4\n")
for x in range(len(licznik)):
    w.write(f"{licznik[x]}\n")
