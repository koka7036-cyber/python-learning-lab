"""Урок 3. Циклы for и while."""

print("Числа от 1 до 5:")
for number in range(1, 6):
    print(number)

print("Сумма чисел от 1 до 5:")
total = 0
for number in range(1, 6):
    total += number
print(total)  # 15

# while повторяется, пока условие истинно.
countdown = 3
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Старт!")

# Задание: посчитай сумму всех чётных чисел от 2 до 20 включительно.
