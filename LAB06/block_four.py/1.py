array = list(map(int, input("Введите элементы массива через пробел: ").split()))

even_sum = 0  
odd_product = 1  


for i in range(len(array)):
    if i % 2 == 0:  
        even_sum += array[i]
    else: 
        odd_product *= array[i]


print(f"Сумма элементов с чётными номерами: {even_sum}")
print(f"Произведение элементов с нечётными номерами: {odd_product}")
