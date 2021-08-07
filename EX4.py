class Student:
    def __init__(self, student, grade):
        self.student = student
        self.grade = grade

    def name(self):
        return self.student

    def get_grade(self):
        return self.grade


name = input("姓名 = ")
grade = int(input("成績 = "))
s1 = Student(name, grade)
print("s1.name = {}".format(s1.name()))