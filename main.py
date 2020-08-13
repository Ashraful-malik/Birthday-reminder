from tkinter import *
import sqlite3
from tkinter import messagebox
window = Tk()


def add_friend():
    connect = sqlite3.connect('birthday.db')
    cursor = connect.cursor()
    add=cursor.execute("INSERT INTO birthday VALUES(:name_box,:birthday_box)",
                   {
                       'name_box': name_box.get(),
                       'birthday_box': birthday_box.get()
                   })
    connect.commit()
    connect.close()
    name_box.delete(0, END)
    connect.close()
    birthday_box.delete(0, END)


def search_name():
    connect = sqlite3.connect('birthday.db')
    cursor = connect.cursor()
    get_info = search_friend_box.get()
    sql = "SELECT* FROM birthday WHERE Friend_name = ?"
    name = (get_info,)
    cursor.execute(sql, name)
    result = cursor.fetchall()
    for results in result:
        search_friend_box.delete(0, END)
        search_friend_box.insert(END, results[1])
    if not result:
        search_friend_box.delete(0, END)
        messagebox.showinfo("", 'Please check your name✍️')
    connect.commit()
    connect.close()


window.title("Birthday reminder")
window.geometry("590x300")

# adding database
connect = sqlite3.connect('birthday.db')
cursor = connect.cursor()

# cursor.execute("""CREATE TABLE birthday(
#     Friend_name text,
#     Birthday text
#         )""")


frame = Frame(window,bg='#33ffbd')
frame.pack(side=TOP)
name_label = Label(frame, text="Name of your Friend", font=" arial 20 italic",bg='#33ffbd',fg="blue")
Birthday_label = Label(frame, text="Birthday", font=" arial 20 italic",bg='#33ffbd',fg="blue")

name_box = Entry(frame, width=30, font="20")
birthday_box = Entry(frame, width=30, font='20')
Add_btn = Button(frame, text="Add Friend Birthday", width=30, command=add_friend,
                 bg='#337dff',font="arial 15",fg="white")
search_friend_box = Entry(frame, text="Add Friend Birthday", width=30,font=' Courier 13')

search_btn = Button(frame, text="SEARCH NAME", command=search_name,font='Roboto 10',bg='#34d2eb',relief='flat')

name_label.grid(row=0, column=0)
Birthday_label.grid(row=1, column=0)
name_box.grid(row=0, column=1, pady=20)
birthday_box.grid(row=1, column=1, pady=20)
Add_btn.grid(row=2, column=0, columnspan=3)

search_btn.grid(row=3, column=0, columnspan=1,pady=10)
search_friend_box.grid(row=3, column=1)
window.config(bg='#33ffbd')
connect.commit()
connect.close()
window.mainloop()
