# Условие: Числа от 1 до 100. Каждому числу кратному 3 должно присваиваться "Fizz"
#          Каждому числу кратному 5 должно присваиваться "Bazz"
#          Каждому числу кратному 3 и 5 должно присваиваться "FizzBazz"
for i in range(1, 101):
    if i%3 == 0 and i%5 == 0:
        print("FizzBazz")
    elif i%5 == 0:
        print("Bazz")
    elif i%3 == 0:
        print("Fizz")
    else:
        print(i)

#         Тут если требуется ввод чисел
v = int(input("Введите число:"))
for i in range(1, v+1):
    if i%3 == 0 and i%5 == 0:
        print("FizzBazz")
    elif i%5 == 0:
        print("Bazz")
    elif i%3 == 0:
        print("Fizz")
    else:
        print(i)

# Создаём словарь
f = {2 : 'два', 3 : 'три'}
# Добавляем в словарь (f) новый ключ (5) и его значение (пять)
f[5] = 'пять'
# Тут указываем, что цикл ввода вручную выполняется 3 раза
for i in 1,2,3:
    # Запрашивает у пользователя ключ
    key = input()
    # Запрашивает значение
    value = input()

    if not(key in f): # Проверяет есть ли такой ключ в словаре, если его нет то
     f[key] = value    # Добавляет его


f = {2 : 'два', 3 : 'три'}
f[5] = 'пять'
for i in 1,2,3:
    key = input()
    value = input()
    if key in f:
        print(f[key])
    else:
     f[key] = value
     print(f)


# Вычисляем периметр и площадь треугольника
import math
print("Введите длины сторон треугольника")
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
p = a + b + c
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print("P=%d, S=%.2f" % (p, s))
# S=%.2f - тут указываем, что результат вычисления: число с плав.точкой (f) и после точки 2 знака
# или можно код стр.7 - 9 записать так:
# print("P=%d, S=%.2f" % (a + b + c, math.sqrt(p * (p - a) * (p - b) * (p - c))))


# Вычисляем периметр и площадь прямоугольника
print("Введите длины сторон прямоугольника")
a = int(input("a="))
b = int(input("b="))
# тут формулы для периметра и площади тоже не расписываем отдельно, а сразу их в print
print("P=%d, S=%.2f" % ((a + b) * 2, a * b))


# Вычисляем длину окружности и площадь круга
print("Введите радиус круга")
r = int(input("r="))
print("P=%2.f, S=%.2f" % (2 * math.pi * r, math.pi * r ** 2))

# ЗАДАЧА № 1
# Вычисляем периметр и площадь треугольника
import math
print("Введите длины сторон треугольника")
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
p = a + b + c
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print("P=%d, S=%.2f" % (p, s))
# S=%.2f - тут указываем, что результат вычисления: число с плав.точкой (f) и после точки 2 знака
# или можно код стр.7 - 9 записать так:
# print("P=%d, S=%.2f" % (a + b + c, math.sqrt(p * (p - a) * (p - b) * (p - c))))


# Вычисляем периметр и площадь прямоугольника
print("Введите длины сторон прямоугольника")
a = int(input("a="))
b = int(input("b="))
# тут формулы для периметра и площади тоже не расписываем отдельно, а сразу их в print
print("P=%d, S=%.2f" % ((a + b) * 2, a * b))


# Вычисляем длину окружности и площадь круга
print("Введите радиус круга")
r = int(input("r="))
print("P=%2.f, S=%.2f" % (2 * math.pi * r, math.pi * r ** 2))

print("1 - прямоугольник", "2 - треугольник", "3 - круг")
figure = input("Выберите фигуру: ")
if figure == "1":
     a = float(input("a="))
     b = float(input("b="))
     print("Площадь: %.2f" % (a * b))
elif figure == "2":
     a = float(input("a="))
     b = float(input("b="))
     c = float(input("c="))
     p = a + b + c
     s = math.sqrt(p * (p - a) * (p - b) * (p - c))
     print("Площадь: %.2f" % s)
elif figure == "3":
     r = float(input("Радиус круга R="))
     print("Площадь: %.2f" % (math.pi * r ** 2))
else:
     print("Ошибка ввода")

# ЗАДАЧА № 2
# Вычислить сумму и произведение цифр трёхзначного числа
# n = int(input("Введите трёхзначное число: "))
# nam1 = n % 10
# nam2 = n % 100 // 10
# nam3 = n // 100
# print("Сумма чисел: ", nam1 + nam2 + nam3)
# print("Произведение чисел: ", nam1 * nam2 * nam3)
#
# n = int(input("Введите трёхзначное число: "))
# nam1 = n % 10
# nam2 = n % 100 // 10
# nam3 = n // 100
# if 99 < n < 1000:
#
#     print("Сумма чисел: ", nam1 + nam2 + nam3)
#
#     print("Произведение чисел: ", nam1 * nam2 * nam3)
# else:
#     print("Введено некорректное число")

# ЗАДАЧА № 3
# Вывод среднего числа
# a = int(input('Введите число a: '))
# b = int(input('Введите число b: '))
# c = int(input('Введите число c: '))
# if (b < a < c or b > a > c):
#     print('Среднее число:', a)
# elif(a < b < c or a > b > c):
#     print('Среднее число:', b)
# else:
#     (a < c < b or a > c > b)
#     print('Среднее число:', c)


# ЗАДАЧА № 4
# Определить нечётное число
# from random import random
# a = int(random() * 100)
# b = int(random() * 100)
# if a % 2 and b % 2 or a % 2 == 0 and b % 2 == 0:
#     a += 1 # a = a + 1
# print(a, b)
# if a % 2:
#     print(a)
# else:
#     print(b)
#
#
# a = int(input('Введите число a: '))
# b = int(input('Введите число b: '))
# if a % 2 == 0:
#     print(b)
# if b % 2 == 0:
#     print(a)
# if a % 2 == 0 and b % 2 == 0:
#     print('Введённые числа чётные')

# ЗАДАЧА № 6
# Угадай число
# import random
# nam = random.randint(1, 100)
# while True:
#     print('Угадайте число от 1 до 100')
#     user_nam = int(input())
#     if user_nam == nam:
#         print('Правильно')
#         break
#     elif user_nam < nam:
#         print('Загаданное число больше')
#     elif user_nam > nam:
#         print('Загаданное число меньше')

# ЗАДАЧА № 7
# Перевернуть введённое число
# nam = int(input('Введите целое число: '))
# nam1 = 0
# while nam > 0:
#     digit = nam % 10 #последняя цифра
#     nam = nam // 10 #удаляем последнюю цифру
#     nam1 = nam1 * 10
#     nam1 = nam1 + digit
# print('Обратное ему число: ', nam1)

# ЗАДАЧА № 8
# Определить сколько чётных и нечётных цифр в введённом числе
# a = int(input("Введите число: "))
# even = 0 #even - чётные
# odd = 0 #odd - нечётные
# while a > 0:
#     if a % 2 == 0:
#         even += 1
#     else:
#         odd += 1
#     a = a // 10
# print('Чётные: %d, Нечётные: %d' % (even, odd))

# ЗАДАЧА № 8
# Написать программу "Калькулятор", которая выполняет над двумя вещественными числами
# одну из четырёх арифметических операций (+, -, *, /).
# Программа должна завершиться по желанию пользователя

# ЗАДАЧА № 9
# Вычислить фактериал циклами while и for
# n = int(input())
# factorial = 1
# while n > 1:
#     factorial *= n
#     n -= 1
# print(factorial)
#
# n = int(input())
# factorial = 1
# for i in range(2, n + 1):
#     factorial *= i
# print(factorial)

# ЗАДАЧА № 10
# Проработка на вложенный цикл на примере вывод таблицы умножения
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i * j, end="\t")
#     print("\n")

# ЗАДАЧА № 11
# Пробегаемся циклом for по последовательности, которую формирует функция range.
# Пусть начало диапазона будет 18, а конец диапазона: 1, шаг: -4
# lst = []
# for item in range(18, 1, -4):
#     lst.append(item)
# print(lst)

# ЗАДАЧА № 12
# Дан список lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20].
# Необходимо вывести элементы, которые одновременно:
# 1) меньше 30
# 2) деляться на 3 без остатка
# Все остальные элементы списка необходимо просуммировать и вывести конечный результат
# lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
# m = 30
# d_m = 3
# sm = 0
# for item in lst:
#     if(item < m) and (item % d_m == 0):
#         print(item)
#     else:
#         sm += item
# print('Сумма: ', sm)

# ЗАДАЧА № 13
# Создать функцию calc(a, b, operation). Описание входных параметров:
# 1. Первое число.
# 2. Второе число.
# 3. Действия над ними: +, -, *, /
# В остальных случаях функция должна возвращать "Операция не поддерживается".
# def calc(a, b, operation):
#     if operation == "+":
#         res = a + b
#     elif operation == "-":
#         res = a - b
#     elif operation == "*":
#         res = a * b
#     elif operation == "/":
#         if b !=0:
#             res = a / b
#         else:
#             res = "Операция не поддерживается"
#     return res
# if __name__ == '__main__':
#     print(calc(30, 15, "+"))
#     print(calc(30, 15, "-"))
#     print(calc(30, 15, "*"))
#     print(calc(30, 15, "/"))
#     print(calc(30, 0, "/"))

# ООП
# class название_класса:
#     методы_класса
# название_объекта = название_класса()
# class Person:
#     name = 'Ivan'
#     def displey_info(self):
#         print('Hi, my name is', self.name)
# person_1 = Person()
# person_1.displey_info()