import math


class SodaCan:
    def __init__(self, h: float, r: float) -> None:
        self.h = h
        self.r = r

    def get_surface_area(self) -> float:
        return round(2 * (math.pi * self.r**2) + 2 * math.pi * self.h, 2)

    def get_volume(self) -> float:
        return round((math.pi * self.r**2) * self.h, 2)


def main():
    puszka = SodaCan(3, 5)
    print(puszka.get_surface_area())
    print(puszka.get_volume())


if __name__ == "__main__":
    main()
