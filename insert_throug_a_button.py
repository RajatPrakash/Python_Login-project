import mysql
import mysql.connector as mc
import tkinter as tk
from tkinter import messagebox as mb
import sys
import re
from password import password

window = tk.Tk()
window.geometry('300x200')
window.resizable = False
window.title = "Add to mysql DB"
connector = mc.connect(host='localhost',db='rajat',user='rajat',password='9711289764')
if connector.is_connected():

    def add():
        try:

            query = 'insert into db (name, password) values(%s, %s)'
            value = (name_entry.get(),password_entry.get())
            if password(password_entry.get()) is True:
                cursor.execute(query, value)
                connector.commit()
                mb.showinfo("Result", 'Data Inserted')
        except mysql.connector.errors.IntegrityError:
            mb.showinfo('Error in saving data, Please look into it!!')

            cursor.close()
            connector.close()

    def exit():
        sys.exit()
    print('you are in...')
    cursor = connector.cursor()
    name_label = tk.Label(window,text='Name: ')
    password_label = tk.Label(window, text="Password: ")
    name_entry = tk.Entry(window)
    password_entry = tk.Entry(window)
    exit_button = tk.Button(window, text='Cancel', command=exit)
    add_button = tk.Button(window, text='Add Record', command=add)
    name_label.grid(row=0, column=3)
    password_label.grid(row=2, column=3)
    name_entry.grid(row=0, column=5)
    password_entry.grid(row=2, column=5)
    exit_button.grid(row=4, column=3)
    add_button.grid(row=4, column=5)




window.mainloop()