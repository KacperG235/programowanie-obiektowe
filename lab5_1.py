class American:
    nationality: str

    def __init__(self, nationality: str):
        self.nationality = nationality

    @staticmethod
    def print_nationality(nationality):
        print(nationality)

def main():
    test = American('Polack')
    print(test.nationality)
    test1 = American.print_nationality('Czech')

if __name__ == '__main__':
    main()
