import doctest


class Dress:
    def __init__(self, size: int, price: float):
        """
        Создание и подготовка к работе объекта "Платье"
        :param size: Размер платья
        :param price: Цена платья
        Примеры:
        >>> dress = Dress(42, 10000)  # инициализация экземпляра класса
        """
        if not isinstance(size, int):
            raise TypeError("Размер платья должен быть типа int")
        if size < 40:
            raise ValueError("Размер плятья должен быть больше 40-го")
        self.size = size

        if not isinstance(price, (int, float)):
            raise TypeError("Цена платья должна быть int или float")
        if price < 0:
            raise ValueError("Цена платья не может быть отрицательным числом")
        self.price = price

    def size_check(self, convinient_size: int) -> None:
        """
        Функция, которая проверяет является ли платье подходящего размера
        :convinient_size: Подходящий размер
        :return: Подходит ли платье
        Примеры:
        >>> dress = Dress(42, 10000)
        >>> dress.size_check(42)
        """
        if not isinstance(convinient_size, int):
            raise TypeError("Подходящий размер должен быть типа int")
        if convinient_size < 40:
            raise ValueError("Размер плятья должен быть больше 40-го")
        ...

    def price_check(self, price_max: float) -> None:
        """
        Проверка подходящего ценового диапазона.
        :price_max: Максимальная цена
        :raise ValueError: Если цена превышает допустимую, то вызываем ошибку
        Примеры:
        >>> dress = Dress(42, 10000)
        >>> dress.price_check(20000)
        """
        if not isinstance(price_max, (int, float)):
            raise TypeError("Максимальная цена должна быть типа int или float")
        if price_max < 0:
            raise ValueError("Максимальная цена должна положительным числом")
        ...


class Door:
    def __init__(self, status: bool, color: str):
        """
        Создание и подготовка к работе объекта "Дверь"
        :param status: Статус двери: закрыта (True) или открыта (False)
        :param color: Цвет двери
        Примеры:
        >>> door = Door(True, "black")  # инициализация экземпляра класса
        """
        if not isinstance(status, bool):
            raise TypeError("Статус двери должен быть типа bool")
        self.status = status

        if not isinstance(color, str):
            raise TypeError("Цвет двери должен быть типа str")
        self.color = color

    def status_check(self) -> bool:
        """
        Функция, которая проверяет является ли дверь открытой
        :return: Является ли дверь открытой
        Примеры:
        >>> door = Door(True, "black")
        >>> door.status_check()
        """
        ...

    def convinient_color(self, convenient_color: str) -> None:
        """
        Функция, которая проверяет является ли дверь подходящего цвета
        :param convenient_color: Требуемый цвет двери
        :return: Подходит ли цвет двери
        Примеры:
        >>> door = Door(True, "black")
        >>> door.convinient_color()
        """
        if not isinstance(convenient_color, str):
            raise TypeError("Требуемый цвет двери должен быть типа str")
        ...


class Country:
    def __init__(self, area: float, population: int):
        """
        Создание и подготовка к работе объекта "Страна"
        :param area: Площадь страны, млн км^2
        :param population: Численность населения в стране, млн чел
        Примеры:
        >>> rus = Country(17.98, 145)  # инициализация экземпляра класса
        """
        if not isinstance(area, float):
            raise TypeError("Площадь страны должна быть типа float")
        if area <= 0:
            raise ValueError("Площадь страны должна быть положительным числом")
        self.area = area

        if not isinstance(population, int):
            raise TypeError("Численность населения должна быть типа int")
        if population < 1:
            raise ValueError("Численность населения должна быть положительным числом")
        self.population = population

    def top_population(self) -> bool:
        """
        Функция, которая проверяет входит ли страна в топ-10 по численности населения
        :return: Входит ли страна в топ-10 по численности населения
        Примеры:
        >>> rus = Country(17.98, 145)
        >>> rus.top_population()
        """
        ...

    def population_growth(self, population_growth: int) -> None:
        """
        Прирост численности населения за год
        :population_growth: Прирост населения за год
        :return: Итоговая численность населения
        Примеры:
        >>> rus = Country(17.98, 145)
        >>> rus.population_growth(5)
        """
        if not isinstance(population_growth, int):
            raise TypeError("Прирост численности населения должен быть типа int")
        if population_growth <= 0:
            raise ValueError("Прирост численности населения должен быть положительным числом")
        ...

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass
