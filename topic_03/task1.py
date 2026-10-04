def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


while True:
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))

    operation = input("Введіть операцію (+, -, *, /) або exit для виходу: ")

    if operation == "exit":
        print("Програму завершено.")
        break

    match operation:
        case "+":
            result = add(a, b)
        case "-":
            result = subtract(a, b)
        case "*":
            result = multiply(a, b)
        case "/":
            if b != 0:
                result = divide(a, b)
            else:
                result = "Помилка: на нуль ділити не можна."
        case _:
            result = "Помилка: невідома операція."

    print("Результат:", result)