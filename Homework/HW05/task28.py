# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

import os
os.system("cls")

def sum(a, b):
    if a == b == 1:
        return 2
    if a < b:
        return sum(a, b - 1) + 1
    else:
        return sum(a - 1, b) + 1

A = int(input('A = '))
B = int(input('B = '))

print('-->', sum(A, B))