def mult(arg, /):
    iloczyn = 1
    for x in arg:
        iloczyn *= x
    return iloczyn


print(mult([3, 5, 7]))
print(mult(range(2, 8, 2)))


def mult_ints(arg, /):
    iloczyn = 1
    for x in arg:
        if isinstance(x, int):
            iloczyn *= x
    return iloczyn


print(mult_ints([3, 3.14, 5, "abs", 7]))


def multiply(*args):
    iloczyn = 1
    for x in args:
        iloczyn *= x
    return iloczyn


print(multiply(3, 5, 7))


def multiply_ints(*args):
    iloczyn = 1
    for x in args:
        if isinstance(x, int):
            iloczyn *= x
    return iloczyn


print(multiply_ints(3, 3.14, 5, "abc", 7))


def make_car(firma, model, **kwargs):
    slownik = {}
    temp = {"firma": firma, "model": model}
    for key, value in kwargs.items():
        slownik[key] = value
    slownik = temp | slownik
    return slownik


print(make_car("BMW", "E46", kolor="czerwony", silnik="fajny", czy_jezdzi="tak", klepany="tak"))

#tablice wielowymiarowe:


def wyswietl(lista):
    for x in range(len(lista)):
        print(lista[x])


tablica1 = [[], [], []]
for x in range(1, 11):
    tablica1[0].append(x)
    tablica1[1].append(x ** 2)
    tablica1[2].append(x ** 3)
wyswietl(tablica1)
print("")

tablica2 = [[], [], [], [], [], [], [], [], [], []]
suma_calkowita = 0
suma_wiersz = 0
sumy = [[], [], [], [], [], [], [], [], [], []]

for x in range(len(tablica2)):
    for y in range(1, 11):
        tablica2[x].append(y)
        if x + 1 == y:
            break
wyswietl(tablica2)

for x in range(len(tablica2)):
    for y in range(len(tablica2[x])):
        suma_wiersz += tablica2[x][y]
        if x == y:
            sumy[x].append(suma_wiersz)
            suma_wiersz = 0
            break
for x in range(len(tablica2)):
    for y in range(len(tablica2[x])):
        suma_calkowita += tablica2[x][y]
        if x == y:
            break
wyswietl(sumy)
print("suma całkowita: ", suma_calkowita)
