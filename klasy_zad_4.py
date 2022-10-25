class Car:
    def __init__(self, wydajnosc: int, pojemnosc_baku: float, poziom_paliwa=0) -> None:
        self.wydajnosc = wydajnosc
        self.pojemnosc_baku = pojemnosc_baku
        self.poziom_paliwa = poziom_paliwa

    def add_fuel(self, ile: float) -> None:
        if self.pojemnosc_baku < ile:
            self.poziom_paliwa = self.pojemnosc_baku
        else:
            self.poziom_paliwa = ile

    def drive(self, ile: float) -> None:
        liczba = self.wydajnosc / 1000
        liczba *= ile
        self. poziom_paliwa -= liczba

    def get_fuel_level(self) -> float:
        return round(self.poziom_paliwa, 2)


def main():
    my_car = Car(20, 40)
    my_car.add_fuel(30)
    my_car.drive(100)
    print(my_car.get_fuel_level())


if __name__ == "__main__":
    main()
