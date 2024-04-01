import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk # theme


""" Setup """
window = ttk.Window(themename = "darkly")
window.geometry("800x450")
window.title("Main Game Loop GUI")

screen_width = window.winfo_screenwidth() # get the screen width
screen_height = window.winfo_screenheight() # get the screen height

""" Layout Configuration """
window.maxsize(screen_width, screen_height)
window.columnconfigure(0, weight=2)
window.columnconfigure(1, weight=1)
window.rowconfigure(0, weight=4)
window.rowconfigure(1, weight=2)

"""Menu Setup"""
menu = tk.Menu(window, tearoff=False)
window.config(menu=menu)



""" Menu : Windows """
show_log = tk.IntVar(value=1)
window_menu = tk.Menu(menu, tearoff=False)
window_menu.add_checkbutton(label="Hide Log", onvalue=1, offvalue=0, command= lambda: f_show_log())

menu.add_cascade(label="Windows", menu=window_menu)

""" Menu Functions """
def f_show_log():
    print(show_log.get())
    if frame_log.winfo_ismapped():
        frame_log.grid_forget()

        frame_main.grid(row=0, column=0,columnspan=2, sticky="nsew")
        frame_main.update()

        frame_input.grid(row=1, column=0, columnspan=2, sticky="nsew")
        
        frame_input.update()
        """ BUG: When the log is hidden, the inp"""

    else:
        print("place")
        frame_log.grid(row=0, column=1,rowspan=2, sticky="nsew")
        frame_main.grid(row=0, column=0,columnspan=1, sticky="nsew")
        frame_main.update()
        frame_input.grid(row=1, column=0, columnspan=1, sticky="nsew")
        frame_input.update()
        # shrink the main and input frame
        # frame_main.grid(row=0, column=0,columnspan=1, sticky="nsew")



""" Frames """
""" 
Main Frame
    This may hold Movement, Battle, and Inventory Frames
"""
frame_main = ttk.Frame(master=window, borderwidth=10, relief= tk.GROOVE )
frame_main.pack_propagate(False) # set the size of the frame to the size of the label
frame_main.grid(row=0, column=0, sticky="nsew", columnspan=2)








""" Frame for possible Inputs """
frame_input = ttk.Frame(master=window, borderwidth=10, relief= tk.GROOVE )
frame_input.pack_propagate(False) # set the size of the frame to the size of the label
# frame_input.pack(anchor="w",side= tk.BOTTOM)
frame_input.grid(row=1, column=0, sticky="nsew", columnspan=2)

""" Frame for activity log that can be collapsed"""
""" Should be scrollable, Position: Right, height across the whole window"""
frame_log = ttk.Frame(master=window, borderwidth=10, relief= tk.GROOVE )
frame_log.pack_propagate(False) # set the size of the frame to the size of the label
frame_log.grid(row=0, column=1,rowspan=2, sticky="nsew")



""" run """
window.mainloop() # run the window

