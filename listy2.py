#Zad 7
def foo7():
    lista = []
    for x in range(10):
        liczba = input("Wprowadz liczbe: ")
        if liczba in lista:
            print("Ta liczba już jest na liscie!")
        else:
            lista.append(liczba)
    print(lista)

#Zad 8
def foo8():
    suma = 0
    lista = []
    for x in range(10001):
        if x > 1:
            lista.append(x)
    liczba = 0
    for x in range(102):
        i = 2
        if x > 1:
            while liczba <= 10000:
                liczba = x**i
                i += 1
                if liczba in lista:
                    lista.remove(liczba)
    print(lista)

#Zad 9

#a
def foo9_a(lista):
    dl = len(lista)
    temp = lista[0]
    lista[0] = lista[dl - 1]
    lista[dl - 1] = temp
    return lista
lista = [1, 2 ,3, 4]
print(foo9_a(lista))

#b
def shift(l, n):
    return l[n:] + l[:n]
a = [1, 4, 9, 16, 25]


 def foo9_b(lista):
    pomoc = []
    dl = len(lista)
    temp = lista[dl - 1]
    for index, item in enumerate(lista):
        if index > 0:
            pomoc.append(lista[index])
    return pomoc
print(foo9_b(a))

#c
def foo9_c(lista):
    for index, item in enumerate(lista):
        if item % 2 == 0:
            lista[index] = 0
    return lista
print(foo9_c(a))











