class WebUser:
    def __init__(self):  
        self.username = None
        self.password = None
        self.usertype=None
        self.email=None
        self.phonenum=None

    def getEmail(self):
        return self.email

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def getUsertype(self):
        return self.usertype

    def getPhoneNumber(self):
        return self.phonenum

    def setEmail(self,email):
        self.email=email

    def setUsername(self,username):
        self.username=username

    def getPassword(self,password):
        self.password=password

    def setUsertype(self,usertype):
        self.usertype=usertype

    def setPhoneNumber(self,phonenum):
        self.phonenum=phonenum

    def login(self,username,password):
        pass

    def userExits(self,username,password):
        pass



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

        


class Customer(WebUser):
    def __init__(self):
        super().__init__(self)
        self.custid=None
        self.cust_name=None
        self.orders=[]

    def createCustomerAccount(self,username,custid,email,phonenum):
        pass

    def viewRegisteredEvents(self,username,event_name,event_time,getticket):
        pass

    def getCustomerId(self):
        return self.custid

    def getCustomerName(self,cust_name):
        return self.cust_name

    def setCustomerId(self,custid):
        self.custid=custid

    def setCustomerName(self,cust_name):
        self.cust_name=cust_name

    def getOrders(self):
        return self.orders



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




class Instructor(Admin,Customer):
    def __init__(self):
        super().__init__(self)
        self.instrspeciality=None

    def getInstrSpeciality(self):
        return self.instrspeciality

    def setInstrSpeciality(self,instrspeciality):
        self.instrspeciality=instrspeciality
    
