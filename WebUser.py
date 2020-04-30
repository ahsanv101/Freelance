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

    def setPassword(self,password):
        self.password=password

    def setUsertype(self,usertype):
        self.usertype=usertype

    def setPhoneNumber(self,phonenum):
        self.phonenum=phonenum

    def login(self,username,password):
        pass

    def userExits(self,username,password):
        pass



