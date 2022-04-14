import math

d1 = open("dane_systemy1.txt", "r")
d2 = open("dane_systemy2.txt", "r")
d3 = open("dane_systemy3.txt", "r")
w = open("wyniki.txt", "w")

czas1 = []
czas2 = []
czas3 = []

czy_rekord1 = []
czy_rekord2 = []
czy_rekord3 = []

temperatura1  = []

w.write("zad 58.1\n")
d1_min = 0
last_temp1 = -100
last_temp2 = -100
last_temp3 = -100
for x in range(1095):
    line = d1.readline().split(" ")
    line = [int(line[0],2), int(line[1],2)]
    temperatura1.append(line[1])
    if line[1] > last_temp1:
        czy_rekord1.append(1)
        last_temp1 = line[1]
    else:
        czy_rekord1.append(0)
    czas1.append(line[0])
    if line[1] < d1_min:
        d1_min = line[1]
d1_min = bin(d1_min)
w.write(d1_min)
w.write(" - najmniejsza temperatura na S1\n")

d2_min = 0
for x in range(1095):
    line = d2.readline().split(" ")
    line = [int(line[0],4), int(line[1],4)]
    if line[1] > last_temp2:
        czy_rekord2.append(1)
        last_temp2 = line[1]
    else:
        czy_rekord2.append(0)
    czas2.append(line[0])
    if line[1] < d2_min:
        d2_min = line[1]
d2_min = bin(d2_min)
w.write(d2_min)
w.write(" - najmniejsza temperatura na S2\n")

d3_min = 0
for x in range(1095):
    line = d3.readline().split(" ")
    line = [int(line[0],8), int(line[1],8)]
    if line[1] > last_temp3:
        czy_rekord3.append(1)
        last_temp3 = line[1]
    else:
        czy_rekord3.append(0)
    czas3.append(line[0])
    if line[1] < d3_min:
        d3_min = line[1]
d3_min = bin(d3_min)
w.write(d3_min)
w.write(" - najmniejsza temperatura na S3\n")

w.write("zad 58.2\n")
licznik = 0
for x in range(1095):
    czas = 12 + 24*x
    if czas1[x] != czas and czas2[x] != czas and czas3[x] != czas:
        licznik += 1
w.write(str(licznik))
w.write(" -liczba niepoprawnych pomiarów czasu we wszystkich stacjach na raz\n")

licznik_rekordów = 0
for x in range(len(czy_rekord3)):
    if czy_rekord3[x] == 1 or czy_rekord2[x] == 1 or czy_rekord1[x] == 1:
        licznik_rekordów +=1
w.write("zad 58.3 \n")
w.write(str(licznik_rekordów))
w.write(" -ilość dni gdy przynajmniej jedna staxcja miała rekord\n")

max_skok = 0
for x in range(len(temperatura1)):
    for y in range(len(temperatura1)):
        r = (temperatura1[x] - temperatura1[y])**2
        if (x - y) != 0:
            skok = math.ceil(r / abs(x - y))
            if skok > max_skok:
                max_skok = skok

w.write("zad 58.4\n")
w.write(str(max_skok))
w.write(" - maksymany skok temperatury")


d1.close()
d2.close()
d3.close()
w.close()