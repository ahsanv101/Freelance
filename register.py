from constants import *
from Customer import Customer
import tkinter as tk


class Register_Control:
    def __init__(self, email, password):
        self.customer=Customer()
        self.customer.setEmail(email)
        self.customer.setPassword(password)
        self.email = self.customer.getEmail()
        self.password = self.customer.getPassword()
        self.save()

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




