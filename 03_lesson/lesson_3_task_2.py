from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Samsung", "Galaxy S23", "+79991234567"))
catalog.append(Smartphone("Apple", "iPhone 13 Pro", "+79887654321"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 11", "+79776543210"))
catalog.append(Smartphone("Huawei", "P60 Pro", "+79665432109"))
catalog.append(Smartphone("OnePlus", "11", "+79554321098"))

for smartphone in catalog:
    print(smartphone)
    