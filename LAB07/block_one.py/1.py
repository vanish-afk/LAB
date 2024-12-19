import pickle

medals_dict = {
    'США': [46, 37, 36, 47, 39, 51],
    'Китай': [38, 31, 26, 38, 42, 38],
    'Россия': [30, 24, 33, 29, 27, 56],
    'Великобритания': [27, 24, 17, 22, 67, 65],
    'Германия': [33, 35, 29, 29, 24, 27],
    'Япония': [12, 14, 12, 11, 27, 58],
    'Франция': [26, 27, 40, 35, 33, 31],
}

total_medals = {}
for country, medals in medals_dict.items():
    total_medals[country] = sum(medals)

print("Список стран и суммарное количество медалей:")
for country, total in total_medals.items():
    print(f"{country}: {total}")

average_medals = {country: sum(medals) / len(medals) for country, medals in medals_dict.items()}
max_country = max(average_medals, key=average_medals.get)
min_country = min(average_medals, key=average_medals.get)

print(f"\nСтрана с максимальным средним числом медалей: {max_country} ({average_medals[max_country]:.2f})")
print(f"Страна с минимальным средним числом медалей: {min_country} ({average_medals[min_country]:.2f})")

max_medal_years = {}
for country, medals in medals_dict.items():
    max_medal_years[country] = medals.index(max(medals)) + 1  

print("\nГод, в котором страна завоевала наибольшее количество медалей:")
for country, year in max_medal_years.items():
    print(f"{country}: Олимпийские игры {year}")

initial_medals = {country: medals[0] for country, medals in medals_dict.items()}
growth_countries = {country: medals for country, medals in medals_dict.items() if (medals[-1] - initial_medals[country]) / initial_medals[country] > 0.2}

print("\nСтраны с ростом медалей более чем на 20%:")
for country in growth_countries:
    print(country)

with open('data.pickle', 'wb') as f:
    pickle.dump(medals_dict, f)

with open('data.pickle', 'rb') as f:
    loaded_medals_dict = pickle.load(f)

print("\nДанные, загруженные из бинарного файла:")
print(loaded_medals_dict)