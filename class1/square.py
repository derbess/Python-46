class Square:
    def __init__(self, side):
        self.side = side
    def perimetr(self):
        return self.side * 4
    def area(self):
        return self.side**2


a = Square(5)
print(a.perimetr()) # 20
print(a.area()) #25