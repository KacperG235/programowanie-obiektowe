class Punkt:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def distance(self, punkt) -> float:
        return ((punkt.x - self.x)**2 + (punkt.y - self.y)**2)**1/2


class NazwanyPunkt:
    def __init__(self, x: float, y: float, nazwa: str) -> None:
        self.x = x
        self.y = y
        self.nazwa = nazwa


def main():
    a = Punkt(1, 2)
    b = NazwanyPunkt(2, 6, 'B')
    print(a.distance(b))


if __name__ == "__main__":
    main()
