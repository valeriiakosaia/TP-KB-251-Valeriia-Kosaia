numbers = [12, 5, 9, 3, 7]

print("Початковий список:", numbers)

numbers.extend([10, 7])
print("Після extend():", numbers)

numbers.append(3)
print("Після append():", numbers)

numbers.insert(2, 34)
print("Після insert():", numbers)

numbers.remove(9)
print("Після remove():", numbers)

numbers.sort()
print("Після sort():", numbers)

numbers.reverse()
print("Після reverse():", numbers)

numbers_copy = numbers.copy()
print("Копія списку після copy():", numbers_copy)

numbers.clear()
print("Після clear():", numbers)

