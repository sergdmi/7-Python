# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

import os  
os.system("cls")

 
N = int(input("N = ")) 

i = 0

for n in range(N):   
    n = 2**i    
    i+=1
    if n <= N:
        print(n)
    