# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

import os
os.system("cls")

a1 = int(input('a1 = '))
d = int(input('d = '))
n = int(input('n = '))

list_ap = [a1 + i * d for i in range(n)]

print(*list_ap)


# через цикл

# list_ap = []

# for i in range(n):
#     num = a1 + i * d
#     list_ap.append(num)

