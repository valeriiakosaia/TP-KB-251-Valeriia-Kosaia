from sys import argv
from Student import Student
from StudentList import StudentList
from Utils import Utils


def main():
    if len(argv) != 2:
        print("Запуск: python lab_03.py lab3.csv")
        return

    fileName = argv[1]

    students = StudentList()
    utils = Utils()

    utils.loadList(fileName, students)

    print("\n--- Завантажений список студентів із файлу ---")
    students.printAllList()
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

                name = input("Введіть ім'я студента: ")
                surname = input("Введіть прізвище студента: ")
                group = input("Введіть групу студента: ")
                phone = input("Введіть номер телефону: ")

                newStudent = Student(name, surname, group, phone)
                students.addNewElement(newStudent)

                print("Студента успішно додано!")
                students.printAllList()

            case "U" | "u":
                print("Редагування даних студента:")

                name = input("Введіть ім'я студента для редагування: ")

                if any(student.name == name for student in students.list):
                    print("Студента знайдено. Введіть нові дані:")

                    newName = input("Введіть нове ім'я: ")
                    newSurname = input("Введіть нове прізвище: ")
                    newGroup = input("Введіть нову групу: ")
                    newPhone = input("Введіть новий номер телефону: ")

                    newStudent = Student(
                        newName, newSurname, newGroup, newPhone
                    )
                    students.updateElement(name, newStudent)

                    print("Дані студента успішно оновлено!")
                else:
                    print("Студента не знайдено!")

                students.printAllList()

            case "D" | "d":
                print("Видалення студента:")

                name = input("Введіть ім'я студента для видалення: ")

                if students.deleteElement(name):
                    print("Студента успішно видалено!")
                else:
                    print("Студента не знайдено!")

                students.printAllList()

            case "P" | "p":
                print("Список студентів:")
                students.printAllList()

            case "X" | "x":
                utils.saveList(fileName, students)
                print("Дані студентів збережено у файл!")
                print("Завершення роботи програми.")
                break

            case _:
                print("Невірна команда! Спробуйте ще раз.")


if __name__ == "__main__":
    main()
