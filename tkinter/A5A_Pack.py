""" pack has arguments: side, anchor, fill, expand, ipadx, ipady, padx, pady"""

import tkinter as tk
from tkinter import ttk

""" Setup """
window = tk.Tk()
window.title("Layout")
window.geometry("600x400")

""" Widgets """
label1 = ttk.Label(master=window, text="Label 1", background="red")
label2 = ttk.Label(master=window, text="Label 2", background="blue")
label3 = ttk.Label(master=window, text="Label 3", background="green")
button1 = ttk.Button(master=window, text="Button 1", command= lambda: print("Button 1"))

""" Layout via Pack """
label1.pack(side= "left", expand=True, fill="both", padx = 10, pady=10)
label2.pack(side= "left", fill="both", ipadx=90 )
label3.pack(side= "left", fill="both" )
button1.pack(side= "left", fill=   "x", expand=True )

""" EXPAND AND FILL
tkinter has 2 kinds of space: the spave a widget can take up, and the space a widget will occupy. 
when expand is true, a widget will be able take up all the space it can get.
fill will fill the space it has been given., it can be x, y, both, none
"""

""" PADDING
padx and pady will add padding around the widget
ipadx and ipady will add padding inside the widget
"""

""" Layout via Grid """


""" Run """
window.mainloop()
