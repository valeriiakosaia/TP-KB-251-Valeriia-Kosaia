
import csv
from sys import argv

list = []

def loadList(fileName):
    with open(fileName, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        list.clear()

        for row in reader:
            list.append({
                "name": row["name"],
                "surname": row["surname"],
                "group": row["group"],
                "phone": row["phone"]
            })

    list.sort(key=lambda item: item["name"])
    print("Дані студентів завантажено!")


def saveList(fileName):
    with open(fileName, "w", newline="", encoding="utf-8-sig") as file:
        fieldnames = ["name", "surname", "group", "phone"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(list)

def printAllList():
    for elem in list:
        strForPrint = (
            "Ім'я: " + elem["name"] +
            ", Прізвище: " + elem["surname"] +
            ", Група: " + elem["group"] +
            ", Телефон: " + elem["phone"]
        )
        print(strForPrint)

def addNewElement(name=None, surname=None, group=None, phone=None):
    if name is None:
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

def deleteElement(name=None):
    if name is None:
        name = input("Введіть ім'я студента для видалення: ")

    for item in list:
        if name == item["name"]:
            list.remove(item)
            print("Студента успішно видалено!")
            return True

    print("Студента не знайдено!")
    return False

def updateElement(name=None, newName=None, newSurname=None,
                  newGroup=None, newPhone=None):

    if name is None:
        name = input("Введіть ім'я студента для редагування: ")

    for item in list:
        if name == item["name"]:

            if newName is None:
                print("Студента знайдено. Введіть нові дані:")
                newName = input("Введіть нове ім'я: ")
                newSurname = input("Введіть нове прізвище: ")
                newGroup = input("Введіть нову групу: ")
                newPhone = input("Введіть новий номер телефону: ")

            list.remove(item)
            addNewElement(newName, newSurname, newGroup, newPhone)

            print("Дані студента успішно оновлено!")
            return True

    print("Студента не знайдено!")
    return False

def main():
    if len(argv) != 2:
        print("Запуск: python lab_02.py students.csv")
        return

    fileName = argv[1]
    loadList(fileName)
    
    print("\n--- Завантажений список студентів із файлу ---")
    printAllList()
    print("---------------------------------------------\n")

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
             saveList(fileName)
             print("Дані студентів збережено у файл!")
             print("Завершення роботи програми.")
             break

            case _:
                print("Невірна команда! Спробуйте ще раз.")

if __name__ == "__main__":
    main()