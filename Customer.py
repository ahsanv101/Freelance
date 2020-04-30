from WebUser import WebUser
class Customer(WebUser):
    def __init__(self):
        WebUser.__init__(self)
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
