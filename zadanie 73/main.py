f = open("tekst.txt", "r")
w = open("wyniki.txt", "w")

text = f.readline().rstrip().split(" ")
zad1 = 0
litery = []
liczby = []
samogloski = ["A","E","I","O","U","Y"]
zad3 = 0

maks = ''
for x in range(len(text)):
    temp2 = ''
    check = 1
    temp = list(text[x])
    for y in range(1,len(temp)):
        if temp[y] == temp[y-1]:
            zad1 += 1
            break
    for y in range(len(temp)):
        if temp[y] in litery:
            liczby[litery.index(temp[y])] += 1
        else:
            liczby.append(1)
            litery.append(temp[y])

    for y in range(len(temp)):
        if not temp[y] in samogloski:
            temp2 += temp[y]
        else:
            if len(temp2) > len(maks):
                maks = temp2
            temp2 = ''
    if len(temp2) > len(maks):
        maks = temp2
all = []
for x in range(len(text)):
    maks2 = ''
    temp = ''
    l = list(text[x])
    for y in range(len(l)):
        if not l[y] in samogloski:
            temp += l[y]
        else:
            if len(temp) > len(maks2):
                maks2 = temp
            temp = ''
    if len(maks2) == len(maks):
        print(maks2)
        all.append(text[x])
w.write(f"zadanie 1 - {zad1}")
w.write(f"zadanie 2 \n")
suma = sum(liczby)
for x in range(len(litery)):
    w.write(f"{litery[x]} - {str(round((liczby[x] / suma)*100,2))}%\n")
w.write(f"zadanie 3 - {len(maks)}")
print(all)
