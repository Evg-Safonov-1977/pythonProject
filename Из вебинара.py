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