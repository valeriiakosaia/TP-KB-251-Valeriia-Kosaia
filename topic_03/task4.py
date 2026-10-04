def find_position(numbers, new_element):
    for i in range(len(numbers)):
        if new_element <= numbers[i]:
            return i

    return len(numbers)


numbers = [1, 4, 8, 14, 17]

print("Відсортований список:", numbers)

new_element = int(input("Введіть новий елемент: "))

position = find_position(numbers, new_element)

print("Позиція для вставки:", position)

numbers.insert(position, new_element)

print("Список після вставки:", numbers)

