p = open("probka.txt", "r")
f = open("tekst.txt", "r")
w = open("wyniki.txt", "w")
alfabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def zakoduj(word,A,B):
    word = list(word)
    zakodowany = ""
    for l in word:
        poz = alfabet.index(l)
        poz *= A
        poz += B
        if poz > 25:
            poz = poz%26
        zakodowany+=alfabet[poz]
    return zakodowany

def znajdz_klucz(w1,w2):
    for x in range(26):
        for y in range(26):
            if zakoduj(w1,x,y) == w2:
                return x,y

tekst = f.readline().rstrip().split()
w.write("zadanie 1\n")
for word in tekst:
    if word[0] == word[len(word)-1] and word[0] == 'd':
        w.write(f"{word}\n")
w.write("\n")
w.write("zadanie 2\n")
for word in tekst:
    if len(word) >= 10:
        w.write(f"{zakoduj(word,5,2)}\n")

w.write("\n")
w.write("zadanie 3\n")
for x in range(5):
    tekst = p.readline().rstrip().split()
    #klucz szyfrujący
    klucz_szyfrujacy = znajdz_klucz(tekst[0],tekst[1])
    #klucz deszyfrujacy
    klucz_deszyfrujacy = znajdz_klucz(tekst[1], tekst[0])
    w.write(f"{tekst[0], tekst[1]} klucz szyfrujacy - {klucz_szyfrujacy}, klucz deszyfrujący - {klucz_deszyfrujacy}\n")



w.close()
p.close()
f.close()