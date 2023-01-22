# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.


import os  
os.system("cls")

n = int(input('n = '))
m = int(input('m = '))

list_n = set([int(input()) for i in range(n)])
print(list_n)

list_m = set([int(input()) for i in range(m)])
print(list_m)

list_res = [int(i) for i in list_n.intersection(list_m)]


print(sorted(list_res))


# сортировка при помощи цикла

# for i in range(len(list_res)-1):
#     for j in range(len(list_res)- i -1):
#         if list_res[j] > list_res[j + 1]:
#             temp = list_res[j]
#             list_res[j] = list_res[j + 1]
#             list_res[j + 1] = temp 

# print(list_res)
        