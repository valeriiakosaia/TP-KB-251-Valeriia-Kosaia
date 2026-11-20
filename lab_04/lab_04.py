import re

priority = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}


def toRPN(expression):
    tokens = re.findall(r"\d+\.?\d*|[()+*/^-]", expression.replace(" ", ""))
    result = []
    stack = []

    for token in tokens:
        if token[0].isdigit():
            result.append(token)

        elif token == "(":
            stack.append(token)

        elif token == ")":
            while stack and stack[-1] != "(":
                result.append(stack.pop())
            if not stack:
                raise ValueError("Неправильні дужки")
            stack.pop()

        else:
            while stack and stack[-1] != "(":
                if priority[stack[-1]] > priority[token] or (
                    priority[stack[-1]] == priority[token] and token != "^"
                ):
                    result.append(stack.pop())
                else:
                    break

            stack.append(token)

    while stack:
        if stack[-1] == "(":
            raise ValueError("Неправильні дужки")
        result.append(stack.pop())

    return result


def calculateRPN(tokens):
    stack = []

    for token in tokens:
        if token[0].isdigit():
            stack.append(float(token))

        else:
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                result = a + b
            elif token == "-":
                result = a - b
            elif token == "*":
                result = a * b
            elif token == "/":
                result = a / b
            elif token == "^":
                result = a ** b

            stack.append(result)

    if len(stack) != 1:
        raise ValueError("Неправильний вираз")

    return stack[0]


while True:
    expression = input("\nВведіть вираз або стоп для виходу: ")

    if expression.lower() == "стоп":
        print("Програму завершено.")
        break

    try:
        tokens = toRPN(expression)
        result = calculateRPN(tokens)

        print("ЗПЗ:", " ".join(tokens))
        print("Результат:", result)

    except (ValueError, IndexError, KeyError):
        print("Помилка: неправильний вираз.")

    except ZeroDivisionError:
        print("Помилка: на нуль ділити не можна.")
