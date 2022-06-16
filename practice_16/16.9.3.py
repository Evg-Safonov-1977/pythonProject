class Clients:

    def __init__(self, name, surname, balance):
        self.name = name
        self.surname = surname
        self.balance = balance

    def __str__(self):
        return f'Clients: Клиент: {self.name} {self.surname}. Баланс: {self.balance} руб.'

client = Clients('Иван', 'Петров', 50)
print(client)