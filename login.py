from constants import *
from Customer import Customer
from Admin import Admin
import tkinter as tk
from tkinter.ttk import Combobox
import random
from tkinter.messagebox import showinfo
from tkinter.ttk import *
from tkinter import *


class Login_Form:
    def __init__(self):
        self.__createView()


    def __createView(self):
        self.window = tk.Tk()
        self.window.geometry('1080x720')
        self.window.title('Event Registration System')
        self.__createForm()
        self.window.mainloop()


    def __createForm(self):
        self.heading=self.__createLabel2("Login in the System",20,20)
        self.heading.config(anchor=CENTER)
        self.heading.pack()

        self.data=("Admin","Customer")
        self.type=self.__createLabel("Select user type:",110)
        self.usertype=self.__createCombo(140,self.data)

        self.type.pack()
        self.usertype.pack()


        self.una=self.__createLabel('Username: ', 170)
        self.username=self.__createInput(200)

        self.una.pack()
        self.username.pack()

        self.pa=self.__createLabel('Password: ', 230)
        self.password = self.__createInput(260)
        self.password.config(show = '*')

        self.pa.pack()
        self.password.pack()


        self.btn=self.__createBtnSubmit()
        self.btn.pack()


    def __createLabel(self, txt, y):
        self.label = tk.Label(self.window, text=txt)
        return self.label
        #self.label.place(x = 500, y = y)



    def __createLabel2(self, txt, y,size):
        self.label = tk.Label(self.window, text=txt)
        #self.label.place(x = 420, y = y)
        self.label.config(font=("Courier", size))
        return self.label

    def __createInput(self, y):
        self.input = tk.Entry(self.window)
        #self.input.place(x = 500, y = y)
        return self.input

    def __createCombo(self,y,data):
        self.combo=Combobox(self.window,values=data)
        #self.combo.place(x=500,y=y)
        return self.combo


    def __createBtnSubmit(self):
        self.button = tk.Button(self.window, text = 'Login', width = 6, background = 'green', command = self.LoginUser)
        return self.button
        #self.button.place(x=500, y=400)


    def LoginUser(self):
        if self.usertype.get()=="Customer":
            self.customer=Customer()
            self.customer.setUserType(self.usertype.get())
            result=self.customer.login(self.username.get(),self.password.get())

            if result ==True:
                showinfo("Sucess","Login Sucessfull")
            if result ==False:
                showinfo("Error", "Login Unsucessfull")

        if self.usertype.get()=="Admin":

            self.admin=Admin()
            self.admin.setUserType(self.usertype.get())
            result=self.admin.login(self.username.get(),self.password.get())

            if result ==True:
                showinfo("Sucess","Login Sucessfull")
            if result ==False:
                showinfo("Error", "Login Unsucessfull")


form = Login_Form()


#
# class Login(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         username = StringVar()
#         password = StringVar()
#         tk.Label(self, text = "Username: ").grid(row = 0, pady = 10, sticky = 'w')
#         tk.Entry(self, textvariable = username).grid(row = 0, column = 1)
#         tk.Label(self, text = "Password: ").grid(row = 1, pady = 0)
#         tk.Entry(self, textvariable = password, show="*").grid(row = 1, column = 1)
#         tk.Button(self, text = "Login", fg = BUTTON_FG_COLOR, bg = BUTTON_BG_COLOR, font = BUTTON_FONT, width = "10",
#                        command = lambda: self.do_login(username.get(), password.get(),parent)) .grid(row = 2 , columnspan=2, pady = 20)
#
#     def do_login(self, username, password,parent):
#             errorMsg = ""
#             if(username.strip() == ""):
#                 errorMsg += "Please enter username.\n"
#
#             if (password.strip() == ""):
#                 errorMsg += "Please enter password."
#
#             if (errorMsg != ""):
#                 tkinter.messagebox.showinfo("Error", errorMsg)
#             else:
#                 fileManager = FileManager()
#                 userList = fileManager.get_user_data(USER_FILE_NAME)
#                 if username not in userList.keys():
#                     errorMsg += "You entered an incorrect username."
#                 else:
#                     user = userList[username]
#                     if(user['password'] != password):
#                         errorMsg += "You entered an incorrect password."
#                 #print(user)
#                 if (errorMsg != ""):
#                     tkinter.messagebox.showinfo("Authentication failed:", errorMsg)
#                 else:
#                     if(user['isHrUser'] == 1):
#                         #print("HR")
#                         employeeList = fileManager.get_all_employee_data(EMPLOYEE_FILE_NAME)
#                         hruser = fileManager.get_employee_data(user['userId'])
#                         frame = HRUser(parent=parent, controller=self.controller, hruser = hruser, employeeList = employeeList)
#                     else:
#                         #print("Employee")
#                         employee = fileManager.get_employee_data(user['userId'])
#                         frame = Employee(parent=parent, controller=self.controller, employee = employee)
#
#                     frame.grid(row=0, column=0, sticky="n")
#                     self.destroy()
#
#             pass
#
#
# global screen
# screen = Tk()
# screen.geometry("300x250")
# screen.title("Notes 1.0")
# Label(text = "Notes 1.0", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
# Label(text = "").pack()
# Button(text = "Login", height = "2", width = "30", command = login).pack()
# Label(text = "").pack()
# Button(text = "Register",height = "2", width = "30", command = register).pack()
