""" We can set up a grid for the window, and then place the frames in the grid. 
We can determine rows, columns and weights for the grid.
--- STICKY ARGUMENT ---
However, we have to use sticky so that the frames fill the space.
Default: widget will be centered in the cell.
when we give more then one direction, the widget will expand in that direction.

"""
import tkinter as tk
from tkinter import ttk

""" Setup """
window = tk.Tk()
window.title("Layout with Grids")
window.geometry("600x400")

""" Widgets """
label1 = ttk.Label(master=window, text="Label 1", background="red")
label2 = ttk.Label(master=window, text="Label 2", background="blue")
label3 = ttk.Label(master=window, text="Green Label 3", background="green")
label4 = ttk.Label(master=window, text="yellowlabel", background="yellow")
button1 = ttk.Button(master=window, text="Button 1", command= lambda: print("Button 1"))

""" Grid Setup """
window.columnconfigure((0, 1, 2, 3), weight=1, uniform="group1") # uniform will keep the widgets from taking more space then they should.
window.rowconfigure((0, 1, 2), weight=1, uniform="group1")



""" place the widgets in the grid """
label1.grid(row=0, column=0, sticky="nsew")
label2.grid(row=0, column=2, sticky = "nsew")
button1.grid(row=1, column=2, sticky="ns", rowspan=2, columnspan=2)
label3.grid(row=2, column=2, sticky="nsew", ipadx=10, ipady=10) # this will push the borders of other cells, beware!
label4.grid(row=2, column=4, sticky="se", padx=10, pady=10)


""" PADDINGS
padx and pady will add padding around the widget
ipadx and ipady will add padding inside the widget - makes it larger and pushes other cells
"""

""" UNIFORMITY ISSUE
empty cells will be filled by widgets?

"""

""" run """
window.mainloop()
