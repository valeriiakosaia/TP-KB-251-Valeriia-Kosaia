
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("На нуль ділити не можна.")
    return a / b


while True:
    operation = input("Введіть операцію (+, -, *, /) або exit для виходу: ")

    if operation == "exit":
        print("Програму завершено.")
        break

    if operation not in ("+", "-", "*", "/"):
        print("Помилка: невідома операція.")
        continue

    try:
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))

        match operation:
            case "+":
                result = add(a, b)
            case "-":
                result = subtract(a, b)
            case "*":
                result = multiply(a, b)
            case "/":
                result = divide(a, b)

        print("Результат:", result)

    except ValueError:
        print("Помилка: потрібно вводити числа.")

    except ZeroDivisionError as error:
        print("Помилка:", error)
