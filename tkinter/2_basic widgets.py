import tkinter as tk
from tkinter import ttk 
import ttkbootstrap as ttk

""" the x.configure() can be called for a help"""


""" A function to be called when the button is clicked, it will print the text from the input field to console"""
def button_func():
    input_text = entry.get() # get the text from the input field
    print(input_text) # print the text to the console
    entry.delete(0, tk.END) # clear the input field
    entry["state"] = "disabled" # disable the input field



# create a window
window = ttk.Window(themename = "darkly")
window.title("Window and Widgets") # set the title of the window
window.geometry("300x500") # set the size of the window

# create widget to yell Hello, World!
label = ttk.Label(master=window, text="Hello, World!", font = "Arial 20 bold") # create a label
label.pack() # add the label to the window

""" A Label for the input field """
label = ttk.Label(master=window, text="Input Field", font = "Arial 20 bold") # create a label
label.pack() # add the label to the window

""" A text field for multi-line text input"""
ttk.Text(master=window, width=30, height=10).pack() # create a text field and pack it in the same line

""" ttk entry is a single line text input """
entry = ttk.Entry(master=window, width=30) # create an entry field
entry.pack() # add the entry field to the window

""" ttk button is a button """
button = ttk.Button(master=window, text="Submit", command= button_func) # create a button
button.pack() # add the button to the window


# run mainloop
window.mainloop() # run the window

