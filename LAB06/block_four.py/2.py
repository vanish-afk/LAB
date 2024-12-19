
array = list(map(int, input("Введите элементы массива через пробел: ").split()))

min_index = array.index(min(array))
max_index = array.index(max(array))


array[min_index], array[max_index] = array[max_index], array[min_index]


print("Массив после перестановки минимального и максимального элементов:")
print(array)
