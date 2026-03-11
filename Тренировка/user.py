class User:
    age = 0

    def __init__(self, name):
        print("Я создался")
        self.userName = name

    def sayName(self):
        print("Вас зовут ", self.userName)

    def sayAge(self):
        print(self.age)

    def setAge(self, newAge):
        self.age = newAge

    def addcard(self, card):
        self.card = card

    def getcard(self):
        return self.card
