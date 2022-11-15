import math


class Circle:
    r: float

    def __init__(self, r: float):
        self.r = r

    def pole(self):
        return math.pi * self.r**2

    def obwod(self):
        return 2 * math.pi * self.r

def nazwa(cos: any) -> None:
    print(type(cos))

def main():
    test = Circle(3)
    print(test.pole())
    print(test.obwod())
    nazwa(test)

if __name__ == '__main__':
    main()
