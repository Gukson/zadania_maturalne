f = open("liczby1.txt", "r")
e = open("liczby2.txt", "r")
w = open("wyniki.txt", "w")
liczby1 = []
liczby1_temp = []
for x in range(1000):
    temp = int(f.readline(), 8)
    liczby1.append(temp)
    liczby1_temp.append(temp)
liczby1_temp.sort()
w.write(f"zadanie 62.1\n{oct(liczby1_temp[0])[2:]} - najmniejsza\n{oct(liczby1_temp[len(liczby1)-1])[2:]} - największa\n")

liczby2 = []
for x in range(1000):
    liczby2.append(int(e.readline()))


def findIncreasingString(dataList):
    # Needed 999 elements
    leng = len(dataList)
    longest = list()  # najwiekszy ciag
    incr = list()  # bufor niemalejacego ciagu

    # konwersja na typ int
    for i in range(leng):
        dataList[i] = int(dataList[i])

        # zabezpieczenie przed out of range
    for idx in range(leng - 1):
        # sprawdza nastepny wyraz
        if dataList[idx + 1] >= dataList[idx]:
            incr.append(dataList[idx])
        # nastepny wyraz jest niemalejacy
        else:
            incr.append(dataList[idx])  # dodaje ostatni rosnacy wyraz
            # porownuje dlugosci
            if len(incr) > len(longest):
                # jesli nowy jest wiekszy to nadpisuje
                longest = incr
            # czysci bufor
            incr = list()

    return longest
licznik3 = 0
licznik4 = 0
for x in range(1000):
    if liczby1[x] == int(liczby2[x]):
        licznik3+=1
    if liczby1[x] > int(liczby2[x]):
        licznik4+=1

stringsList = findIncreasingString(liczby2)
w.write("zadanie 62.2\n")
w.write(f"Pierwszym elementem jest: {str(stringsList[0])}\n")
w.write(f"Dlugosc wynosi: {str(len(stringsList))}")
print(licznik3)
print(licznik4)