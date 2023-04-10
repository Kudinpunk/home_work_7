# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, 
# вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

number_ticket = int(input('Введите номер билета: '))
if number_ticket > 99999 and number_ticket < 1000000:
    fisrt_number = number_ticket // 1000
    sum_1 = fisrt_number // 100 + fisrt_number % 100 // 10 + fisrt_number % 10
    second_number = number_ticket % 1000
    sum_2 = second_number // 100 + second_number % 100 // 10 + second_number % 10

    print('YES, your ticket is happy') if sum_1 == sum_2 else print('NO, try again')
else:
    print("Проверьте ввод чисел билета")