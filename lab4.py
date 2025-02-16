from typing import Union

class ConiferTree:
    """
    Базовый класс для хвойных деревьев.

    Атрибуты:
        name (str): Название дерева.
        height (float): Высота дерева в метрах.
        _age (int): Возраст дерева в годах (защищенный атрибут).
        needle_count (int): Количество иголок (по умолчанию 1_000_000).

    Методы:
        grow(years: int) -> None: Увеличивает возраст и высоту дерева.
        shed_needles() -> int: Возвращает количество сброшенных иголок.
    """

    def __init__(self, name: str, height: float, age: int) -> None:
        """
        Конструктор базового класса.
        
        Args:
            name: Название дерева.
            height: Начальная высота в метрах.
            age: Начальный возраст в годах.
        """
        self.name = name
        self.height = height
        self._age = age  # Инкапсуляция: возраст изменяется только через метод grow
        self.needle_count = 1_000_000

    def __str__(self) -> str:
        return f"{self.name} (Возраст: {self._age} лет, Высота: {self.height} м)"

    def __repr__(self) -> str:
        return f"ConiferTree(name={self.name!r}, height={self.height}, age={self._age})"

    def grow(self, years: int = 1) -> None:
        """
        Увеличивает возраст дерева и его высоту.
        
        Args:
            years: Количество лет для роста (по умолчанию 1).
        """
        self._age += years
        self.height += years * 0.5  # Усредненный годовой прирост

    def shed_needles(self) -> int:
        """Возвращает количество сброшенных за сезон иголок (10% от общего количества)."""
        shed = int(self.needle_count * 0.1)
        self.needle_count -= shed
        return shed


class Spruce(ConiferTree):
    """
    Класс для елей. Наследует атрибуты и методы ConiferTree.
    
    Дополнительные атрибуты:
        cone_count (int): Количество шишек.
    """

    def __init__(self, name: str, height: float, age: int, cone_count: int = 0) -> None:
        """
        Расширяет конструктор базового класса параметром cone_count.
        
        Args:
            cone_count: Количество шишек (по умолчанию 0).
        """
        super().__init__(name, height, age)
        self.cone_count = cone_count

    def __str__(self) -> str:
        return f"Ель {self.name} | Шишек: {self.cone_count} | {self.height} м"

    def __repr__(self) -> str:
        return f"Spruce(name={self.name!r}, height={self.height}, age={self._age}, cone_count={self.cone_count})"

    def produce_cones(self, amount: int) -> None:
        """Увеличивает количество шишек на заданное значение."""
        self.cone_count += amount


class Pine(ConiferTree):
    """
    Класс для сосен. Наследует атрибуты и методы ConiferTree.
    
    Дополнительные атрибуты:
        needle_length (float): Длина иголок в сантиметрах.
    """

    def __init__(self, name: str, height: float, age: int, needle_length: float) -> None:
        """
        Расширяет конструктор базового класса параметром needle_length.
        
        Args:
            needle_length: Длина иголок в см.
        """
        super().__init__(name, height, age)
        self.needle_length = needle_length

    def __str__(self) -> str:
        return f"Сосна {self.name} | Иглы: {self.needle_length} см | {self.height} м"

    def __repr__(self) -> str:
        return f"Pine(name={self.name!r}, height={self.height}, age={self._age}, needle_length={self.needle_length})"

    def shed_needles(self) -> int:
        """
        Перегрузка метода: сосны сбрасывают меньше иголок (5% вместо 10%).
        
        Причина: У сосен более жесткие и долговечные иглы.
        """
        shed = int(self.needle_count * 0.05)
        self.needle_count -= shed
        return shed

    def produce_resin(self) -> str:
        """Генерирует смолу (уникальный метод для сосен)."""
        return "🌲 Выделение смолы"


if __name__ == "__main__":
    # Демонстрация работы классов
    tree = ConiferTree("Хвойное", 2.5, 5)
    spruce = Spruce("Ёлка", 3.0, 7, 50)
    pine = Pine("Сосёнка", 4.2, 10, 15.5)

    print(tree)      # Хвойное (Возраст: 5 лет, Высота: 2.5 м)
    print(spruce)    # Ель Ёлка | Шишек: 50 | 3.0 м
    print(pine)      # Сосна Сосёнка | Иглы: 15.5 см | 4.2 м

    # Проверка методов
    pine.grow(2)
    print(pine.height)  # 4.2 + 2*0.5 = 5.2

    print(f"Сброшено иголок у сосны: {pine.shed_needles()}")  # 5% от 1_000_000 ≈ 50_000
    print(pine.produce_resin())  # 🌲 Выделение смолы
    pass
