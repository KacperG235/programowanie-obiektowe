#zad 8
class Student:
    pass


class Marks:
    pass


def main():
    student1 = Student()
    student2 = Student()
    student3 = Student()
    marks1 = Marks()
    marks2 = Marks()
    marks3 = Marks()
    print(isinstance(student1, Student))
    print(isinstance(student2, Student))
    print(isinstance(student3, Student))
    print(isinstance(marks1, Student))
    print(isinstance(marks1, Marks))
    print(isinstance(marks2, Marks))
    print(isinstance(marks3, Marks))
    print(issubclass(Student, Marks))

if __name__ == '__main__':
    main()
