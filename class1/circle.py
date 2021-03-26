import math

class Circle:
    def __init__(self, r):
        self.r = r
    def perimter(self):
        return math.pi * 2 * self.r
    def area(self):
        return math.pi * self.r**2

a = Circle(5)
print(a.perimter(), a.area())