from WebUser import WebUser
class Customer(WebUser):
    def __init__(self):
        WebUser.__init__(self)
        self.custid=None
        self.cust_name=None
        self.orders=[]

    def createCustomerAccount(self,username,custid,email,phonenum):
        try:
            self.file_name = 'user.txt'
            self.file = open(self.file_name, 'a')
            self.file.writelines('\n')
            self.file.writelines( self.username +',' +self.custid +',' +self.email +',' +self.phonenum+ '\n' )
            self.file.close()
            print('\n Data saved successfully')

        except:
            print('\n Error saving data')

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
