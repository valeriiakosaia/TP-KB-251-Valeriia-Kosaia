class StudentList:
    def __init__(self):
        self.list = []

    def printAllList(self):
        for student in self.list:
            print(student)

    def addNewElement(self, student):
        insertPosition = 0

        for item in self.list:
            if student.name > item.name:
                insertPosition += 1
            else:
                break

        self.list.insert(insertPosition, student)
        return True

    def deleteElement(self, name):
        for student in self.list:
            if student.name == name:
                self.list.remove(student)
                return True

        return False

    def updateElement(self, name, newStudent):
        for student in self.list:
            if student.name == name:
                self.list.remove(student)
                self.addNewElement(newStudent)
                return True

        return False
