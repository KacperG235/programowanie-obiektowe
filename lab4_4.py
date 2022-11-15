#zad 10
class Student:
    student_id = 166266
    student_name = 'Kacper'


def main():
    #zad 11
    test = Student()
    print(test.student_id)
    print(test.student_name)
    setattr(Student, 'student_class', 2)
    print(test.student_id)
    print(test.student_name)
    print(test.student_class)
    delattr(Student, 'student_name')
    print(test.student_id)
    print(test.student_class)


if __name__ == '__main__':
    main()
