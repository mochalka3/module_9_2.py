first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Операция 1: Список длин строк, длина которых больше 5 символов
first_result = [len(s) for s in first_strings if len(s) >= 5]

# Операция 2: Список пар строк одинаковой длины
second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]

# Операция 3: Словарь строк с четной длиной
third_result = {str: len(str) for str in first_strings + second_strings if len(str) % 2 == 0}

print("first_result:", first_result)
print("second_result:", second_result)
print("third_result:", third_result)
