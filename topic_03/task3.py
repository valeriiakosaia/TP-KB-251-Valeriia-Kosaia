student = {
    "name": "Valeriia",
    "group": "KB-251",
    "age": 19
}

print("Початковий словник:", student)

student.update({"age": 20, "city": "Chernihiv"})
print("Після update():", student)

del student["city"]
print("Після del:", student)

print("Ключі після keys():", student.keys())

print("Значення після values():", student.values())

print("Пари ключ-значення після items():", student.items())

student.clear()
print("Після clear():", student)

