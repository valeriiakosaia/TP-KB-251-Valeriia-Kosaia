
import lab_02

def test_add():
    lab_02.list.clear()

    lab_02.addNewElement("Bob", "Smith", "КБ-251", "0631234567")

    assert len(lab_02.list) == 1
    assert lab_02.list[0]["name"] == "Bob"


def test_delete():
    lab_02.list.clear()

    lab_02.addNewElement("Bob", "Smith", "КБ-251", "0631234567")
    result = lab_02.deleteElement("Bob")

    assert result == True
    assert len(lab_02.list) == 0


def test_update():
    lab_02.list.clear()

    lab_02.addNewElement("Bob", "Smith", "КБ-251", "0631234567")

    result = lab_02.updateElement(
        "Bob", "Anna", "Bondar", "КБ-252", "0671234567"
    )

    assert result == True
    assert len(lab_02.list) == 1
    assert lab_02.list[0]["name"] == "Anna"


def test_save_load(tmp_path):
    lab_02.list.clear()

    lab_02.addNewElement("Bob", "Smith", "КБ-251", "0631234567")

    fileName = tmp_path / "test.csv"
    lab_02.saveList(fileName)

    lab_02.list.clear()
    lab_02.loadList(fileName)

    assert len(lab_02.list) == 1
    assert lab_02.list[0]["name"] == "Bob"
