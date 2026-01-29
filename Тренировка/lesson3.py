
from user import User
from card import Card

Alex = User("Alex")

Alex.sayName()
Alex.setAge(33)
Alex.sayAge()

card = Card("1234 5678 8765 4321", "03/28", "Alex F")
Alex.addcard(card) 
Alex.getcard().pay(1000)
