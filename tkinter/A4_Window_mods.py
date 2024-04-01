import tkinter as tk
from tkinter import ttk

""" Setup """
window = tk.Tk()
window.title("Window and Widgets")
window.geometry("800x600+300+400") # x is the width, y is the height, +startx+starty
# window.iconbitmap("favicon.ico") # set the icon of the window

""" Window sizes """
window.minsize(200, 200) # set the minimum size of the window, you should always set 
window.maxsize(1960, 1280) # set the maximum size of the window
window.resizable(True, True) # set the window to be resizable in the x and y directions

""" Screen attributes """
screen_width = window.winfo_screenwidth() # get the screen width
screen_height = window.winfo_screenheight() # get the screen height

""" Window Attributes """
window.attributes("-alpha", 0.5) # set the transparency of the window
window.attributes("-topmost", True) # set the window to be on top of all other windows (win-scale)

""" Security Event """
window.bind("<Escape>", lambda event: window.quit()) # bind the escape key to close the window

# window.attributes("-disabled", True) # disable the window, useless
# window.attributes("-fullscreen", True) # set the window to be fullscreen

""" Title Bar - removes resizing and easy quitting"""
window.overrideredirect(True) # removes the title bar

# reintroduce resizing
grip = ttk.Sizegrip(master=window) # create a size grip for resizing
grip.place(relx=1.0, rely=1.0, anchor= "se") # place the size grip in the bottom right corner 




""" A Label for the input field """

"""run"""
window.mainloop() # run the window