list1 = [int(i) for i in input().split()]

list2 = [ (i, i*i) for i  in list1 if i % 2 == 0]

print(list2)