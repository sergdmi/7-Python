# 17. Дан список чисел. Определите, сколько в нем встречается различных чисел.

# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# list1 = [1, 1, 2, 0, -1, 3, 4, 4]
# print(len(set(list1)))


# 19. Дана последовательность из N целых чисел и число K. Необходимо сдвинуть
# всю последовательность (сдвиг - циклический) на K элементов вправо,
# K – положительное число.

# Input: [1, 2, 3, 4, 5] k = 2
# Output: [4, 5, 1, 2, 3]

# list1 = [1, 2, 3, 4, 5]
# list2 = []
# k = 2

# for i in range(k):
#     list2.append(list1[len(list1) - i -1])
# list2 = list2[::-1]

# for i in range(len(list1) - k):
#     list2.append(list1[i])

# print(list2)


# 21. Напишите программу для печати всех уникальных значений в словаре.

# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
# {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]

# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# list1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, {" VIII ":"S007"}]
# result_set = set()
# for i in list1:
#     for k, v in i.items():
#         result_set.add(v)
# print(result_set)

# 23. Дан массив, состоящий из целых чисел. Напишите программу, которая
# подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером)

# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

count = 0
list1= [0, -1, 5, 2, 3]
for i in range(len(list1)-1):
    if list1[i]<list1[i+1]:
        count = count+1
print(count)