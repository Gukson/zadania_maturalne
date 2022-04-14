f = open("napisy.txt", "r")

zad1 = 0
check = 0
koncowki = 0
wszystkie = []
for x in range(200):
    wyrazy = f.readline().rstrip().split(" ")
    if len(wyrazy[0])*3 < len(wyrazy[1]) or len(wyrazy[1])*3 < len(wyrazy[0]):
        if check == 0:
            print(wyrazy)
            check = 1
        zad1+=1
    if wyrazy[0] in wyrazy[1]:
        if wyrazy[1][:len(wyrazy[0])] == wyrazy[0]:
            print(wyrazy)
            print(wyrazy[1][len(wyrazy[0]):], " <- to trzeba dopisać do pierwszego wyrazu aby uzyskać drugi")
            print("===============")
    temp = 1
    while wyrazy[0][-temp:] == wyrazy[1][-temp:]:
        temp+=1
    if temp > koncowki:
        koncowki = temp
    wszystkie.append(wyrazy)
print(koncowki, " -")
for x in range(200):
    if wszystkie[x][0][-koncowki:] == wszystkie[x][1][-koncowki:]:
        print("siema")

print(zad1)

