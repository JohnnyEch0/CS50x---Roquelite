""" Copied from tkinter folder, this is V2 """

import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

class App(ttk.Window):
    def __init__(self, player, level):
        # Main Setup
        super().__init__(themename = "darkly")
        self.title = ("Main Game Loop GUI")
        self.geometry("800x450")
        self.minsize(400, 225)
        self.layout_setup()

        # data from the game
        self.player = player

        # do we really need the level?
        self.level = level

        # Menu Variables
        self.show_log = tk.IntVar(value=1)

        # menu setup
        self.main_menu = Menu(self)
        self.config(menu=self.main_menu)

        # create Widgets 
        self.input_widget = Input(self)
        self.main_frame = Main_Frame(self)
        self.log_frame = Log_Frame(self)

        """ We need the mainloop to stop while the game is processing events"""
        
        # run
        
    
    def layout_setup(self):
        screen_width = self.winfo_screenwidth() # get the screen width
        screen_height = self.winfo_screenheight() # get the screen height
        self.maxsize(screen_width, screen_height)
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=5)
        self.rowconfigure(1, weight=2)

    
class Menu(tk.Menu):
    """ This should be the menu at the top of the window"""
    def __init__(self, parent):
        super().__init__(parent)
        self.create_sub_menus(parent)

    def create_sub_menus(self, parent):
        window_menu = tk.Menu(self, tearoff=False)
        window_menu.add_checkbutton(label="Hide Log", onvalue=1, offvalue=0, command= lambda: self.f_show_log(parent))
        self.add_cascade(label="Windows", menu=window_menu)

    def f_show_log(self, parent):
        """ Waiting for the Log to be implemented"""
        print("Show Log")
        # print(parent.show_log.get())
        if parent.log_frame.winfo_ismapped():
            parent.log_frame.grid_forget()

            parent.main_frame.grid(row=0, column=0,columnspan=2, sticky="nsew")
            parent.main_frame.update()

            parent.input_widget.grid(row=1, column=0, columnspan=2, sticky="nsew")
            
            # parent.input_widget.update()
        else:
            parent.log_frame.grid(row=0, column=1,rowspan=2, sticky="nsew")

            parent.main_frame.grid(row=0, column=0,columnspan=1, sticky="nsew")
            parent.main_frame.update()

            parent.input_widget.grid(row=1, column=0, columnspan=1, sticky="nsew")
            # parent.input_widget.update()


class Input(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.grid(row=1, column=0, columnspan=1, sticky="nsew", padx=5, pady=5)

        self.input = tk.StringVar(value=None)
        self.create_widgets()

    def create_widgets(self, options=None):
        """ This function should get options as an argument and create buttons for each option """
        """ Options are a tuple of a string and the value to be returned when the button is clicked"""
        self.columnconfigure((0,1,2,3), weight=1, uniform="group1")
        self.rowconfigure((0, 1), weight=1, uniform="group1")

        answer_for_game = tk.StringVar(value=None)
        if not options:
            button1 = ttk.Button(self, text="Useless Option 1", command= lambda: print("Useless Option 1"))
            button2 = ttk.Button(self, text="Placeholder Option 2", command= lambda: print("Useless Option 2"))
            # place widgets
            button1.grid(row=1, column=0, sticky="nsew")
            button2.grid(row=1, column=1, sticky="nsew")
            return
        
        else:

            for i, option in enumerate(options):
                # Fix: Modify the lambda function to capture the current value of 'option'
                button = ttk.Button(self, 
                                    text=option[0], 
                                    command= lambda option=option: self.input.set(option[1]),

                                    )
                button.grid(row=1, column=i, sticky="nsew", padx=5, pady=5)
    
    def update(self, options):
        """ This function should update the buttons based on the options provided and return the selected option"""

        # destroy old widgets
        for widget in self.winfo_children():
            widget.destroy()
        # reset the input var
        self.input.set(None)

        # create new widgets
        self.create_widgets(options)

        # wait for and return the input
        self.wait_variable(self.input)
        input = self.input.get()
        for widget in self.winfo_children():
            widget.destroy()
        return input

class Main_Frame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.grid(row=0, column=0, columnspan=1, sticky="nsew")
        label = ttk.Label(self, text="Main Frame")
        label.grid(row=0, column=0, sticky="nsew")
    
    def update_stats(self):
        # destroy old widgets
        for widget in self.winfo_children():
            widget.destroy()
        # stat_points_spent = tk.IntVar(value=0)

        # layout
        self.rowconfigure(0, weight=2) # column for main label
        self.rowconfigure((1, 2), weight=1) # columns for the stats
        self.rowconfigure(3, weight=2) # column for main label
        self.columnconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform="group1")

        # label
        label = ttk.Label(self, text="Stat Upgrade's")
        label.grid(row=0, column=0, columnspan=6, sticky="nsew")

        # create the stat upgrade labels
        stats = ["health", "attack", "spell_attack", "defense", "spell_def", "initiative"]
        # create a dictionary to store the stat points spent
        stat_points_spent = {stat: 0 for stat in stats}
        # create a d
        for i, stat in enumerate(stats):
            label = ttk.Label(self, text=stat)
            label.grid(row=1, column=i, sticky="nsew")

            # let the user spent exactly 6 points on stats
            # each spinbox needs an individual value
            

            spinbox = ttk.Spinbox(self, from_=0, to=6, textvariable=lambda stat=stat: stat_points_spent[stat])
            spinbox.grid(row=2, column=i, sticky="nsew")

            # when this spinbox is changed, update the stat_points_spent dictionary
            spinbox.bind("<FocusOut>", lambda event, stat=stat: stat_points_spent.update({stat: event.widget.get()}))

        # okay button
        okay = tk.IntVar(value=0)
        button = ttk.Button(self, text="Okay", command= lambda: okay.set(1))
        button.grid(row=3, column=0,columnspan=6, sticky="nsew")
        while True:
            self.wait_variable(okay)
            # convert the values in the dictionary to integers
            stat_points_spent = {key: int(value) for key, value in stat_points_spent.items()}

            # convert the values of the dictionary to a list
            stat_points_spent_values = list(stat_points_spent.values()) 

            # convert the values of the list to integers
            stat_points_spent_values = [int(value) for value in stat_points_spent_values]

            
            stat_points_spent_sum = sum(stat_points_spent_values)
            if stat_points_spent_sum == 6:
                for widget in self.winfo_children():
                    widget.destroy()

                return stat_points_spent
            okay.set(0)

    def print_level_up_info(self, old_stats, new_stats):
        # print the difference between the old and new stats
        self.rowconfigure(0, weight=2)
        self.rowconfigure((1, 2, 3, 4, 5, 6), weight=1)
        self.columnconfigure((0, 1, 2), weight=1)
        self.rowconfigure(7, weight=2)

        label = ttk.Label(self, text="Your Stats have been upgraded")
        label.grid(row=0, column=0, columnspan=3, sticky="nsew")

        for i, stat in enumerate(old_stats):
            label = ttk.Label(self, text=f"{stat}: {old_stats[stat]} -> {new_stats[stat]}")
            label.grid(row=i+1, column=0, sticky="nsew")
        
        for i, stat in enumerate(new_stats):
            label = ttk.Label(self, text=f"{stat}: {old_stats[stat]} -> {new_stats[stat]}")
            label.grid(row=i+1, column=1, sticky="nsew")
        
        okay = tk.IntVar(value=0)

        button = ttk.Button(self, text="Okay", command= lambda: okay.set(1))
        button.grid(row=7, column=0, columnspan=3, sticky="nsew")
        while True:
            self.wait_variable(okay)
            for widget in self.winfo_children():
                widget.destroy()
            return True

class Log_Frame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.grid(row=0, column=1, rowspan=2, sticky="nsew")
        label = ttk.Label(self, text="Log Frame")
        label.grid(row=0, column=0, sticky="nsew")





        

# run
# app = App()