import tkinter as tk
import mysql.connector as mc

window = tk.Tk()
window.geometry('300x200')
window.resizable(False, False)
label = tk.Label(window, text='User Name')
entry = tk.Entry(window)
flag = 1


def check():
    connnect = mc.connect(host='localhost', db='rajat', user='rajat', password='9711289764')
    if connnect.is_connected():
        print('You are in...')
        cur = connnect.cursor()
        cur.execute('select * from python')
        rows = cur.fetchall()
        user_input = entry.get()
        for row in rows:
            if user_input == row[1]:
                flag = 0
                break
            else:
                flag = 1
        if flag == 0:
            print('data Exists')
        else:
            print('new data')

        cur.close()
        connnect.close()
    else:
        print('Somethings Wrong')


check_button = tk.Button(window, text="check", command=check)
label.pack()
entry.pack()
check_button.pack()



window.mainloop()