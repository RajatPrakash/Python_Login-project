# this is the final login project with everything in place
import tkinter as tk
import mysql.connector as mc
from tkinter import messagebox as mb
import re
import sys

design = ('Arial Bold', 8)
window = tk.Tk()
window.geometry('400x150')
window.title('Sign up')
window.resizable(False, False)
connect = mc.connect(host='localhost', db='rajat', user='rajat', password='9711289764')
if connect.is_connected():
    print('you are in...')


class Sign_up:

        def sign_up_click(self):
            self.root = tk.Toplevel(window)
            self.root.geometry('500x250')
            self.root.resizable(False, False)
            # self.pho = tk.PhotoImage(file='coding-job.png')
            self.top_frame = tk.Frame(self.root)
            self.bottom_frame = tk.Frame(self.root)
            self.user_name = tk.Label(self.top_frame, text='User Name', font=design)
            self.user_name_entry = tk.Entry(self.top_frame)
            self.password = tk.Label(self.top_frame, text="Passsword", font=design)
            self.password_entry = tk.Entry(self.top_frame)
            self.confirm_password = tk.Label(self.top_frame, text='''Confirm 
    Password''', font=design)
            self.confirm_password_entry = tk.Entry(self.top_frame)
            self.check_button = tk.Button(self.top_frame, text='Create Account', command=self.check, font=design)
            self.exit_button = tk.Button(self.top_frame, text='Cancel', command=self.Exit, font=design)
            # self.image_label_top.place(x=0, y=0, relwidth=1, relheight=1)
            # self.image_label_bottom.place(x=0, y=0, relwidth=1, relheight=1)
            self.exit_button.grid(row=9, column=2)
            self.auto_label = tk.Label(self.bottom_frame, text='', fg='red', font=('arial', 10))
            self.email = tk.Label(self.top_frame, text='Email ID', font=design)
            self.email_entry = tk.Entry(self.top_frame)
            self.pass_instruction = tk.Label(self.bottom_frame, text='''Rules for passwords!
                 Password Length should be atleast 8 character long:
                 Password should have atleast one Capital Letter:        
          Password should have atleast one Number
                Password should have atleast one special character!''', fg='blue', font=design)
            self.user_name.grid(row=0, column=2)
            self.user_name_entry.grid(row=0, column=5)
            self.password.grid(row=3, column=2)
            self.password_entry.grid(row=3, column=5)
            self.confirm_password.grid(row=5, column=2)
            self.confirm_password_entry.grid(row=5, column=5)
            self.email.grid(row=7, column=2)
            self.email_entry.grid(row=7, column=5)
            self.check_button.grid(row=9, column=5)
            self.auto_label.pack(side='top')
            self.top_frame.pack()
            self.bottom_frame.pack(side='bottom')
            self.pass_instruction.pack()

        def Exit(self):
            sys.exit()

        def mailid(self):
            mail = self.email_entry.get()
            self.mail_flag =0
            if len(mail) == 0:
                self.mail_flag =1
                self.auto_label.configure(text='Email Cannot be left blank',fg='red')
            elif re.search('@', mail) is None:
                self.mail_flag = 2
                self.auto_label.configure(text='please provide a valid email id',fg='red')
            else:
                self.mail_flag =0

        def check(self):
            flag = 0
            cursor = connect.cursor()
            cursor.execute('select * from python_login')
            rows = cursor.fetchall()

            entry = self.user_name_entry.get()
            # print(len(entry))
            for row in rows:
                if len(entry) == 0:
                    flag = 2
                    break
                elif entry == row[1]:
                    flag = 1
                    break
                else:
                    flag = 0

            if flag == 2:
                self.auto_label.configure(text='User name cannot be empty',fg='red')
            elif flag == 1:
                self.auto_label.configure(text='User Exists!',fg='red')
            else:
                self.password_checker()
                if self.pass_flag == 0:
                    self.confirm_pass()
                    if self.confirm_pass_flag == 0:
                        self.auto_label.configure(text='confirm Password is not equal to password',fg='red')
                    else:
                        password = self.password_entry.get()
                        self.mailid()
                        if self.mail_flag == 0:
                            mail = self.email_entry.get()
                            query = """insert into python_login (name,password,email) values(%s, %s, %s)"""
                            values = (entry, password,mail)
                            try:
                                cursor.execute(query, values)
                                connect.commit()
                                self.user_name_entry.delete(first=0, last=30)
                                self.password_entry.delete(first=0, last=30)
                                self.confirm_password_entry.delete(first=0, last=30)
                                self.email_entry.delete(first=0, last=30)
                                print('Record Insert successfully!')
                                self.auto_label.configure(text='User Created',fg='green')
                            except:
                                connect.rollback()
                                print("Connection has been roll back")

        def confirm_pass(self):

            if self.pass_flag == 0:
                self.confirm_pass_flag = 0
                confirm_pass = self.confirm_password_entry.get()
                password = self.password_entry.get()
                if password == confirm_pass:
                    self.confirm_pass_flag = 1
                else:
                    self.confirm_pass_flag = 0

        # def user_input(self):
        #     while True:
        #         if len(self.user_name_entry.get()) == 0:
        #             self.auto_label.configure(text='User name cannot be empty')

        def password_checker(self):
            password = self.password_entry.get()
            self.pass_flag = 0
            while True:
                if len(password) < 8:
                    self.auto_label.configure(text='Password Length should be atleast 8 character long:')
                    self.pass_flag = 1
                    break
                elif re.search('[A-Z]', password) is None:
                    self.auto_label.configure(text='Password should have atleast one Capital Letter:')
                    self.pass_flag = 1
                    break
                elif re.search('[0-9]', password) is None:
                    self.auto_label.configure(text='Password should have atleast one Number')
                    self.pass_flag = 1
                    break
                elif re.search('[!@#$%^&*]', password) is None:
                    self.auto_label.configure(text='Password should have atleast one special character!')
                    self.pass_flag = 1
                    break
                else:
                    print('password is in order')
                    self.pass_flag = 0
                    break


class Sign_in:
    def sign_in_click(self):
        self.root1 = tk.Toplevel(window)
        self.root1.geometry('250x150')
        self.root1.resizable(False, False)
        self.root1.title('Sign in')
        self.top_frame = tk.Frame(self.root1)
        self.bottom_frame = tk.Frame(self.root1)
        self.label = tk.Label(self.top_frame, text='Welcome!', font=('Arial BOLD',15))
        self.user_label = tk.Label(self.top_frame, text='User-Name', font=design)
        self.user_entry = tk.Entry(self.top_frame)
        self.password_label = tk.Label(self.top_frame, text='Password', font=design)
        self.password_entry = tk.Entry(self.top_frame)
        self.auto_label = tk.Label(self.bottom_frame,text='',font=design)
        self.Submit = tk.Button(self.top_frame,text="Submit", font=design,command=self.check)
        self.cancel = tk.Button(self.top_frame,text="Cancel", font=design, command=self.Exit)
        self.label.grid(row=0,column=5)
        self.user_label.grid(row=2,column=2)
        self.password_label.grid(row=4,column=2)
        self.user_entry.grid(row=2,column=5)
        self.password_entry.grid(row=4,column=5)
        self.Submit.grid(row=6,column=5)
        self.cancel.grid(row=6,column=2)
        self.auto_label.pack()
        self.top_frame.pack()
        self.bottom_frame.pack(side='bottom')

    def Exit(self):
        sys.exit()

    def check(self):
        user = self.user_entry.get()
        password = self.password_entry.get()
        check_flag = 0
        print(len(password))
        if len(user) == 0:
            self.auto_label.configure(text='User name cannot be Empty',fg='red')
            check_flag = 1
        elif len(password) == 0:
            self.auto_label.configure(text='Password  cannot be Empty',fg='red')
            check_flag = 1
        else:
            check_flag = 0
            self.varifi()

    def varifi(self):
        user = self.user_entry.get()
        password = self.password_entry.get()
        cursor = connect.cursor()
        cursor.execute('select * from python_login')
        rows = cursor.fetchall()
        for row in rows:
            if user == row[1]:
                if password ==row[2]:
                    self.auto_label.configure(text='Login Successfull',fg='Green')
                else:
                    self.auto_label.configure(text='Password Incorrect',fg='red')
            else:
                self.auto_label.configure(text='User name Does not exists',fg='red')


obj = Sign_up()
obj1= Sign_in()
label = tk.Label(window,text="Welcome to the Rajat's World!",fg='Green',font=('BOLD',20))
button = tk.Button(window, text='Sign Up',command=obj.sign_up_click,font=('BOLD',12))
button1 = tk.Button(window, text='Sign In  ',command=obj1.sign_in_click,font=('BOLD',12))
label.pack()
button1.pack()
button.pack()

window.mainloop()
