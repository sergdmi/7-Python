# Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

import os
os.system("cls")

def power(a, b):
    if b == 0:
        return 1
    return power(a, b - 1)*a

A = int(input('A = '))
B = int(input('B = '))

print('-->', power(A, B))
