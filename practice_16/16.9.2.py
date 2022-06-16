# Вариант 1:
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def getA(self):
        return self.a
    def getB(self):
        return self.b
    def getArea(self):
        return self.a * self.b
    # Ниже добавил ещё метод __str__
    def __str__(self):
        return f'Rectangle: {self.getA()}, {self.getB()}, {self.getArea()}'
rectangle = Rectangle(10, 20)
print('сторона a =', rectangle.getA())
print('сторона b =', rectangle.getB())
print('площадь =', rectangle.getArea())
print('-------------')
print(rectangle)
print('-------------')
# Вариант 2:
class Rect:
    def __init__(self, c, d):
        self.c = c
        self.d = d
    def get_Area(self):
        return self.c * self.d
    def __str__(self):
        return f'Rect: Cторона c = {self.c}, Сторона d = {self.d}, Площадь = {self.get_Area()}'
rect = Rect(10, 20)
print(rect)

