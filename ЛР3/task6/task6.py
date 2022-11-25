list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_index = 0
max_num_index = list_numbers[max_index]

for i, current_num in enumerate(list_numbers):  # перебераем пары индекс - значение
    if current_num >= max_num_index:  # если текущее число больше или равно того, который встречали ранее
        max_index = i  # то перезаписываем индекс максимального числа
        max_num_index = list_numbers[max_index]  # и перезаписываем число

last_index = len(list_numbers)-1  # индекс последнего числа

list_numbers[max_index], list_numbers[last_index] = list_numbers[last_index], list_numbers[max_index]
# меняяем местами элементы с индексами последнего максимального и последнего элемента

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
