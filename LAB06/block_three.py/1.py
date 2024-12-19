text = input("Введите строку: ")
words = text.split()
words_ending_with_ya = [word for word in words if word.endswith("я") or word.endswith("Я")]
print("Слова, оканчивающиеся на 'я':")
print(", ".join(words_ending_with_ya) if words_ending_with_ya else "Таких слов нет.")
