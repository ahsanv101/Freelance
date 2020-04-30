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

    def getUserType(self):
        return self.usertype

    def getPhoneNumber(self):
        return self.phonenum

    def setEmail(self,email):
        self.email=email

    def setUserName(self,username):
        self.username=username

    def setPassword(self,password):
        self.password=password

    def setUserType(self,usertype):
        self.usertype=usertype

    def setPhoneNumber(self,phonenum):
        self.phonenum=phonenum

    def login(self,username,password):
        lst=[]
        if self.usertype=="Customer":
            file1 = open('user.txt', 'r')
            
        else:
            file1 = open('employees.txt', 'r')
        try:
            
            Lines = file1.readlines()
            for line in Lines:
                if line.strip()!='':
                    cred=line.strip()
                    cred=cred.split(',')
                    lst.append(cred)

            for i in lst:
                if str(i[0])==str(username):
                    if str(i[1])==str(password):
                        return True
            return False
                
        except:
            return False


    def userExits(self,username,password):
        pass



