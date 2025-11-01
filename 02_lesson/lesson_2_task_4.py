def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
n_input = input("Введите число n: ")            
if n_input.isdigit() and len(n_input) > 0:
    n = int(n_input)
    if n > 0:
        fizz_buzz(n)
    else:
        print("Ошибка: число должно быть больше нуля.")
else:
    print("Ошибка: введите положительное целое число.")