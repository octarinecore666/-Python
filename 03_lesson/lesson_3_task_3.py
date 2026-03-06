from address import Address
from mailing import Mailing

from_addr = Address("125009", "Москва", "Тверская", "7", "15")
to_addr = Address("603000", "Нижний Новгород", "Большая Покровская", "40", "22")

mailing = Mailing(
    to_address=to_addr, from_address=from_addr, cost=350, track="RU123456789RU"
)

print(
    f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
    f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
    f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
    f"{mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей."
)
