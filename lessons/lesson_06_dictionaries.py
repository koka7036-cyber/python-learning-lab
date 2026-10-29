"""Урок 6. Словари — пары ключ: значение."""

student = {
    "name": "Ирина",
    "course": 2,
    "active": True,
}

print(student["name"])
student["course"] = 3              # изменить значение
student["city"] = "Кемерово"       # добавить ключ
print(student)

# .get() позволяет безопасно получить необязательное поле.
email = student.get("email", "не указан")
print("Почта:", email)

for key, value in student.items():
    print(f"{key}: {value}")

# Задание: создай словарь товара с названием, ценой и количеством.
