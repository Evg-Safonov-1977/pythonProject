# def par_checker(string):
#     stack = []  # инициализируем стек
#
#     for s in string:  # читаем строку посимвольно
#         if s == "(":  # если открывающая скобка,
#             stack.append(s)  # добавляем её в стек
#         elif s == ")":
#             # если встретилась закрывающая скобка, то проверяем
#             # пуст ли стек и является ли верхний элемент — открывающей скобкой
#             if len(stack) > 0 and stack[-1] == "(":
#                 stack.pop()  # удаляем из стека
#             else:  # иначе завершаем функцию с False
#                 return False
#     # если стек пустой, то незакрытых скобок не осталось
#     # значит, возвращаем True, иначе — False
#     return len(stack) == 0
#
#
# pars = {")": "(", "]": "["}
#
#
# def par_checker_mod(string):
#     stack = []
#
#     for s in string:
#         if s in "([":
#             stack.append(s)
#         elif s in ")]":
#             if len(stack) > 0 and stack[-1] == pars[s]:
#                 stack.pop()
#             else:
#                 return False
#     return len(stack) == 0


# # Создадим класс Queue - нужная нам очередь
# class Queue:
#     # Конструктор нашего класса, в нём происходит нужная инициализация объекта
#     def __init__(self, max_size):
#         self.max_size = max_size  # размер очереди
#         self.task_num = 0  # будем хранить сквозной номер задачи
#
#         self.tasks = [0 for _ in range(self.max_size)]  # инициализируем список с нулевыми элементами
#         self.head = 0  # указатель на начало очереди
#         self.tail = 0  # указатель на элемент следующий за концом очереди
#
#     # !!! Класс далее нужно дополнить методами !!!
#     def is_empty(self):  # очередь пуста?
#         # да, если указатели совпадают и в них содержится ноль
#         return self.head == self.tail and self.tasks[self.head] == 0
#
#     def size(self):  # получаем размер очереди
#         if self.is_empty():  # если она пуста
#             return 0  # возвращаем ноль
#         elif self.head == self.tail:  # иначе, если очередь не пуста, но указатели совпадают
#             return self.max_size  # значит очередь заполнена
#         elif self.head > self.tail:  # если хвост очереди сместился в начало списка
#             return self.max_size - self.head + self.tail
#         else:  # или если хвост стоит правее начала
#             return self.tail - self.head
#
#     def add(self):
#         self.task_num += 1  # увеличиваем порядковый номер задачи
#         self.tasks[self.tail] = self.task_num  # добавляем его в очередь
#         print(f"Задача №{self.tasks[self.tail]} добавлена")
#
#         # увеличиваем указатель на 1 по модулю максимального числа элементов
#         # для зацикливания очереди в списке
#         self.tail = (self.tail + 1) % self.max_size
#
#     def show(self):  # выводим приоритетную задачу
#         print(f"Задача №{self.tasks[self.head]} в приоритете")
#
#     def do(self):  # выполняем приоритетную задачу
#         print(f"Задача №{self.tasks[self.head]} выполнена")
#         # после выполнения зануляем элемент по указателю
#         self.tasks[self.head] = 0
#         # и циклично перемещаем указатель
#         self.head = (self.head + 1) % self.max_size
#
# # Используем класс
# size = int(input("Определите размер очереди: "))
# q = Queue(size)
#
# while True:
#     cmd = input("Введите команду:")
#     if cmd == "empty":
#         if q.is_empty():
#             print("Очередь пустая")
#         else:
#             print("В очереди есть задачи")
#     elif cmd == "size":
#         print("Количество задач в очереди:", q.size())
#     elif cmd == "add":
#         if q.size() != q.max_size:
#             q.add()
#         else:
#             print("Очередь переполнена")
#     elif cmd == "show":
#         if q.is_empty():
#             print("Очередь пустая")
#         else:
#             q.show()
#     elif cmd == "do":
#         if q.is_empty():
#             print("Очередь пустая")
#         else:
#             q.do()
#     elif cmd == "exit":
#         for _ in range(q.size()):
#             q.do()
#         print("Очередь пустая. Завершение работы")
#         break
#     else:
#         print("Введена неверная команда")


G = {"Адмиралтейская" :
         {"Садовая" : 4},
     "Садовая" :
         {"Сенная площадь" : 3,
          "Спасская" : 3,
          "Адмиралтейская" : 4,
          "Звенигородская" : 5},
     "Сенная площадь" :
         {"Садовая" : 3,
          "Спасская" : 3},
     "Спасская" :
         {"Садовая" : 3,
          "Сенная площадь" : 3,
          "Достоевская" : 4},
     "Звенигородская" :
         {"Пушкинская" : 3,
          "Садовая" : 5},
     "Пушкинская" :
         {"Звенигородская" : 3,
          "Владимирская" : 4},
     "Владимирская" :
         {"Достоевская" : 3,
          "Пушкинская" : 4},
     "Достоевская" :
         {"Владимирская" : 3,
          "Спасская" : 4}}
# D = {k : 100 for k in G.keys()} # расстояния
# start_k = 'Адмиралтейская' # стартовая вершина
# D[start_k] = 0 # расстояние от неё до самой себя равно нулю
# U = {k : False for k in G.keys()} # флаги просмотра вершин
#
# for _ in range(len(D)):
#     # выбираем среди непросмотренных наименьшее по расстоянию
#     min_k = min([k for k in U.keys() if not U[k]], key = lambda x: D[x])
#
#     for v in G[min_k].keys(): # проходимся по всем смежным вершинам
#         D[v] = min(D[v], D[min_k] + G[min_k][v]) # минимум
#     U[min_k] = True # просмотренную вершину помечаем
# print(D)


# Модифицируйте алгоритм Дейкстры таким образом,
# что в массив P по соответствующему ключу будет записываться
# предок с минимальным расстоянием, если это необходимо.
D = {k : 100 for k in G.keys()} # расстояния
start_k = 'Адмиралтейская' # стартовая вершина
D[start_k] = 0 # расстояние от нее до самой себя равно нулю
U = {k : False for k in G.keys()} # флаги просмотра вершин
P = {k : None for k in G.keys()} # предки

for _ in range(len(D)):
    # выбираем среди непросмотренных наименьшее по расстоянию
    min_k = min([k for k in U.keys() if not U[k]], key = lambda x: D[x])

    for v in G[min_k].keys(): # проходимся по всем смежным вершинам
         if D[v] > D[min_k] + G[min_k][v]: # если расстояние от текущей вершины меньше
            D[v] = D[min_k] + G[min_k][v] # то фиксируем его
            P[v] = min_k # и записываем как предок
    U[min_k] = True # просмотренную вершину помечаем

print(D)
# Теперь проходом цикла while по вершинам в словаре P можно найти вершины кратчайшего пути, правда, в обратном порядке:
pointer = "Владимирская" # куда должны прийти
while pointer is not None: # перемещаемся, пока не придём в стартовую точку
    print(pointer)
    pointer = P[pointer]


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, next_value):
        if self.left_child is None:
            self.left_child = BinaryTree(next_value)
        else:
            new_child = BinaryTree(next_value)
            new_child.left_child = self.left_child
            self.left_child = new_child
        return self

    def insert_right(self, next_value):
        if self.right_child is None:
            self.right_child = BinaryTree(next_value)
        else:
            new_child = BinaryTree(next_value)
            new_child.right_child = self.right_child
            self.right_child = new_child
        return self

node_root = BinaryTree(2).insert_left(7).insert_right(5)
    # левое поддерево корня /2|7|6\
node_7 = node_root.left_child.insert_left(2).insert_right(6)
    # правое поддерево предыдущего узла /5|6|11\
node_6 = node_7.right_child.insert_left(5).insert_right(11)
    # правое поддерево корня /|5|9\
node_5 = node_root.right_child.insert_right(9)
    # левое поддерево предыдущего узла корня /4|9|\
node_9 = node_5.right_child.insert_left(4)

def pre_order(self):
    print(self.value)  # процедура обработки

    if self.left_child is not None:  # если левый потомок существует
        self.left_child.pre_order()  # рекурсивно вызываем функцию

    if self.right_child is not None:  # если правый потомок существует
        self.right_child.pre_order()  # рекурсивно вызываем функцию

def post_order(self):
    if self.left_child is not None:  # если левый потомок существует
        self.left_child.post_order()  # рекурсивно вызываем функцию

    if self.right_child is not None:  # если правый потомок существует
        self.right_child.post_order()  # рекурсивно вызываем функцию
    node_root.in_order()
    print(self.value)  # процедура обработки