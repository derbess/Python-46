class Person:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def walk(self):
        return "I am walking"
    def eat(self):
        return "I am eating"
    def think(self):
        return "I think"

class Teacher(Person):
    def __init__(self, name, age, weight, height, exp):
        super().__init__(name, age, weight, height)
        self.exp = exp
    def teach(self):
        return "Teach"

teacher1 = Teacher("Name", 46, 70, 175, 10)

print(teacher1.eat())