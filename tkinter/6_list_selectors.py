import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

""" Setup """
window = ttk.Window(themename = "darkly")
window.title("List Selectors")
window.geometry("400x400")

""" Dropdown / Combobox """
""" create a list and assign it to the values. """
items = ("item 1", "item 2", "item 3", "item 4", "item 5")
item_string = tk.StringVar(value= items[0])
combo = ttk.Combobox(master=window, values= items, textvariable= item_string)
combo.pack()

""" Dropdown an Item was Selected- Event"""
combo.bind("<<ComboboxSelected>>", lambda e: combo_lavel.config(text= f"Selected: {item_string.get()}") ) # when an item is selected

combo_lavel = ttk.Label(master=window, text="Dropdown")
combo_lavel.pack()

""" Spinbox """
spint_int = tk.IntVar(value= 0)

spin = ttk.Spinbox(master=window, from_=0, to=6, textvariable= spint_int, wrap= False)
# spin["value"] = (1, 2, 3, 4, 5) # alternative to from_ and to

""" Spinbox Events """
spin.bind("<<Increment>>", lambda e: print("Incremented") )
spin.bind("<<Decrement>>", lambda e: print("Decremented"))
spin.bind("<Return>", lambda e: print("Return"))

spin.pack()

""" Run """
window.mainloop() # run the window