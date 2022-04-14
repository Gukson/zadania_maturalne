f = open("funkcja.txt", "r")
all  = []
def szukaj(mi,ma):
    last = 0
    x = (mi + ma) / 2
    while True:
        if wylicz(x) == 0:
            break
        x = (mi + ma)/2
        if last == x:
            return x
        if wylicz(x) * wylicz(ma) > 0:
            ma = x
        else:
            mi = x
        last = x

def wylicz(x):
    if x >= 0 and x <1:
        f = float(all[0][0]) + float(all[0][1])*x + float(all[0][2])*x*x + float(all[0][3])*x*x*x
        return f
    elif x >= 1 and x <2:
        f = float(all[1][0]) + float(all[1][1])*x + float(all[1][2])*x*x + float(all[1][3])*x*x*x
        return f
    elif x >= 2 and x <3:
        f = float(all[2][0]) + float(all[2][1])*x + float(all[2][2])*x*x + float(all[2][3])*x*x*x
        return f
    elif x >= 3 and x <4:
        f = float(all[3][0]) + float(all[3][1])*x + float(all[3][2])*x*x + float(all[3][3])*x*x*x
        return f
    elif x >= 4 and x <5:
        f = float(all[4][0]) + float(all[4][1])*x + float(all[4][2])*x*x + float(all[4][3])*x*x*x
        return f
for x in range(5):
    wspolczynniki = f.readline().rstrip().lstrip().split()
    all.append(wspolczynniki)
zad1 = wylicz(1.5)
zad1 = round(zad1,5)
print(f"zadanie 1: {zad1}")
maks = 0
iks = 0
for x in range (0,5000):
    temp2 = x/1000
    temp = wylicz(temp2)
    if temp > maks:
        maks = temp
        iks = temp2

maks = round(maks,5)
print(f"zadanie 2: x = {iks} , f(x) = {maks}")

print(round(szukaj(0,1),5))
print(round(szukaj(2,3),5))
print(round(szukaj(3,4),5))