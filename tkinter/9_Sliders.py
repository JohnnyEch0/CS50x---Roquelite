""" Sliders in tkinter: Progress Bars and Sliders"""

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

""" Setup """
window = tk.Tk()
window.title("Sliders")
window.geometry("400x400")

""" Sliders """


""" Sliders can be moved by the user """

scale_int = tk.IntVar(value= 15)
scale = ttk.Scale(master=window, 
                  command= lambda value: print("test", value), 
                  orient="horizontal",
                  from_=0, to=100, length=200,
                  variable= scale_int)
scale.pack()

""" Progress Bar """
""" Progress Bars are sliders that are not interactive """
""" They have a start and a stop method , that are weird."""

progress = ttk.Progressbar(master=window, variable= scale_int, orient="horizontal", length=200, mode="determinate")
progress.pack()

""" scrollable text input folder"""

scrolled_text = scrolledtext.ScrolledText(master=window, wrap= tk.WORD, width= 40, height= 10)
scrolled_text.pack()

""" Usually its way better to create your own scrollable text input, but this is a quick way to do it."""





""" run """
window.mainloop() # run the window