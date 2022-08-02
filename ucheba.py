# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
# petr = User('Petr Petrov', 'petr@mail.ru')
# ivan = User('Ivan Ivanov', 'ivan@mail.ru')
#
# print(petr.name)
# print(petr.email)
#
# print(ivan.name)
# print(ivan.email)
#
#
# class Event:
#     def __init__(self, timestamp, event_type, session_id):
#         self.timestamp = timestamp
#         self.event_type = event_type
#         self.session_id = session_id
# events = [
#     {
#      "timestamp": 111,
#      "type": "itemViewEvent",
#      "session_id": "0:N1"
#     },
#     {
#      "timestamp": 222,
#      "type": "itemViewEvent",
#      "session_id": "0:N2"
#     },
#     {
#      "timestamp": 333,
#      "type": "itemViewEvent",
#      "session_id": "0:N3"
#     },
# ]
#
# for event in events:
#     event_obj = Event(timestamp=event.get("timestamp"),
#                       event_type=event.get("type"),
#                       session_id=event.get("session_id"))
#     print(event_obj.timestamp)


class Node: # Класс элемента
    def __init__(self, value = None, next_ = None): # инициализируем
        self.value = value # значением
        self.next = next_ # и ссылкой на следующий элемент
    def __str__(self):
        return "Node value = " + str(self.value)

class LinkedList: # Класс списка
    def __init__(self): # инициализируем пустым
        self.first = None
        self.last = None

    def clear(self): # Очищаем список
        self.__init__()

    def __str__(self): # Функция печати
        R = ''

        pointer = self.first # Берём первый указатель
        while pointer is not None: # пока указатель не станет None
            R += str(pointer.value) # добавляем значение в строку
            pointer = pointer.next # идём дальше по указателю
            if pointer is not None: # если он существует добавляем пробел
                R += ' '
        return R

    def pushleft(self, value): # добавим метод pushleft, который вставляет новый элемент в начало списка
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node = Node(value, self.first)
            self.first = new_node

    def pushright(self, value): # pushright, которая добавляет элемент в правую часть списка
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node = Node(value)
            self.last.next = new_node
            self.last = new_node

    def popleft(self):
        if self.first is None:  # если список пустой, возвращаем None
            return None
        elif self.first == self.last:  # если список содержит только один элемент
            node = self.first  # сохраняем его
            self.__init__()  # очищаем
            return node  # и возвращаем сохранённый элемент
        else:
            node = self.first  # сохраняем первый элемент
            self.first = self.first.next  # меняем указатель на первый элемент
            return node  # возвращаем сохранённый

    def popright(self):
        if self.first is None:  # если список пустой, возвращаем None
            return None
        elif self.first == self.last:  # если список содержит только один элемент
            node = self.first  # сохраняем его
            self.__init__()  # очищаем
            return node  # и возвращаем сохранённый элемент
        else:
            node = self.last  # сохраняем последний
            pointer = self.first  # создаём указатель
            while pointer.next is not node:  # пока не найдем предпоследний
                pointer = pointer.next
            pointer.next = None  # обнуляем указатели, чтобы
            self.last = pointer  # предпоследний стал последним
            return node  # возвращаем сохранённый

    def __iter__(self):  # объявляем класс как итератор
        self.current = self.first  # в текущий элемент помещаем первый
        return self  # возвращаем итератор

    def __next__(self):  # метод перехода
        if self.current is None:  # если текущий стал последним
            raise StopIteration  # вызываем исключение
        else:
            node = self.current  # сохраняем текущий элемент
            self.current = self.current.next  # совершаем переход
            return node  # и возвращаем сохранённый

    def __len__(self):
        count = 0
        pointer = self.first
        while pointer is not None:
            count += 1
            pointer = pointer.next
        return count
        print(count)

LL = LinkedList()

LL.pushright(1)
LL.pushleft(2)
LL.pushright(3)
LL.popright()
LL.pushleft(4)
LL.pushright(5)
LL.popleft()

print(LL)

# import random  # модуль, с помощью которого перемешиваем массив
#
# # пусть имеем массив всего лишь из 9 элементов
# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
#
# is_sort = False  # станет True, если отсортирован
# count = 0  # счётчик количества перестановок
#
# while not is_sort:  # пока не отсортирован
#     count += 1  # прибавляем 1 к счётчику
#
#     random.shuffle(array)  # перемешиваем массив
#
#     # проверяем, отсортирован ли
#     is_sort = True
#     for i in range(len(array) - 1):
#         if array[i] > array[i + 1]:
#             is_sort = False
#             break
#
# print(array)
# # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(count)

# n = 9
# def fact(n):
#     if (n == 1 or n == 0):
#         return 1
#     else:
#         return n * fact(n - 1)
# print("The factorial of ",n," is: ",fact(n))

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
counter = 0
for i in range(len(array)):  # проходим по всему массиву
    idx_min = i  # сохраняем индекс предположительно минимального элемента
    for j in range(i, len(array)):
        if array[j] < array[idx_min]:
            counter += 1
            idx_min = j
    if i != idx_min:  # если индекс не совпадает с минимальным, меняем
        array[i], array[idx_min] = array[idx_min], array[i]

print(counter)
print(array)

for i in range(1, len(array)):
    x = array[i]
    idx = i
    while idx > 0 and array[idx-1] > x:
        array[idx] = array[idx-1]
        counter += 1
        idx -= 1
    array[idx] = x
print(array)
