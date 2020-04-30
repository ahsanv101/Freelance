from WebUser import WebUser

class Admin(WebUser):
    def __init__(self):
        WebUser.__init__(self)
        self.adminid=None
        self.adminname=None

    def createAdminAccount(self,username,adminid,email,phonenum):
        try:
            self.file_name = 'employees.txt'
            self.file = open(self.file_name, 'a')
            self.file.writelines('\n')
            self.file.writelines( self.username +',' +self.password+',' +self.adminid +',' +self.email +',' +self.phonenum+ '\n' )
            self.file.close()
            print('\n Data saved successfully')

        except:
            print('\n Error saving data')


    def getAdminId(self):
        return self.adminid

    def getAdminName(self):
        return self.adminname

    def setAdminId(self,adminid):
        self.adminid=adminid

    def setAdminName(self,adminname):
        self.adminname=adminname

