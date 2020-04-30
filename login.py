#from tkinter import *
from constants import *
from Customer import Customer


import tkinter as tk

import datetime



# class Person:
#     def __init__(self, name, email, password):
#         self.__name = name
#         self.__email = email
#         self.__password = password
#
#     def get_name(self):
#         return self.__name
#
#     def get_email(self):
#         return self.__email
#
#     def get_password(self):
#         return self.__password


class Register_Control:
    def __init__(self, email, password):
        #self.get_date()

        #self.person = Person( email, password)
        self.customer=Customer()
        self.customer.setEmail(email)
        self.customer.setPassword(password)
        #self.name = 'Name: {}'.format(self.person.get_name())
        self.email = self.customer.getEmail()
        self.password = self.customer.getPassword()

       # self.print_console()
        self.save()

    # def get_date(self):
    #     self.current_date = datetime.datetime.now()
    #
    #     self.text_date = '{}_{}_{}'.format(self.current_date.day, self.current_date.month, self.current_date.year)
    #     self.text_time_data = 'Date created: {}'.format(self.current_date.strftime("%d/%m/%Y  %H:%M"))


    # def print_console(self):
    #     print(
    #         '\n Name: ', self.person.get_name(), \
    #         '\n Email: ', self.person.get_email(), \
    #         '\n Password: ', self.person.get_password()
    #     )
    #     self.save()

    def save(self):
        try:
            self.file_name = 'user.txt'
            self.file = open(self.file_name, 'a')
            self.file.writelines('\n')
            self.file.writelines( self.email +',' +self.password + '\n' )
            self.file.close()
            print('\n Data saved successfully')

        except:
            print('\n Error saving data')







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



        #self.__createLabel('Your Name: ', 80)
        #self.inputName = self.__createInput(100)



        self.__createLabel('Email: ', 130)
        self.inputEmail = self.__createInput(150)

        self.__createLabel('Password: ', 180)
        self.inputPassword = self.__createInput(200)
        self.inputPassword.config(show = '*')

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


    def __createBtnSubmit(self):
        self.button = tk.Button(self.window, text = 'Submit', width = 6, background = 'green', command = self.get_input_data)
        self.button.place(x=500, y=233)


    def get_input_data(self):
        self.control = Register_Control(self.inputEmail.get(), self.inputPassword.get())
        self.respost = self. __createLabel('User created successfully', 40)





form = Register_Form()





























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
