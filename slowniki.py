#Zad 1
'''
def foo_a(slowo, znak):
    dl = len(slowo)
    ile = 0
    for x in range(dl):
        if slowo[x] == znak:
            ile += 1
    dict = {znak: ile}
    return dict
'''


def foo_a(slowo, znak):
    ile = slowo.count(znak)
    return {znak: ile}


print(foo_a("siemaa", "a"))


def foo_b(slowo):
    slownik = {}
    for x in slowo:
        slownik = slownik | {x: slowo.count(x)}
    return slownik


print(foo_b("siemaA"))


def foo_c(slowo):
    slowo = slowo.lower()
    slownik = {}
    for x in slowo:
        slownik = slownik | {x: slowo.count(x)}
    return slownik


print(foo_c("siemaA"))


def foo_d(slowo):
    slowo = slowo.lower()
    slownik = {}
    for x in slowo:
        slownik = slownik | {x: slowo.count(x)}
    maks = 1
    for x in slowo:
        ile = slowo.count(x)
        if ile > maks:
            maks = ile
    return max(slownik)


print(foo_d("siemaa"))
