from random import randint
def get_unique_list_numbers(count=None) -> list[int]:
    start = -10
    stop = 10
    count = 15
    list_numbers = []  # Заводим список, в который будем помещать уникальные числа
    while len(list_numbers) < count:  # Заполняем список до 15 значений
        number = randint(start, stop)
        if number not in list_numbers:  # Оставляем только уникальные, отсеиваем повторения
            list_numbers.append(number)
    return list_numbers


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
#