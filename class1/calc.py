class Calculator():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    def minus(self):
        return self.a - self.b
    def multiply(self):
        return self.a * self.b
    def division(self):
        return self.a / self.b

calc1 = Calculator(12,3)
calc1.a = 20
print(calc1.add())
print(calc1.minus())
print(calc1.multiply())
print(calc1.division())