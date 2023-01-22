# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

import os  
os.system("cls")

N = int(input('N = '))

# A = []

# for i in range(N):
#     A.append(int(input()))

A = [int(input()) for i in range(N)]

X = int(input('X = '))

n = A[0]

for j in range(len(A)):    

    
    if abs(X-A[j]) <= abs(X-n) and A[j] != X:
        n = A[j]
           
print('-->', n)
 
