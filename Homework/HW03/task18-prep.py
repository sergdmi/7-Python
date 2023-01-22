n = int(input())

# list1 = list()
# for i in range(n):
# list1.append(int(input()))

list1 = [int(input()) for i in range(n)]
k= int(input())

m = abs(k - list1[0])
number = list1[0]

for i in range(1, len(list1)):
    if m > abs(k - list1[i]):
        m = abs(k - list1[i])
        number = list1[i]

print(number)