# Задача 2: Найдите сумму цифр трехзначного числа.

N = int(input('N = '))

a = N // 100
b = (N // 10) % 10
c = N % 10


print ('Сумма чисел =', a + b + c)