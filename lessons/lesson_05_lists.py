"""Урок 5. Списки и работа с ними."""

prices = [120, 250, 80, 310]
print("Все цены:", prices)
print("Первая цена:", prices[0])
print("Количество товаров:", len(prices))

prices.append(175)            # добавить элемент
prices.sort()                  # отсортировать на месте
print("После сортировки:", prices)

expensive_prices = [price for price in prices if price >= 200]
print("Цены от 200:", expensive_prices)
print("Общая сумма:", sum(prices))

# Задание: создай список из пяти чисел и выведи только положительные числа.
