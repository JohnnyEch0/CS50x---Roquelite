import tkinter as tk
from tkinter import ttk # widgets we want to use
import ttkbootstrap as ttk # theme

def convert():
    input_text = entry_int.get() # get the text from the input field
    # output.config(text="Out: " + input_text) # set the text of the output field
    output_string.set("Out: " + str(input_text)) # set the text of the output field 2
    
    # entry,get is not optimal


window = tk.Tk() # create a window
# window = ttk.Window(themename = "darkly") # create a window with a theme


window.title("Demo") # set the title of the window
window.geometry("500x500") # set the size of the window

# title
title_lavel = ttk.Label(master=window, text="Hello, World!", font = "Arial 20 bold") # create a title
title_lavel.pack() # add the title to the window

# input field
input_field = ttk.Entry(master=window, width=30) # create an input field
input_field.pack() # add the input field to the window

""" # input field 2 with a seperate Frame and Button """
input_frame = ttk.Frame(master=window) # create a frame for widgets
 
entry_int = tk.IntVar() # create a variable to store the input
entry = ttk.Entry(master=input_frame, width=30, textvariable = entry_int) # create an input field

button = ttk.Button(master=input_frame, text="Submit", command = convert) # create a button for submit

entry.pack(side="left", padx= 10) # add the input field to the frame
button.pack(side="left")
input_frame.pack(pady=10) # add the frame to the window

# output
output_string = tk.StringVar() # create a variable to store the output
output = ttk.Label(master=window, 
                   text="Out: ", 
                   font = "Arial 20", 
                   textvariable=output_string) # create an output field


output.pack() # add the output field to the window


# run
window.mainloop() # run the window
