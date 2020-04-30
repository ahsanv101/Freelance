from constants import *
from Customer import Customer
from Admin import Admin
import tkinter as tk
from tkinter.ttk import Combobox
import random

class Register_Control:
    def __init__(self, email, password,name,username,phonenum,usertype):
        #print(email,password,name,username,phonenum,usertype)
        if usertype=="Customer":
            self.customer=Customer()
            self.customer.setEmail(email)
            self.customer.setPassword(password)
            self.customer.setUserName(username)
            self.customer.setPhoneNumber(phonenum)
            self.customer.setUserType(usertype)
            self.customer.setCustomerName(name)
            id= ' '.join([str(random.randint(0, 999)).zfill(3) for _ in range(2)])
            self.customer.setCustomerId(id)
            self.customer.createCustomerAccount(username,id,email,phonenum)

        if usertype=="Admin":
            self.admin=Admin()
            self.admin.setEmail(email)
            self.admin.setPassword(password)
            self.admin.setUserName(username)
            self.admin.setPhoneNumber(phonenum)
            self.admin.setUserType(usertype)
            self.admin.setAdminName(name)
            id= ' '.join([str(random.randint(0, 999)).zfill(3) for _ in range(2)])
            self.admin.setAdminId(id)
            self.admin.createAdminAccount(username,id,email,phonenum)


        # self.customer=Customer()
        # self.customer.setEmail(email)
        # self.customer.setPassword(password)
        # self.email = self.customer.getEmail()
        # self.password = self.customer.getPassword()
        # self.save()




class Register_Form:
    def __init__(self):
        self.__createView()


    def __createView(self):
        self.window = tk.Tk()
        self.window.geometry('1080x720')
        self.window.title('Event Registration System')
        self.__createForm()
        self.window.mainloop()


    def __createForm(self):
        self.__createLabel2("Register in the System",20,20)
        self.data=("Admin","Customer")


        self.__createLabel('Full name: ', 50)
        self.name = self.__createInput(80)


        self.__createLabel("Select user type:",110)
        self.usertype=self.__createCombo(140,self.data)


        self.__createLabel('Username: ', 170)
        self.username=self.__createInput(200)


        self.__createLabel('Password: ', 230)
        self.inputPassword = self.__createInput(260)
        self.inputPassword.config(show = '*')


        self.__createLabel('Email: ', 290)
        self.inputEmail = self.__createInput(310)


        self.__createLabel('Phone Number: ', 340)
        self.phonenum = self.__createInput(370)


        self.__createBtnSubmit()


    def __createLabel(self, txt, y):
        self.label = tk.Label(self.window, text=txt)
        self.label.place(x = 500, y = y)



    def __createLabel2(self, txt, y,size):
        self.label = tk.Label(self.window, text=txt)
        self.label.place(x = 420, y = y)
        self.label.config(font=("Courier", size))

    def __createInput(self, y):
        self.input = tk.Entry(self.window)
        self.input.place(x = 500, y = y)
        return self.input

    def __createCombo(self,y,data):
        self.combo=Combobox(self.window,values=data)
        self.combo.place(x=500,y=y)
        return self.combo



    def __createBtnSubmit(self):
        self.button = tk.Button(self.window, text = 'Submit', width = 6, background = 'green', command = self.get_input_data)
        self.button.place(x=500, y=400)


    def get_input_data(self):
        self.control = Register_Control(self.inputEmail.get(), self.inputPassword.get(),self.name.get(),self.username.get(),self.phonenum.get(),self.usertype.get())
        self.respost = self. __createLabel('User created successfully', 40)




form = Register_Form()




