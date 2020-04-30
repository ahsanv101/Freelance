from Admin import Admin
from Customer import Customer

class Instructor(Admin,Customer):
    def __init__(self):
        super().__init__(self)
        self.instrspeciality=None

    def getInstrSpeciality(self):
        return self.instrspeciality

    def setInstrSpeciality(self,instrspeciality):
        self.instrspeciality=instrspeciality
    
