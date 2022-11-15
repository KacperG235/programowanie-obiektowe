class Rectangle:
    dlugosc: float
    szerokosc: float

    def __init__(self, dlugosc: float, szerokosc: float):
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def pole(self) -> float:
        return self.dlugosc * self.szerokosc


def main():
    test = Rectangle(10, 4)
    print(test.pole())


if __name__ == '__main__':
    main()
