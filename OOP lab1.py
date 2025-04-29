import doctest


class Object:
    """
    Абстрактный класс, описывающий объект.
    """

    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color

    def move(self, destination: str) -> None:
        """
        Перемещает объект в указанное место.

        Пример использования:
        >>> obj = Object('Object1', 'red')
        >>> obj.move('table')
        """

    def change_color(self, new_color: str) -> None:
        """
        Меняет цвет объекта.

        Пример использования:
        >>> obj = Object('Object1', 'red')
        >>> obj.change_color('blue')
        """


class LivingBeing(Object):
    """
    Абстрактный класс, описывающий живое существо.
    """

    def __init__(self, name: str, color: str, age: int):
        super().__init__(name, color)
        self.age = age

    def eat(self, food: str) -> None:
        """
        Живое существо ест указанную пищу.

        Пример использования:
        >>> living_being = LivingBeing('LivingBeing1', 'green', 5)
        >>> living_being.eat('grass')
        """


class Device(Object):
    """
    Абстрактный класс, описывающий устройство.
    """

    def __init__(self, name: str, color: str, power_source: str):
        super().__init__(name, color)
        self.power_source = power_source


if __name__ == "__main__":
    doctest.testmod()
