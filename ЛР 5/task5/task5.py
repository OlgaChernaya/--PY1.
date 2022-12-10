import string
from random import sample
def get_random_password(count=8) -> str:
    list_population = [d for d in str(string.ascii_uppercase + string.ascii_lowercase + string.digits)]
    # Заводим объединенный список возможных символов
    list_password = sample(list_population, count)  # Генерируем пароль
    return "".join(str(d) for d in list_password)  # Выводим пароль в виде строки


print(get_random_password())
#