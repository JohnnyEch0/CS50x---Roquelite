""" More complex Layouts with Containers/Frames"""
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk # theme
    
""" Setup """
window = ttk.Window(themename = "darkly")
window.geometry("400x400")
window.title("Frames and Parenting")

"""create a frame"""
frame = ttk.Frame(master=window, width= 200, height= 200, borderwidth=10, relief= tk.GROOVE )
frame.pack_propagate(False) # set the size of the frame to the size of the label
frame.pack(side= tk.LEFT)

""" master setting"""
label = ttk.Label(master=frame, text="Hello, World!", font = "Arial 15 bold") # create a label
label.pack() # add the label to the window

""" TTK tries to create the size of the frame to fit the label, but it can be set manually"""
button = ttk.Button(master=frame, text="Submit", command= lambda: print("Button Pressed")) # create a button
button.pack() # add the button to the window

""" label outside the frame"""
label = ttk.Label(master=window, text="Hello, World!", font = "Arial 15 bold") # create a label
label.pack() # add the label to the window

""" Another Frame"""

""" run """
window.mainloop() # run the window