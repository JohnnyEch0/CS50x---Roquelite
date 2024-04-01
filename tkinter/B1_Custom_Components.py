""" Creating custom components for tkinter """
""" Functional approach: creating a widget inside of a function an return it.
    use this for smaller components
"""

""" Pause at 7:26"""

import tkinter as tk
from tkinter import ttk

def create_segment(parent, label_text, button_text):
    frame = ttk.Frame(parent)
    frame.rowconfigure(0, weight=1)
    frame.columnconfigure((0,1,2), weight=1, uniform="group1")
    ttk.Label(frame, text=label_text).grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    ttk.Button(frame, text=button_text, command= lambda: print(button_text)).grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
    frame.pack(expand=True, fill="both")
    return frame


class Segment(ttk.Frame):
    def __init__(self, parent, label_text, button_text):
        super().__init__(master = parent)

        # grid
        self.rowconfigure(0, weight=1)
        self.columnconfigure((0,1,2), weight=1, uniform="group1")
        ttk.Label(self, text=label_text).grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        ttk.Button(self, text=button_text, command= lambda: print(button_text)).grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.create_widgets("exercise").grid(row=0, column=2, sticky="nsew")

        self.pack(expand=True, fill="both")

    
    def create_widgets(self, text):
        print("Creating widgets")
        frame = ttk.Frame(self)
        ttk.Label(frame, text= text ).pack(expand=True, fill="both", padx=10, pady=10, )
        ttk.Button(frame, text= text).pack(expand=True, fill="both", padx=10, pady=10, )
        return frame
        

window = tk.Tk()
window.title("Custom Components")
window.geometry("500x500")


# create widgets
Segment(window, "Label 1", "Button 1")
Segment(window, "Label 2", "Button 2")
# Segment(window, "Label 3", "Button 3")
# Segment(window, "Label 4", "Button 5")

# Create Widgets using function
create_segment(window, "First Label", "Button 1").pack(expand=True, fill="both", padx=10, pady=10)
create_segment(window, "Label 2", "Button 2").pack(expand=True, fill="both", padx=10, pady=10)
create_segment(window, "Label 3", "Button 3").pack(expand=True, fill="both", padx=10, pady=10)
create_segment(window, "Last Label", "Button 4").pack(expand=True, fill="both", padx=10, pady=10)

# run

window.mainloop()
