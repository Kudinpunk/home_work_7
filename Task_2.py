# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

number = int(input("Введите трехзначное число: "))

number = abs(number)
if number > 99 and number < 1000:
    sum = number // 100 + number % 100 // 10 + number % 10
    print(f"Сумма цифр числа {number} = {sum}")
else:
    print("Вы ввели не трехзначное число")
