"""Урок 4. Функции, параметры и return."""


def greet(name: str) -> str:
    """Возвращает приветствие для указанного имени."""
    return f"Привет, {name}!"


def rectangle_area(width: float, height: float) -> float:
    """Вычисляет площадь прямоугольника."""
    if width < 0 or height < 0:
        raise ValueError("Стороны не могут быть отрицательными")
    return width * height


print(greet("Алексей"))
print(f"Площадь: {rectangle_area(4, 3)}")

# Задание: напиши функцию is_even(number), которая возвращает True для чётного числа.
