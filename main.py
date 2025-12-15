text = "Python-разработчик учится использовать стандартную библиотеку."
num = [2, 5, 8, 3, 2, 8, 10]

# Работа со строками
count_word = text.count('библиотеку')
first_index = text.find('Python')
starts_with_word = text.startswith('Python')
replace_word = text.replace('стандартную', 'встроенную')

# Работа с числами
sum_num = sum(num)
max_num = max(num)
count_num = num.count(8)
unique_num = set(num)  # сохраняем уникальные числа в отдельной переменной

# Запись результатов в файл
with open('results.txt', 'w', encoding='utf-8') as f:
    f.write(f"Текст: {text}\n")
    f.write(f"Слово 'библиотеку' встречается: {count_word} раз\n")
    f.write(f"Индекс слова 'Python': {first_index}\n")
    f.write(f"Начинается ли текст с 'Python': {starts_with_word}\n")
    f.write(f"Замена слова: {replace_word}\n")
    f.write(f"Сумма чисел: {sum_num}\n")
    f.write(f"Максимум: {max_num}\n")
    f.write(f"Число 8 встречается: {count_num} раз\n")
    f.write(f"Уникальные числа: {unique_num}\n")

# Печать результатов в консоль
print("Результаты работы программы:")
print(f"Текст: {text}")
print(f"Слово 'библиотеку' встречается: {count_word} раз")
print(f"Индекс слова 'Python': {first_index}")
print(f"Начинается ли текст с 'Python': {starts_with_word}")
print(f"Замена слова: {replace_word}")
print(f"Сумма чисел: {sum_num}")
print(f"Максимум: {max_num}")
print(f"Число 8 встречается: {count_num} раз")
print(f"Уникальные числа: {unique_num}")

import os
print(os.getcwd())  # покажет, где Python пытается создать файл
