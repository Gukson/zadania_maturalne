s1 = open("szyfr1.txt", "r")
s2 = open("szyfr2.txt", "r")
s3 = open("szyfr3.txt", "r")
w1 = open("wyniki_szyfr1.txt", "w")
w2 = open("wyniki_szyfr2.txt", "w")
w3 = open("wyniki_szyfr3.txt", "w")

tekst1 = s1.read().split("\n")
klucz1 = tekst1[len(tekst1)-1].rstrip().split()
del tekst1[len(tekst1)-1]

tekst2 = s2.read().split("\n")
klucz2 = tekst2[1].rstrip().split()

tekst3 = s3.readline().rstrip()

def generuj_klucz(l,tab=[]):
    klucz = []
    if l == len(tab):
        return tab
    elif l > len(tab):
        t = int(l/len(tab))
        r = l%len(tab)
        for x in range(t):
            for y in range(len(tab)):
                klucz.append(tab[y])
        for x in range(r):
            klucz.append(tab[x])
    return klucz

def swap(n, m, tab = []):
    temp = tab[n]
    tab[n] = tab[m-1]
    tab[m-1] = temp

def zad1(tekst):
    klucz = generuj_klucz(50,klucz1)
    tekst = list(tekst)
    for x in range(len(tekst)):
        swap(x,int(klucz[x]),tekst)
    tekst = ''.join(tekst)
    return tekst

def zad2(tekst):
    klucz = generuj_klucz(50,klucz2)
    tekst = list(tekst)
    for x in range(len(tekst)):
        swap(x,int(klucz[x]),tekst)
    tekst = ''.join(tekst)
    return tekst

def zad3(tekst):
    klucz = generuj_klucz(50, ["6","2","4","1","5","3"])
    tekst = list(tekst)
    for x in range(len(tekst)-1,-1,-1):
        temp =int(klucz[x])
        swap(x,int(klucz[x]), tekst)
    tekst = ''.join(tekst)
    return tekst

w1.write("zadanie 1\n")
for word in tekst1:
    temp = zad1(word)
    w1.write(f"{temp}\n")


w2.write(f"zadanie2\n{zad2(tekst2[0])}\n")
w3.write(f"zadanie3\n{zad3(tekst3)}\n")
