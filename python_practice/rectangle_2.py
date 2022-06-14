from rectangle import Rectangle, Square, Circle
rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)
print(rect_1.get_area())
print(rect_2.get_area())

square_1 = Square(5)
square_2 = Square(10)
print(square_1.get_area(), square_2.get_area())

circle = Circle(10)
print(circle.get_area())

figures = [rect_1, rect_2, square_1, square_2, circle]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area())
    else:
        print(figure.get_area())