"""
Widgets can have a custom size


"""
import tkinter as tk
from tkinter import ttk

""" Setup """
window = tk.Tk()
window.title("Layout")
window.geometry("600x400")

""" Widgets """
label1 = ttk.Label(master=window, text="Label 1", background="red")
label2 = ttk.Label(master=window, text="Label 2", background="blue")
# The width of a Widget is in characters, not pixels - it's strange.

""" Layout via Pack """
# label1.pack()
# label2.pack(fill="x")
# setting fill to x will increase the width of the widget.

""" Layout via Grid """
window.columnconfigure((0, 1), weight=1, uniform="group1")
window.rowconfigure((0,1), weight=1, uniform="group1")

label1.grid(row=0, column=0)
label2.grid(row=0, column=0, sticky="ew") 



""" Stacking order"""
# Widgets are always created ontop of each other when created, not when placed.
# you can raise widgets individually, ontop of another or at the very top.

button1 = ttk.Button(master=window, text="Lift Label 1", command= lambda: label1.lift())
button2 = ttk.Button(master=window, text="Lift Label 2", command= lambda: label2.lift())

button1.grid(row=0, column=1)
button2.grid(row=1, column=1)

""" Run """
window.mainloop()