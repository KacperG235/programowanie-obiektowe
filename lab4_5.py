class Wyraz:
    wyraz: str

    def __init__(self, wyraz: str = None):
        self.wyraz = wyraz

    def get_string(self, value: str) -> None:
        self.wyraz = value

    def print_string(self) -> None:
        print(self.wyraz.upper())


def main():
    test = Wyraz('siema')
    test.print_string()
    test.get_string('no tak')
    test.print_string()


if __name__ == '__main__':
    main()
