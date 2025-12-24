def square(side):
    """Вычисляет площадь квадрата. Если площадь дробная — округляет вверх."""
    area = side * side
    if area != int(area):
        area = int(area) + 1
    else:
        area = int(area)
    return area

side_input = input("Введите длину стороны квадрата: ")

# Проверяем, что ввод — число (содержит только цифры, точку и, возможно, минус)
if side_input.replace('.', '', 1).lstrip('-').isdigit() and side_input.count('.') <= 1:
    side = float(side_input)
    
    if side <= 0:
        print("Ошибка: сторона должна быть положительным числом.")
    else:
        result = square(side)
        print(f"Площадь квадрата: {result}")
else:
    print("Ошибка: введите корректное число (например, 5 или 3.14).")
