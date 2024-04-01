import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

# setup
window = ttk.Window(themename = "darkly")
window.title("Buttons Demo")
window.geometry("400x400")

# button
def button_func():
    print("Button clicked")

button_string = tk.StringVar(value= "A button w a string var")

button = ttk.Button(master=window, text="Click Me", command= button_func, textvariable= button_string) 
# command = lambda: print("Button clicked") # alternative to button_func

button.pack()

""" Checkbox """
check_var = tk.BooleanVar(value = True) # value sets a default

check = ttk.Checkbutton(master=window, 
                        text="Check Me", 
                        command= lambda: print(check_var.get()), # returns 1 or 0
                        variable= check_var
                        )

check.pack()

""" Radio Buttons are connected by default, only one can be selected at a time, seperated by value"""
radio_var = tk.StringVar()
radio = ttk.Radiobutton(master=window, 
                        text="Radio Me", 
                        value= "radio",
                        variable= radio_var,
                        command= lambda: print(radio_var.get())
                        )
radio.pack()

radio2 = ttk.Radiobutton(master=window, 
                        text="Radio Me 2", 
                        value= "radio2",
                        variable= radio_var,
                        command= lambda: print(radio_var.get())
                        )
radio2.pack()

""" Scale """


# run
window.mainloop() # run the window