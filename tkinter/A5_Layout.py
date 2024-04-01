"""
3 Major Methods for Layout:
1. pack()
    Pack will always put widgets under each other.
    But you can also go left to right, or right to left.
2. grid()
    Grid will put widgets in a grid.
    You can specify the row and column.
    Grid is really flexible 
3. place()
    Place will put widgets in a specific place.
    You can specify the x and y coordinates.
    Place is really flexible, but it is not recommended to use it.
    Because it is not responsive.
You can combine these methods.
Everything will rely on parenting and frames.

"""

import tkinter as tk
from tkinter import ttk

""" Setup """
window = tk.Tk()
window.title("Layout")
window.geometry("600x400")

""" Widgets """
label1 = ttk.Label(master=window, text="Label 1", background="red")
label2 = ttk.Label(master=window, text="Label 2", background="blue")

""" Pack """
# label1.pack(side="left")
# label2.pack(side="left", expand=True, fill="both") # fill will fill the space, expand will expand the space
# fill can be x, y, both, none


""" Grid """
'''

window.columnconfigure(0, weight=1) 
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=2) # this column will be twice as big as the other columns
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)

label1.grid(row=0, column=1, sticky="nsew") # sticky will stick the widget to the sides - to which border it is going to stick
# takes compass directions: n, s, e, w, ne, nw, se, sw
label2.grid(row=1, column=1, columnspan= 2,sticky="nsew")

'''

""" Place """
label1.place(x=0, y=0, width=200) # x and y coordinates, place it at the top left corner
label2.place(relx=0.5, rely=0.5, height=100, anchor = "center") # relational x and y, between 0 and 1, 0.5 is the middle
# anchor by default is NW
""" When using place, use relx and rely, because it is responsive."""



""" run """
window.mainloop() 