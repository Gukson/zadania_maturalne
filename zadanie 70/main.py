def wylicz_f(x):
    y = (x ** 4) / 500 - (x ** 2) / 200 - 3 / 250
    y = abs(y)
    return y


def wylicz_g(x):
    y = -1 * (x ** 3) / 30 + x / 20 + 1 / 6
    y = abs(y)
    return y


p1 = 0
p2 = 0
x = 2
last_f = wylicz_f(2)
last_f = float(last_f)
last_g = wylicz_g(2)
lf = 0.0
lg = 0

while x < 10:
    lf += ((0.001) ** 2 + (wylicz_f(x) - last_f) ** 2) ** (1 / 2)
    lg += ((0.001) ** 2 + (wylicz_g(x) - last_g) ** 2) ** (1 / 2)

    last_f = wylicz_f(x)
    last_g = wylicz_g(x)

    p1 += 0.001 * (98 / 3 - wylicz_g(x))
    p2 += 0.001 * (2436 / 125 - wylicz_f(x))
    x += 0.001

h = round(98 / 3 + 2436 / 125, 3)
O = lf + lg + 8 + 8 + h
r = round((h * 8) - p1 - p2, 3)

suma = 0
x = 9.75
while x > 4.75:
    y = round(wylicz_f(x)) + round(wylicz_g(x))
    suma+=y
    x-=0.25
print(f"zadanie 1 - {r}")
print(f"zadanie 2 - {round(O)}")
print(f"zadanie 3 - {suma}")