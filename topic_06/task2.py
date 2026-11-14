students = [
    {"name": "Emma", "grade": 85},
    {"name": "Zak", "grade": 72},
    {"name": "Lera", "grade": 95},
    {"name": "Bob", "grade": 78},
    {"name": "Vika", "grade": 61},
    {"name": "Ben", "grade": 50},
    {"name": "Anna", "grade": 98}
]

print("Початковий список:")
for student in students:
    print(student)

sortedByName = sorted(students, key=lambda student: student["name"])

print("\nСортування за ім'ям:")
for student in sortedByName:
    print(student)

sortedByGrade = sorted(students, key=lambda student: student["grade"])

print("\nСортування за оцінкою:")
for student in sortedByGrade:
    print(student)
