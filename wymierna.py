class Wymierna:
    def __init__(self, p=0, q=1):
        self.p = p
        self.q = q

    def get_licznik(self):
        return self.p

    def get_mianownik(self):
        return self.q

    def __repr__(self):
        return f'{self.p}/{self.q}'

    def __float__(self):
        return self.p / self.q

    def __add__(self, other):
        return Wymierna((self.p/self.q) + (other.p/other.q))

    def __eq__(self, other):
        if self.p == other.p:
            if self.p <= self.q:
                return self.p == other.p and self.q == other.q

    def __ne__(self, other):
        return self.p != other.p and self.q != other.q

    def __lt__(self, other):
        if self.q == other.q:
            if self.p < self.q:
                return True
            else:
                return False

    def __le__(self, other):
        if self.q == other.q:
            if self.p <= self.q:
                return True
            else:
                return False

    def __gt__(self, other):
        if self.q == other.q:
            if self.p > self.q:
                return True
            else:
                return False

    def __ge__(self, other):
        if self.q == other.q:
            if self.p >= self.q:
                return True
            else:
                return False

    def __mul__(self, other):
        temp = Wymierna()
        temp.p = self.p * other.p
        temp.q = self.q * other.q
        return temp

    def __truediv__(self, other):
        temp = Wymierna()
        temp.p = self.p * other.q
        temp.q = self.q * other.p
        return temp


def main():
    liczba1 = Wymierna(1, 2)
    liczba2 = Wymierna(3, 2)
    print(liczba1.get_licznik())
    print(liczba1.get_mianownik())
    print(repr(liczba1))
    print(float(liczba1))
    print(liczba1 + liczba2)
    print(liczba1 == liczba2)
    print(liczba1 != liczba2)
    print(liczba1 < liczba2)
    print(liczba1 <= liczba2)
    print(liczba1 > liczba2)
    print(liczba1 >= liczba2)
    print(liczba1 * liczba2)
    print(liczba1 / liczba2)


if __name__ == "__main__":
    main()
