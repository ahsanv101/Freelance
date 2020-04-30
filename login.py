from tkinter import *
from constants import *

'''
class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller        
        username = StringVar()
        password = StringVar()
        tk.Label(self, text = "Username: ").grid(row = 0, pady = 10, sticky = 'w') 
        tk.Entry(self, textvariable = username).grid(row = 0, column = 1)
        tk.Label(self, text = "Password: ").grid(row = 1, pady = 0)
        tk.Entry(self, textvariable = password, show="*").grid(row = 1, column = 1) 
        tk.Button(self, text = "Login", fg = BUTTON_FG_COLOR, bg = BUTTON_BG_COLOR, font = BUTTON_FONT, width = "10", 
                       command = lambda: self.do_login(username.get(), password.get(),parent)) .grid(row = 2 , columnspan=2, pady = 20)   

    def do_login(self, username, password,parent):   
            errorMsg = ""
            if(username.strip() == ""):
                errorMsg += "Please enter username.\n"
            
            if (password.strip() == ""):
                errorMsg += "Please enter password."
            
            if (errorMsg != ""):
                tkinter.messagebox.showinfo("Error", errorMsg)
            else:
                fileManager = FileManager()
                userList = fileManager.get_user_data(USER_FILE_NAME)
                if username not in userList.keys():
                    errorMsg += "You entered an incorrect username."
                else:
                    user = userList[username]
                    if(user['password'] != password):
                        errorMsg += "You entered an incorrect password."
                #print(user)
                if (errorMsg != ""):
                    tkinter.messagebox.showinfo("Authentication failed:", errorMsg)
                else:
                    if(user['isHrUser'] == 1):
                        #print("HR")
                        employeeList = fileManager.get_all_employee_data(EMPLOYEE_FILE_NAME)
                        hruser = fileManager.get_employee_data(user['userId'])
                        frame = HRUser(parent=parent, controller=self.controller, hruser = hruser, employeeList = employeeList)
                    else:
                        #print("Employee")
                        employee = fileManager.get_employee_data(user['userId'])
                        frame = Employee(parent=parent, controller=self.controller, employee = employee)
                    
                    frame.grid(row=0, column=0, sticky="n")
                    self.destroy()
                    
            pass
'''

global screen
screen = Tk()
screen.geometry("300x250")
screen.title("Notes 1.0")
Label(text = "Notes 1.0", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
Label(text = "").pack()
Button(text = "Login", height = "2", width = "30", command = login).pack()
Label(text = "").pack()
Button(text = "Register",height = "2", width = "30", command = register).pack()
