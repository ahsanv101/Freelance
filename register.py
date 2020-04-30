from constants import *
from Customer import Customer
from Admin import Admin
import tkinter as tk
from tkinter.ttk import Combobox
import random
from tkinter.messagebox import showinfo


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
        self.password = self.__createInput(260)
        self.password.config(show = '*')


        self.__createLabel('Email: ', 290)
        self.email = self.__createInput(310)


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
        self.button = tk.Button(self.window, text = 'Submit', width = 6, background = 'green', command = self.registerUser)
        self.button.place(x=500, y=400)


    def registerUser(self):
        if self.usertype.get()=="Customer":
            self.customer=Customer()
            self.customer.setEmail(self.email.get())
            self.customer.setPassword(self.password.get())
            self.customer.setUserName(self.username.get())
            self.customer.setPhoneNumber(self.phonenum.get())
            self.customer.setUserType(self.usertype.get())
            self.customer.setCustomerName(self.name.get())
            id= ' '.join([str(random.randint(0, 999)).zfill(3) for _ in range(2)])
            self.customer.setCustomerId(id)
            try:
                self.customer.createCustomerAccount(self.username.get(),id,self.email.get(),self.phonenum.get())
                showinfo("Sucess","Account Created")
            except:
                showinfo("Error", "Error in Creating Account ")

        if self.usertype.get()=="Admin":
            self.admin=Admin()
            self.admin.setEmail(self.email.get())
            self.admin.setPassword(self.password.get())
            self.admin.setUserName(self.username.get())
            self.admin.setPhoneNumber(self.phonenum.get())
            self.admin.setUserType(self.usertype.get())
            self.admin.setAdminName(self.name.get())
            id2= ' '.join([str(random.randint(0, 999)).zfill(3) for _ in range(2)])
            self.admin.setAdminId(id2)
            try:
                self.admin.createAdminAccount(self.username.get(),id2,self.email.get(),self.phonenum.get())
                showinfo("Sucess","Admin Account Created")
            except:
                showinfo("Error","Error in Creating Account ")


form = Register_Form()




