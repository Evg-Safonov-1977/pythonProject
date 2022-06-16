# Задание 19.6.4

class Volunteers:

    def __init__(self, name, surname, city, status):
        self.name = name
        self.surname = surname
        self.city = city
        self.status = status

    def getName(self):
        return self.name

    def getSurname(self):
        return self.surname

    def getCity(self):
        return self.city

    def getStatus(self):
        return self.status