"""Простой калькулятор. Можно импортировать calculate() в другие программы."""


def calculate(first: float, operator: str, second: float) -> float:
    """Выполняет арифметическую операцию или сообщает об ошибке."""
    if operator == "+":
        return first + second
    if operator == "-":
        return first - second
    if operator == "*":
        return first * second
    if operator == "/":
        if second == 0:
            raise ZeroDivisionError("На ноль делить нельзя")
        return first / second
    raise ValueError(f"Неизвестная операция: {operator}")


def main() -> None:
    print("Учебный калькулятор (+, -, *, /). Для выхода введи q.")
    while True:
        first_text = input("Первое число (или q): ").strip()
        if first_text.lower() == "q":
            print("До встречи!")
            break
        operator = input("Операция (+, -, *, /): ").strip()
        second_text = input("Второе число: ").strip()
        try:
            result = calculate(float(first_text), operator, float(second_text))
        except ValueError as error:
            print(f"Ошибка ввода: {error}")
        except ZeroDivisionError as error:
            print(f"Ошибка вычисления: {error}")
        else:
            print(f"Результат: {result:g}")


if __name__ == "__main__":
    main()
