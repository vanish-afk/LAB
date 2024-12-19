import math
n = int(input("Введите число n: "))

for i in range(1, n + 2):  
    square = i ** 2  
    if square > n:   
        print(f"Первое число из последовательности, большее {n}: {square}")
        break  
