def month_to_season(month):
    if month in (12, 1, 2):
        return "Зима"
    elif month in (3, 4, 5):
        return "Весна"
    elif month in (6, 7, 8):
        return "Лето"
    elif month in (9, 10, 11):
        return "Осень"
    else:
        return "Ошибка: введите число от 1 до 12"


month_input = input("Введите номер месяца (от 1 до 12): ")

if month_input.isdigit():
    month = int(month_input)
    result = month_to_season(month)
    print(result)
else:
    print("Ошибка: введите целое число от 1 до 12")
