import os
os.system("cls")

list1 = [int(input()) for i in range(int(input()))]

count = 0
for i in range(1, len(list1)-1):
    if list1[i-1] < list1[i] > list1[i+1]:
        count +=1

print(count)