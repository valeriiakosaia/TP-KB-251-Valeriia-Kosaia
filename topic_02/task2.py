def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))

operation = input("Введіть операцію (+, -, *, /): ")

if operation == "+":
    result = add(a, b)
elif operation == "-":
    result = subtract(a, b)
elif operation == "*":
    result = multiply(a, b)
elif operation == "/":
    if b != 0:
        result = divide(a, b)
    else:
        result = "Помилка: на нуль ділити не можна."
else:
    result = "Помилка: невідома операція."

print("Результат:", result)
