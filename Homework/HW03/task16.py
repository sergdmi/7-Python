# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

import os  
os.system("cls")

N = int(input('N = '))

A = []

for i in range(N):
    A.append(int(input()))

X = int(input('X = '))
count = 0

for j in A:
    if j == X:
        count += 1

print('-->', count)
