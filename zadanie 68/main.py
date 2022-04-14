f = open("dane_napisy.txt", "r")
w = open("wyniki.txt", "w")
def Czy_jednolite(tekst1, tekst2):
    if not tekst1 == tekst2: return False
    else:
        check = 1
        litera = tekst1[0]
        for x in range(len(tekst1)):
            if not tekst2[x] == tekst1[x] and tekst2[x] == litera:
                check *=0
        if check == 0: return False
        else: return True

def Czy_anagram(tekst1,tekst2):
    temp1 = list(tekst1)
    temp1.sort()
    temp2 = list(tekst2)
    temp2.sort()
    if temp1 == temp2: return True
    else: return False

zad1 = 0
zad2 = 0
all = []
for x in range(1000):
    teksty = f.readline().strip().split(" ")
    tekst1 = teksty[0]
    tekst2 = teksty[1]
    if Czy_jednolite(tekst1,tekst2): zad1+=1
    if Czy_anagram(tekst1,tekst2): zad2+=1
    tekst1 = list(tekst1)
    tekst1.sort()
    tekst2 = list(tekst2)
    tekst2.sort()
    all.append(tekst1)
    all.append(tekst2)
all.sort()
maks = 0
temp = 1
for x in range (1,len(all)):
    if all[x] == all[x-1]:
        temp+=1
    else:
        if temp > maks:
            maks = temp
            temp = 1
w.write(f"zadanie 1: {zad1}\n")
w.write(f"zadanie 2: {zad2}\n")
print(maks)