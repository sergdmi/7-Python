# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

import os
os.system('cls')

def print_operation_table(operation, num_rows, num_columns):

    row1 = [int(i) for i in range(1, num_columns + 1)]
    print(*row1)
    
    for j in range(2, num_rows + 1):
        row_j = []
        for i in range(1, num_columns):
            if i == 1:
                row_j.append(j)           
            row_j.append(operation(row1[i], j))
        print(*row_j)

print_operation_table(lambda x, y: x * y, 6, 6)