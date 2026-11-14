from functions import add, subtract, multiply, divide
import logging

def calculate():
    operation = input("Введіть операцію (+, -, *, /): ")

    if operation not in ("+", "-", "*", "/"):
        print("Помилка: невідома операція.")
        logging.info("Помилка: невідома операція %s", operation)
        return

    try:
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))

        logging.info("Введені числа: %s, %s", a, b)
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
        logging.info("Операція: %s %s %s = %s", a, operation, b, result)

    except ValueError:
        print("Помилка: потрібно ввести число.")
        logging.info("Помилка: введено неправильне число")

    except ZeroDivisionError:
        print("Помилка: на нуль ділити не можна.")
        logging.info("Помилка: спроба ділення на нуль")