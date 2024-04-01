""" you dont really hide(reveal) widgets in tkinter, you can just remove(add) them from the screen. """
import tkinter as tk
from tkinter import ttk

""" Setup """
window = tk.Tk()
window.title("Layout")
window.geometry("600x400")

""" Functions """
def toggle_label1():
    # can also be done via a global variable
    if label1.winfo_ismapped():
        label1.place_forget()
    else:
        label1.place(relx=0.5, rely=0.5, anchor="center")


""" Widgets """
button1 = ttk.Button(master=window, text="toggle label 1", command = toggle_label1)
button1.place(relx=0.5, rely=0.1, anchor="center")

label1 = ttk.Label(master=window, text="Label 1", background="red")
label1.place(relx=0.5, rely=0.5, anchor="center")


""" Run """
window.mainloop()