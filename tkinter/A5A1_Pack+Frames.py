""" More complicated layouts with pack and frames 
Always create single direction layouts
Some items are frames, containing their own layout
"""
import tkinter as tk
from tkinter import ttk

""" Setup """
window = tk.Tk()
window.title("Layout")
window.geometry("600x400")

""" Widgets """
""" 
Code Structure should be creating the things one after another and in parent-child rows
Later you can pack them in the right order
"""
# Top Frame
top_frame = ttk.Frame(master=window)

tf_label = ttk.Label(master=top_frame, text="Top Frame - Label", background="red")
tf_label.pack(expand=True, fill="both")
tf_label2 = ttk.Label(master=top_frame, text="Top Frame - Label 2", background="yellow")
tf_label2.pack(expand=True, fill="both")

top_frame.pack(expand=True, fill="both")

# Middle Widget

mid_button = ttk.Button(master=window, text="Button 1", command= lambda: print("Button 1"))
mid_button.pack(expand=True, fill="both")

# Low Frame

low_frame = ttk.Frame(master=window)
lf_left_frame = ttk.Frame(master=low_frame)

# Low - Left Frame

lf_left_label = ttk.Label(master=lf_left_frame, text="Low Frame - Label", background="green")
lf_left_label.pack(expand=True)

lf_left_frame.pack(side="left", expand=True, fill="both")

# Low - Right Frame

lf_right_frame = ttk.Frame(master=low_frame)

lf_rf_button1 = ttk.Button(master=lf_right_frame, text="boddom right Button 2", command= lambda: print("Button 2"))
lf_rf_button1.pack(expand=True)
lf_rf_button2 = ttk.Button(master=lf_right_frame, text="boddom right Button 3", command= lambda: print("Button 3"))
lf_rf_button2.pack(expand=True)

lf_right_frame.pack(side="left", expand=True, fill="both")

# Pack Low
low_frame.pack(expand=True, fill="both")


""" Run """
window.mainloop()