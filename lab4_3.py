#zad 9
class Student:
    student_name = 'Kacper'
    marks = 50


def main():
    test = Student()
    print(test.student_name)
    print(test.marks)
    setattr(Student, 'student_name', 'Krzysztof')
    setattr(Student, 'marks', 100)
    print(test.student_name)
    print(test.marks)


if __name__ == '__main__':
    main()
