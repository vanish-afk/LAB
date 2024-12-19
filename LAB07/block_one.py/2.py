import string

with open('input.txt', 'r', encoding='utf-8') as infile:
    lines = infile.readlines()

punctuation = string.punctuation

filtered_lines = [line for line in lines if any(char in punctuation for char in line)]

with open('output.txt', 'w', encoding='utf-8') as outfile:
    outfile.writelines(filtered_lines)

print("Фильтрация завершена. Результат записан в output.txt.")