""" Tabs via ttk.Notebook"""
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk # theme

""" Setup """
window = ttk.Window(themename = "darkly")
window.geometry("400x400")
window.title("Tabs")

""" create a Notebook, they need tabs"""
notebook = ttk.Notebook(master=window)

# tab 1
tab1 = ttk.Frame(master=notebook)
label1 = ttk.Label(master=tab1, text="Hello, World! - said Tab 1", font = "Arial 10 ") # create a label
label1.pack()


tab2 = ttk.Frame(master=notebook)
label2 = ttk.Label(master=tab2, text="Hello, World! - said Tab 2", font = "Arial 10") # create a label
label2.pack()

""" add tabs to the notebook"""

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.pack()



""" run """
window.mainloop()