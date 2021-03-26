class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

a = Student("Derbes", 21, 3.0)
b = Student("Student", 18, 4.0)


print(a.name, a.age, a.gpa)
print(b.name, b.age, b.gpa)
