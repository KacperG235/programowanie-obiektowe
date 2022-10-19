#Macierze
def wyswietl(lista):
    for x in range(len(lista)):
        print(lista[x])
    print("")


def suma(a, b):
    if len(a) == len(b) and len(a[0]) == len(b[0]):
        c = [[0] * len(a)] * len(a[0])
        for x in range(len(a)):
            for y in range(len(a[0])):
                c[x][y] = a[x][y] + b[x][y]
        return c
    else:
        error = "Nie mozna dodac tych dwoch maciezy!"
        return error


def product(a, b):
    if len(a[0]) == len(b):
        c = [[0] * len(a[0])] * len(b)
        for x in range(len(a)):
            for y in range(len(b[0])):
                for z in range(len(b)):
                    c[x][y] += a[x][z] * b[z][y]
        return c
    else:
        error = "Nie mozna pomnozyc tych dwoch macierzy!"
        return error


def mult(a, liczba):
    for x in range(len(a)):
        for y in range(len(a[0])):
            a[x][y] *= liczba
    return a


def transp(a):
    temp = [[0] * len(a)] * len(a[0])
    for x in range(len(a)):
        for y in range(len(a[0])):
            temp[y][x] = a[x][y]
    return temp


a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]
c = [
    [1, 2, 3, 4],
    [2, 3, 4, 5]
]
d = [
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
]
wyswietl(suma(a, b))
wyswietl(product(a, b))
wyswietl(product(c, d))
wyswietl(mult(a, 2))
print(transp(d))
