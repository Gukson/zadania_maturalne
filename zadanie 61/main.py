f = open("ciagi.txt", "r")
e = open("bledne.txt", "r")
w1 = open("wyniki1.txt", "w")
w2 = open("wyniki2.txt", "w")
w3 = open("wyniki3.txt", "w")

def czy_arytmentyczny(ciag = []):
    r = int(ciag[1]) - int(ciag[0])
    check = True
    for x in range(len(ciag)-1):
        if int(ciag[x]) + r != int(ciag[x+1]):
            check = False
    return check,r

def find_r(ciag = []):
    temp_r = int(ciag[1]) - int(ciag[0])
    if int(ciag[len(ciag)-1]) - int(ciag[len(ciag)-2]) == temp_r:
        return temp_r
    else:
        temp_r = int(ciag[len(ciag)-1]) - int(ciag[len(ciag)-2])
        return temp_r

def czy_arytmentyczny_bledne(ciag = []):
    r = find_r(ciag)
    bledny = ''
    for x in range(len(ciag)-1):
        if int(ciag[x]) + r != int(ciag[x+1]):
            bledny = ciag[x+1]
            break
    return bledny

def max_szescian(ciag = []):
    maks = 0
    for x in ciag:
        a = int(x)
        for y in [int(a**(1/3)) + i for i in (-1, 0, 1)]:
            if y**3 == a:
                maks = x
                break
    return maks

licznik_arytmetycznych = 0
maksr = 0
for x in range(100):
    dlugosc = int(f.readline())
    ciag = f.readline().rstrip().split(" ")

    maks = max_szescian(ciag)
    if int(maks) > 0:
        w2.write(f"{str(maks)}\n")

    if czy_arytmentyczny(ciag)[0]:
        licznik_arytmetycznych+=1
        if czy_arytmentyczny(ciag)[1] > maksr:
            maksr = czy_arytmentyczny(ciag)[1]

w1.write(f"{licznik_arytmetycznych} - liczba ciągów arytmetycznych w pliku\n{maksr} - największa różnica")

for x in range(20):
    dlugosc = int(e.readline())
    ciag = e.readline().rstrip().split(" ")

    bledne = czy_arytmentyczny_bledne(ciag)
    w3.write(f"{str(bledne)}\n")