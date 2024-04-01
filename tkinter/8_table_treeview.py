import tkinter as tk
from tkinter import ttk

""" window """
window = tk.Tk()
window.title("Table / Treeview")
window.geometry("800x400")

""" data """

first_names = ["John", "Jane", "Jim", "Jill", "Jack"]
last_names = ["Doe", "Smith", "Brown", "White", "Black"]
ages = [23, 24, 25, 26, 27]

""" Treeview """
table = ttk.Treeview(master=window, columns=("First Name", "Last Name", "Age"), show="headings")
table.heading("First Name", text="First Name")
table.heading("Last Name", text="Last Name")
table.heading("Age", text="Age")
table.pack()

""" add data """

for i in range(1, 5):
    table.insert("", "end", values=(first_names[i], last_names[i], ages[i]))


""" Insert Data dynamically"""
table.insert(parent="", index=0, values=("Tom", "Jerry", 30))


""" Events"""
def select(event):
    for i in table.selection():
        print(table.item(i)["values"])
    
table.bind("<<TreeviewSelect>>", lambda e: select(e) )
table.bind("<Delete>", lambda e: table.delete(table.selection()) )

""" run """
window.mainloop()