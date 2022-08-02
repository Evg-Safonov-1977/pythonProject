# проверяемая последовательность чисел, введенная через пробел
sequence_of_numbers = list(map(int, input('Введите через пробел числа больше 2: ').split()))
print('sequence_of_numbers', sequence_of_numbers, type(sequence_of_numbers))

# 1. Преобразование введённой последовательности в список
element = int(input('Введите любое произвольное число: '))
print('element', element, type(element))
array = sequence_of_numbers + [element]  # соединение последовательности чисел и произвольного числа в массив
print('array', array, type(array))

# 2.Сортировка списка по возрастанию элементов в нем (для реализации сортировки определена функция)
def qsort(array, left, right):
    middle = (left + right) // 2

    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)


qsort(array, 0, len(array) - 1)
print(qsort(array, 0, len(array) - 1))

print(sequence_of_numbers, type(sequence_of_numbers))
print(element, type(element))
print(array, type(array))

# # 3.Установка позиции элемента алгоритмом двоичного поиска. Реализован отдельной функцией.
def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находим середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)
# запускаем алгоритм на левой и правой границе

print(binary_search(array, element, 0, len(array)-1))