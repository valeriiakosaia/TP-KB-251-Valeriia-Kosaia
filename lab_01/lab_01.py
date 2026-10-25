
list = [
    {"name": "Bob", "surname": "Smith", "group": "КБ-251", "phone": "0631234567"},
    {"name": "Emma", "surname": "Brown", "group": "КБ-251", "phone": "0632345678"},
    {"name": "Jon", "surname": "Wilson", "group": "КБ-251", "phone": "0633456789"},
    {"name": "Zak", "surname": "Taylor", "group": "КБ-251", "phone": "0634567890"}
]


def printAllList():
    for elem in list:
        strForPrint = (
            "Ім'я: " + elem["name"] +
            ", Прізвище: " + elem["surname"] +
            ", Група: " + elem["group"] +
            ", Телефон: " + elem["phone"]
        )
        print(strForPrint)
    return


def addNewElement():
    name = input("Введіть ім'я студента: ")
    surname = input("Введіть прізвище студента: ")
    group = input("Введіть групу студента: ")
    phone = input("Введіть номер телефону: ")

    newItem = {
        "name": name,
        "surname": surname,
        "group": group,
        "phone": phone
    }

    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break

    list.insert(insertPosition, newItem)
    print("Студента успішно додано!")
    return


def deleteElement():
    name = input("Введіть ім'я студента для видалення: ")
    deletePosition = -1

    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break

    if deletePosition == -1:
        print("Студента не знайдено!")
    else:
        print("Позиція видалення: " + str(deletePosition))
        del list[deletePosition]
        print("Студента успішно видалено!")
    return


def updateElement():
    name = input("Введіть ім'я студента для редагування: ")
    updatePosition = -1

    for item in list:
        if name == item["name"]:
            updatePosition = list.index(item)
            break

    if updatePosition == -1:
        print("Студента не знайдено!")
    else:
        print("Студента знайдено. Введіть нові дані:")

        newName = input("Введіть нове ім'я: ")
        newSurname = input("Введіть нове прізвище: ")
        newGroup = input("Введіть нову групу: ")
        newPhone = input("Введіть новий номер телефону: ")

       
        del list[updatePosition]

        
        newItem = {
            "name": newName,
            "surname": newSurname,
            "group": newGroup,
            "phone": newPhone
        }

        
        insertPosition = 0
        for item in list:
            if newName > item["name"]:
                insertPosition += 1
            else:
                break

        list.insert(insertPosition, newItem)
        print("Дані студента успішно оновлено!")
    return


def main():
    while True:
        chouse = input(
            "\nОберіть дію "
            "[ C - додати, U - редагувати, D - видалити, "
            "P - показати список, X - вихід ]: "
        )

        match chouse:
            case "C" | "c":
                print("Додавання нового студента:")
                addNewElement()
                printAllList()

            case "U" | "u":
                print("Редагування даних студента:")
                updateElement()
                printAllList()

            case "D" | "d":
                print("Видалення студента:")
                deleteElement()
                printAllList()

            case "P" | "p":
                print("Список студентів:")
                printAllList()

            case "X" | "x":
                print("Завершення роботи програми.")
                break

            case _:
                print("Невірна команда! Спробуйте ще раз.")


main()
