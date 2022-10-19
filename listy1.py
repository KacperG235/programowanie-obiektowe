#Zad 1
lista = []
#a
for x in range(10):
    lista.append(x+1)
print(lista)
#b
lista = []
for x in range(11):
    lista.append(x*2)
print(lista)
#c
lista = []
for x in range(10):
    lista.append((x+1)**2)
print(lista)
#d
lista = []
for x in range(10):
    lista.append(0)
print(lista)
#e
lista = []
for x in range(10):
    if x%2 == 0:
        lista.append(0)
    else:
        lista.append(1)
print(lista)
#f
lista = []
for x in range(5):
    lista.append(x)
for x in range(5):
    lista.append(x)
print(lista)
print('')
#Zad 2
#a
lista = []
i = 1
while i < 11:
    lista.append(i)
    i +=1
print(lista)
#b
lista = []
i = 0
while i < 11:
    lista.append(i*2)
    i +=1
print(lista)
#c
lista = []
i = 1
while i < 11:
    lista.append(i**2)
    i +=1
print(lista)
#d
lista = []
i = 1
while i < 11:
    lista.append(0)
    i +=1
print(lista)
#e
lista = []
i = 0
while i < 10:
    if i%2 == 0:
        lista.append(0)
    else:
        lista.append(1)
    i +=1
print(lista)
#f
lista = []
i = 0
while i < 5:
    lista.append(i)
    i +=1
i = 0
while i < 5:
    lista.append(i)
    i +=1
print(lista)

#Zad 3
def ile_ujemnych(lista):
    i = 0
    for x in lista:
        if x < 0:
            i +=1
    return i
lista = [-1, -19, 7, -4, 5]
print(ile_ujemnych(lista))

#Zad 4
def iloczyn(lista):
    i = 1
    for x in lista:
        i = i * x
    return i
lista = [1, 2, 3, 4]
print(iloczyn(lista))

#Zad 5
def minmax(lista):
    max = lista[0]
    min = lista[0]
    for x in lista:
        if max < x:
            max = x
        if min > x:
            min = x
    krotka = (min, max)
    return krotka
a = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print(minmax(a))

#Zad 6
def sumaprze(lista):
    suma = 0
    i = 0
    for x in lista:
        if i % 2 == 0:
            suma += x
        else:
            suma -= x
        i += 1
    return suma
b = [1, 4, 16, 9, 9, 7, 4, 9, 11]
print(sumaprze(b))
