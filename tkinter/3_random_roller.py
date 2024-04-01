import tkinter as tk
from tkinter import ttk 
import ttkbootstrap as ttk
import random as r
import dat_4_tk

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# import ../db.py
import utils

def roll_random_Trader():
    """ A function to be called when the button is clicked, it will print the text from the input field to console"""
    roll = roll = utils.random_choice_list_tuple(dat_4_tk.npc_traders)
    output_string.set(roll) # set the text of the output field


# create a window
window = ttk.Window(themename = "darkly")
window.title("Random Roller Alpha 1.0") # set the title of the window
window.geometry("800x500") # set the size of the window

""" Title """
label = ttk.Label(master=window, text="What would you like to roll?", font = "Arial 15 bold") # create a label
label.pack() # add the label to the window


""" ttk button is a button """
button = ttk.Button(master=window, text="Trader", command= roll_random_Trader) # create a button
button.pack(side="left", padx=10) # add the button to the window

""" Output"""
output_string = tk.StringVar() # create a variable to store the output
output = ttk.Label(master=window, 
                   text="Out: ", 
                   font = "Arial 14", 
                   textvariable=output_string) # create an output field
output.pack(side="left") # add the output field to the window



"""run mainloop"""
window.mainloop() # run the window