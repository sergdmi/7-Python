num_columns = 3
num_rows = 3

# def operation(x, y):
#     return x + y


# row1 = [int(i) for i in range(1, num_columns + 1)]
# print(*row1)

# for j in range(1, num_rows):
#     row_j = list(map(lambda i: i + j if i in range(2, num_columns) else i + 1, row1))
#     print(*row_j)

row1 = [int(i) for i in range(1, num_columns + 1)]
print(*row1)

for j in range(2, num_rows +1):
    row_j = []
    for i in range(1, num_columns):
        if i == 1:
              row_j.append(j)  
        row_j.append(row1[i] * j)
    print(*row_j)



