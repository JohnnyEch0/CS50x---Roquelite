""" tkinter widgets (usually frames) are created via inheritance"""
""" You should always use the class based approach when working on more complex projects. """
import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self, title, size):
        # Main Setup
        super().__init__()
        self.title = title
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])

        # create Widgets
        self.menu = Menu(self)
        self.main = Main(self)

        # run
        self.mainloop()

class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.place(x=0, y=0, relwidth=0.3, relheight=1)
        self.create_widgets()


    def create_widgets(self):
        menu_button1 = ttk.Button(self, text="Button 1", command= lambda: print("Button 1"))
        menu_button2 = ttk.Button(self, text="Button 2", command= lambda: print("Button 2"))
        menu_button3 = ttk.Button(self, text="Button 3", command= lambda: print("Button 3"))

        menu_slider1 = ttk.Scale(self, from_=0, to=100, orient="vertical")
        menu_slider2 = ttk.Scale(self, from_=0, to=100, orient="vertical")

        toggle_frame = ttk.Frame(self)
        menu_toggle = ttk.Checkbutton(toggle_frame, text="Toggle 1", command= lambda: print("Toggle 1"))
        menu_toggle_2 = ttk.Checkbutton(toggle_frame, text="Toggle 2", command= lambda: print("Toggle 2"))

        entry = ttk.Entry(self)
        
        self.columnconfigure((0,1,2), weight=1, uniform="group1")
        self.rowconfigure((0,1,2,3), weight=1, uniform="group1")

        # place widgets
        menu_button1.grid(row=0, column=0, sticky="nsew", columnspan=2)
        menu_button2.grid(row=0, column=2, sticky="nsew")
        menu_button3.grid(row=1, column=0, sticky="nsew", columnspan=3)

        menu_slider1.grid(row=2, column=0, rowspan=2, sticky="nsew", pady=20)
        menu_slider2.grid(row=2, column=1, rowspan=2, sticky="nsew", pady=20)

        # toggle layout
        toggle_frame.grid(row=4, column=0, columnspan=3, sticky="nsew")
        menu_toggle.pack(side="left", expand=True, fill="both")
        menu_toggle_2.pack(side="left", expand=True, fill="both")

        entry.place(relx=0.5, rely=0.95, relwidth=0.9, anchor="center")

        
class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)

        self.frame1 = Frame1(self)
        self.frame2 = Frame1(self, "Frame 2", "Button 2", "blue")
        
        


        # self.create_widgets()

class Frame1(ttk.Frame):
    def __init__(self, parent, label_text="Frame 1", button_text="Button 1", label_bg="red"):
        super().__init__(parent)
        self.create_widgets(label_text, button_text, label_bg)
        self.pack(side= "left", expand=True, fill="both", padx=10, pady=10)

    def create_widgets(self, label_text="Frame 1", button_text="Button 1", label_bg="red"):
        label1 = ttk.Label(self, text=label_text, background=label_bg)
        button1 = ttk.Button(self, text=button_text, command= lambda: print("Button 1"))
        label1.pack(expand=True, fill="both")
        button1.pack(expand=True, fill="both", pady=10)
        

""" Run """
App("tk-Classes", (800, 800))