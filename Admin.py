from WebUser import WebUser

class Admin(WebUser):
    def __init__(self):
        super().__init__(self)
        self.adminid=None
        self.adminname=None

    def createAdminAccount(self,username,adminid,email,phonenum):
        pass

    def getAdminId(self):
        return self.adminid

    def getAdminName(self):
        return self.adminname

    def setAdminId(self,adminid):
        self.adminid=adminid

    def setAdminName(self,adminname):
        self.adminname=adminname

