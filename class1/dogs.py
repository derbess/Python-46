class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def learnTrick(self, trick):
        self.tricks.append(trick)

dog1 = Dog("Sharik")
dog2 = Dog("Eva")
dog1.learnTrick("round")
print(dog1.tricks)
print(dog2.tricks)

