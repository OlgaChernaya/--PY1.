if __name__ == "__main__":
    class Clothes:
        def __init__(self, size: int, price_max: float):
            """
            Создание и подготовка к работе объекта "Одежда"
            :param size: Требуемый размер одежды
            :param price_max: Максимальная цена одежды
            Примеры:
            >>> clothes = Clothes(42, 10000)  # инициализация экземпляра класса
            """
            self.size = size
            self.price_max = price_max


        def __str__(self) -> str:
            return f"Размер {self.size}. Цена {self.price_max}"

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(name={self.size!r}, author={self.price_max!r})"

        def size_check(self, convinient_size: int) -> None:
            """
            Функция, которая проверяет соответствие одежды требуему размеру
            :convinient_size: Подходящий размер
            :return: Подходит ли одежда
            Примеры:
            >>> clothes = Clothes(42, 10000)
            >>> clothes.size_check(42)
            """
            ...

        def price_check(self, price_item: float) -> None:
            """
            Проверка подходящего ценового диапазона.
            :price_item: Цена выбранного экземпляра
            :raise ValueError: Если цена превышает допустимую, то вызываем ошибку
            Примеры:
            >>> clothes = Clothes(42, 10000)
            >>> clothes.price_check(20000)
            """


    class Dress(Clothes):
        def __init__(self, size: int, price_max: float, color: str, sale: int):
            """
            Создание и подготовка к работе объекта "Платье"
            :param size: Размер платья
            :param price_max: Максимальная цена платья
            :param color: Цвет платья
            :param sale: Клиентская скидка на платья
            Примеры:
            >>> dress = Dress(42, 10000, "black", 10)  # инициализация экземпляра класса
            """
            super().__init__(size, price_max)
            self.color = color
            self.sale = sale


        def __str__(self) -> str:
            return f"Размер {self.size}. Цена {self.price_max}. Цвет {self.color}"

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(name={self.size!r}, author={self.price_max!r}, , color={self.color!r})"

        # Методы __str__ и __repr__ перегрузили, так как в них добавили новый параметр Цвет.

        # Метод size_check может унаследоваться

        def price_check(self, price_item: float) -> None:
            """
            Проверка подходящего ценового диапазона с учетом клиентской скидки на платья.
            Добавляется новый параметр, поэтому перегружаем метод.
            :price_item: Цена на данный товар
            :raise ValueError: Если цена превышает допустимую, то вызываем ошибку
            Примеры:
            >>> dress = Dress(42, 10000, "black", 10)
            >>> dress.price_check(10000)
            """
            ...
    pass
#