first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Переменная first_result: список длин строк из first_strings длиной не менее 5 символов
first_result = [len(s) for s in first_strings if len(s) >= 5]

# Переменная second_result: список кортежей с парами слов одинаковой длины из first_strings и second_strings
second_result = [(f, s) for f in first_strings for s in second_strings if len(f) == len(s)]

# Переменная third_result: словарь с ключом-значением строка-длина строки (для строк четной длины)
combined_strings = first_strings + second_strings
third_result = {s: len(s) for s in combined_strings if len(s) % 2 == 0}

# Вывод результатов
print(first_result)
print(second_result)
print(third_result)
