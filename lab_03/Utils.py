import csv
from Student import Student


class Utils:
    def loadList(self, fileName, studentList):
        with open(fileName, "r", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)

            studentList.list.clear()

            for row in reader:
                student = Student(
                    row["name"],
                    row["surname"],
                    row["group"],
                    row["phone"]
                )
                studentList.addNewElement(student)

        print("Дані студентів завантажено!")

    def saveList(self, fileName, studentList):
        with open(fileName, "w", newline="", encoding="utf-8-sig") as file:
            fieldnames = ["name", "surname", "group", "phone"]

            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for student in studentList.list:
                writer.writerow({
                    "name": student.name,
                    "surname": student.surname,
                    "group": student.group,
                    "phone": student.phone
                })
