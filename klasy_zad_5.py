class Student:
    def __init__(self, imie: str, nazwisko: str, cal_wynik_quizow: int, quizy=1) -> None:
        self.imie = imie
        self.nazwisko = nazwisko
        self.cal_wynik_quizow = cal_wynik_quizow
        self.quizy = quizy

    def get_name(self):
        return self.imie

    def add_quiz(self, score: int) -> None:
        self.cal_wynik_quizow += score
        self.quizy += 1

    def get_total_score(self) -> float:
        return self.cal_wynik_quizow

    def get_average_score(self):
        return self.cal_wynik_quizow / self.quizy


def main():
    student = Student("Kacper", "Gutowski", 10, 2)
    print(student.get_name())
    student.add_quiz(8)
    print(student.get_total_score())
    print(student.get_average_score())


if __name__ == "__main__":
    main()
