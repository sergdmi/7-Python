# Задача 32: Определить элементы массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import os
os.system('cls')

list_x = [int(i) for i in (input()).split()]

min = int(input('min = '))
max = int(input('max = '))

list_y = [i for i in list_x if min <= i <= max]

print (*list_y)


# через цикл
# list_y = []
# for i in range(len(list_x)):
#     if min <= list_x[i] <= max:
#         list_y.append(list_x[i])

# если нужно вывести только значения списка в диапазоне (min, max) а не все элементы

# list_y = set([i for i in list_x if min <= i <= max]) 


# Задача 32 (первоначальный вариант): Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# import os
# os.system('cls')

# list_x = [int(i) for i in (input()).split()]

# min = int(input('min = '))
# max = int(input('max = '))

# list_y = [i for i in range(len(list_x)) if min <= list_x[i] <= max]

# print (*list_y)