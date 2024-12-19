def count_digits(n):
    
    if n < 10:
        return 1
    
    return 1 + count_digits(n // 10)


number = int(input("Введите натуральное число: "))


if number > 0:
    print(f"Количество цифр в числе {number}: {count_digits(number)}")
else:
    print("Ошибка: число должно быть натуральным (больше 0).")
