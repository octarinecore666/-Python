def is_year_leap(year):
    return year % 4 == 0

year_input = input("Введите год: ")
year = int(year_input)

result = is_year_leap(year)

print("год " + str(year) + ": " + str(result))