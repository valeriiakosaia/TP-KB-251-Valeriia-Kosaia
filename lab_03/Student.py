class Student:
    def __init__(self, name, surname, group, phone):
        self.name = name
        self.surname = surname
        self.group = group
        self.phone = phone

    def __str__(self):
        return (
            "Ім'я: " + self.name +
            ", Прізвище: " + self.surname +
            ", Група: " + self.group +
            ", Телефон: " + self.phone
        )
