class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Ім'я: {self.name}, Вік: {self.age}"

students = [
    Student("Emma", 20),
    Student("Zak", 22),
    Student("Anna", 19),
    Student("Bob", 21),
    Student("Vika", 23),
    Student("Lera", 19)
]


print("Початковий список:")
for student in students:
    print(student)


sortedByName = sorted(students, key=lambda student: student.name)

print("\nСортування за ім'ям:")
for student in sortedByName:
    print(student)


sortedByAge = sorted(students, key=lambda student: student.age)

print("\nСортування за віком:")
for student in sortedByAge:
    print(student)
