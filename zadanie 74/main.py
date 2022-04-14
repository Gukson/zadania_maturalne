f = open("hasla.txt", "r")
w = open("wyniki_hasla.txt", "w")

hasla = []
cyfry = ["0","1","2","3","4","5","6","7","8","9"]
zad2 = set()
def zad1(haslo):
    check = 1
    for x in range(len(haslo)):
        if not haslo[x] in cyfry:
            check*=0
    if check == 0:
        return False
    else:
        return True

def zad3(haslo):
    maks= ''
    temp = haslo[0]
    for x in range(1,len(haslo)):
        if haslo[x] in cyfry and temp[0] in cyfry:
            temp+=haslo[x]
        elif haslo[x] not in cyfry and haslo[x].lower() == haslo[x]:
            if temp.lower() == temp:
                print("siema")

one = 0
for x in range(200):
    hasla.append(f.readline().rstrip())
for x in range(len(hasla)):
    if zad1(hasla[x]): one+=1
    if hasla.count(hasla[x]) > 1: zad2.add(hasla[x])

list(zad2)
w.write(f"zadanie 1 - {one}\n")
w.write(f"zadanie 2 - {zad2}")