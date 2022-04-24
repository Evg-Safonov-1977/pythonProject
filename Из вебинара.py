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