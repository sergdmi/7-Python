# 31.Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 8
# Задание необходимо решать через рекурсию

# 0 1 2 3 4 5 6 7  8
# 0 1 1 2 3 5 8 13 21


# def f(n):
#     if n == 0 or n == 1:
#         return n
#     return f(n - 1) + f(n - 2)

# n = int(input())
# print(f(n))

# 33. Хакер Василий получил доступ к классному журналу и хочет заменить 
# все свои минимальные оценки на максимальные. Напишите программу, которая 
# заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# n = int(input('Введите количество оценок  '))
# list1 = [int(input()) for i in range(n)]
# print(list1)

# maxM = 0
# minM = list1[0]
# for i in list1:
#     if i>maxM:
#         maxM=i
#     if i<minM:
#         minM=i
# for i in range(len(list1)):
#     if list1[i]==maxM:
#         list1[i]=minM
# print(list1)

#другое решение

# list1 = [int(i) for i in input().split()]
# max_n = max(list1)
# min_n = min(list1)
# list1 = [min_n if list1[i] == max_n else list1[i] for i in range(len(list1))]
# print(list1)

# 35. Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)

# Input: 5
# Output: yes

# def prime(n):
#     i = 2
#     flag = True
#     while i < n and flag:
#         if n % i == 0:
#             flag = False 
#         i += 1
#     if flag:
#         return 'yes'
#     return 'no'

# print(prime(int(input())))

# 35. Дано натуральное число N и последовательность из N элементов.
#  Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

# Input:    2 -> 3 4
# Output: 4 3

def f(n):
    if n==0:
        return ''
    k=int(input())
    return f(n-1)+f' {str(k)}'

n = int(input('введите число n  '))
print(f(n))
