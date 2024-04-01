import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def get_pos(event):
    print(event.x, event.y)

# setup
window = ttk.Window(themename = "darkly")
window.title("Buttons Demo")
window.geometry("400x400")

""" widgets """


entry = ttk.Entry(master=window)
entry.pack()

btn = ttk.Button(master=window, text="Click Me")
btn.pack()

""" events """
btn.bind("<Alt-KeyPress-a>", lambda e: print(e)) # alt + a on the button
window.bind("<Motion>", get_pos) # mouse movement on the window

window.bind("<KeyPress>", lambda e: print(e.char)) # any key press on the window

entry.bind("<FocusIn>", lambda e: print("Focus In")) # focus in on the entry-field


""" run """
window.mainloop() # run the window