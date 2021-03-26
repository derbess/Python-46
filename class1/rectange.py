class Rectange():
    def __init__(self, sideA, sideB):
        self.sideA = sideA
        self.sideB = sideB

    def perimetr(self):
        return (self.sideA + self.sideB) * 2
    def area(self):
        return self.sideA * self.sideB

a = Rectange(4,5)
# del a.sideB

print(a.sideB)