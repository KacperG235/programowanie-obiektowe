import array
import builtins


class Test:

    def __init__(self, liczba1: int = 0, liczba2: int = 0):
        self.liczba1 = liczba1
        self.liczba2 = liczba2


class Student:

    def __init__(self, nazwa_ucznia: str, klasa_ucznia: str, student_id: int):
        self.nazwa_ucznia = nazwa_ucznia
        self.klasa_ucznia = klasa_ucznia
        self.student_id = student_id

    def student_data(self, nazwa: str = None, klasa: str = None) -> None:
        print(self.student_id)
        if nazwa is not None:
            print(self.nazwa_ucznia)
        if klasa is not None:
            print(self.klasa_ucznia)


def main():
    #zad 1:
    print(dir(array.__dict__))
    #zad 2:
    print(dir(Test.__dict__))
    #zad 3:
    test = Test()
    print(dir(test.__dict__))
    #zad 4:
    help(builtins.abs)
    print(builtins.abs(-155))
    #zad 5
    testowy_student = Student('Krzystof', 'Kononowicz', 172137)
    print(testowy_student.nazwa_ucznia)
    print(testowy_student.klasa_ucznia)
    print(testowy_student.student_id)
    #zad 6
    testowy_student.student_data()
    testowy_student.student_data('krzysiek', 'notak')
    #zad 7
    print(type(Student))
    print(dir(Student.__dict__))
    print(dir(Student.__module__))


if __name__ == "__main__":
    main()
