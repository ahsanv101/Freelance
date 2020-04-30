from Customer import Customer
class Students(Customer):
    def __init__(self):
        super().__init__(self)
        self.studentmajor=None
        self.studentage=None

    def getStudentMajor(self):
        return self.studenmajor

    def getStudentAge(self):
        return self.studentage

    def setStudentMajor(self,studentmajor):
        self.studentmajor=studentmajor

    def setStudentAge(self,studentage):
        self.studentage=studentage
