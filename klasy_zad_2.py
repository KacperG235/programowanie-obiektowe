class Adres:
    def __init__(self, nr_domu: int, ulica: str, miasto: str, kod_pocztowy: str, nr_mieszkania=0) -> None:
        self.nr_domu = nr_domu
        self.ulica = ulica
        self.nr_mieszkania = nr_mieszkania
        self.miasto = miasto
        self.kod_pocztowy = kod_pocztowy

    def show(self):
        print(self.nr_domu, self.ulica, "Numer mieszkania: ", self.nr_mieszkania)
        print(self.kod_pocztowy, self.miasto)

    def comes_before(self, other):
        if int(other.kod_pocztowy[2:5]) < int(self.kod_pocztowy[2:5]):
            return True
        else:
            return False


def main():
    adres1 = Adres(11, "notak", "Sosnowiec", "24-131", 11)
    adres2 = Adres(12, "nonie", "Olsztyn", "23-124")
    adres1.show()
    adres2.show()
    print(adres2.comes_before(adres1))


if __name__ == "__main__":
    main()