f = open("dane_geny.txt", "r")

def znajdz_geny(genotyp):
    geny = []
    while genotyp.find("AA") != -1 or genotyp.find("BB") != -1:
        AA_index = genotyp.find("AA")
        if AA_index == -1:
            break
        genotyp = genotyp[AA_index:]
        BB_index = genotyp.find("BB")
        if BB_index == -1:
            break
        geny.append(genotyp[:BB_index+2])
        genotyp = genotyp[BB_index+2:]
    return geny


gatunki = []
for x in range(1000):
    genotyp = f.readline().rstrip()
    geny = znajdz_geny(genotyp)
    gatunki.append(geny)
# se = set(gatunki)
gatunki.sort()
print(gatunki)