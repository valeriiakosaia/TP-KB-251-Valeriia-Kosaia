
from functions import add, subtract, multiply, divide


def calculate():
    operation = input("Введіть операцію (+, -, *, /): ")

    if operation not in ("+", "-", "*", "/"):
        print("Помилка: невідома операція.")
        return

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
        print("Помилка: потрібно ввести число.")

    except ZeroDivisionError:
        print("Помилка: на нуль ділити не можна.")
