from functions import Calculator

def calculate():
    calc = Calculator()

    operation = input("Введіть операцію (+, -, *, /): ")

    if operation not in ("+", "-", "*", "/"):
        print("Помилка: невідома операція.")
        return

    try:
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))

        match operation:
            case "+":
                result = calc.add(a, b)
            case "-":
                result = calc.subtract(a, b)
            case "*":
                result = calc.multiply(a, b)
            case "/":
                result = calc.divide(a, b)

        print("Результат:", result)

    except ValueError:
        print("Помилка: потрібно ввести число.")

    except ZeroDivisionError:
        print("Помилка: на нуль ділити не можна.")
