from Student import Student
from StudentList import StudentList
from Utils import Utils

def test_add():
    students = StudentList()

    students.addNewElement(Student("Bob", "Smith", "КБ-251", "0631234567"))

    assert len(students.list) == 1
    assert students.list[0].name == "Bob"


def test_delete():
    students = StudentList()

    students.addNewElement(Student("Bob", "Smith", "КБ-251", "0631234567"))
    result = students.deleteElement("Bob")

    assert result == True
    assert len(students.list) == 0


def test_update():
    students = StudentList()

    students.addNewElement(Student("Bob", "Smith", "КБ-251", "0631234567"))

    result = students.updateElement(
        "Bob", Student("Anna", "Bondar", "КБ-252", "0671234567")
    )

    assert result == True
    assert len(students.list) == 1
    assert students.list[0].name == "Anna"


def test_sort():
    students = StudentList()

    students.addNewElement(Student("Zak", "Taylor", "КБ-251", "111"))
    students.addNewElement(Student("Anna", "Bondar", "КБ-251", "222"))

    assert students.list[0].name == "Anna"
    assert students.list[1].name == "Zak"


def test_save_load(tmp_path):
    students = StudentList()
    utils = Utils()

    students.addNewElement(Student("Bob", "Smith", "КБ-251", "0631234567"))

    fileName = tmp_path / "test.csv"
    utils.saveList(fileName, students)

    students.list.clear()
    utils.loadList(fileName, students)

    assert len(students.list) == 1
    assert students.list[0].name == "Bob"
    assert students.list[0].phone == "0631234567"
