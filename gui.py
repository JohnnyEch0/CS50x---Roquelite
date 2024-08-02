""" Graphical User Interface for the Main Game Loop """

import datetime
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from data.input_dicts import direction_placements

class App(ttk.Window):
    """ Main GUI for the Main Game Loop"""
    def __init__(self, player, level):
        # Main Setup
        super().__init__(themename = "darkly")
        self.title = ("Main Game Loop GUI")
        self.geometry("1600x900")
        self.attributes("-fullscreen", True)
        self.minsize(400, 225)
        self.layout_setup()

        # data from the game
        self.player = player

        # do we really need the level? -> yeah for the map
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

        # place widgets
        self.main_frame.grid(row=0, column=0, columnspan=1, sticky="nsew")
        self.input_widget.grid(row=1, column=0, columnspan=1, sticky="nsew")
        self.log_frame.grid(row=0, column=1, rowspan=2, sticky="nsew")

        """ We need the mainloop to stop while the game is processing events"""
        # self.mainloop()
        # stop the mainloop

    
    def update_gui(self) -> None:
        """ This function is called from the main game loop to update the GUI"""
        self.main_frame.player_metrics_update()
        self.main_frame.notebook.map_update()
  
    
    def layout_setup(self):
        """ Creates grid and maxsite for the main window"""
        screen_width = self.winfo_screenwidth() 
        screen_height = self.winfo_screenheight() 
        self.maxsize(screen_width, screen_height)

        # grid configuration
        self.columnconfigure(0, weight=2, uniform="group_main")
        self.columnconfigure(1, weight=1, uniform="group_main")
        self.rowconfigure(0, weight=5, uniform="group_main")
        self.rowconfigure(1, weight=2, uniform="group_main")

    
class Menu(tk.Menu):
    """ Menu at the top of the window"""
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
    """ Input Frame, holds buttons for the player to interact with the game"""
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.columnconfigure((0,1,2,3), weight=1, uniform="group1")
        self.rowconfigure((0, 1, 2), weight=1, uniform="group1")

        self.input = tk.StringVar(value=None)
        self.create_widgets()

    def create_widgets(self, options=None):
        """ 
        This function should get options as an argument and create buttons for each option 
        Options are a tuple of a string and the value to be returned when the button is clicked
        """
        # fallback 
        if not options:
            
            button1 = ttk.Button(self, text="Useless Option 1", command= lambda: print("Useless Option 1"))
            button2 = ttk.Button(self, text="Placeholder Option 2", command= lambda: print("Useless Option 2"))
            # place widgets
            button1.grid(row=1, column=0, sticky="nsew")
            button2.grid(row=1, column=1, sticky="nsew")
            return
        
        # create buttons for each option
        else:

            for i, option in enumerate(options):
                button = ttk.Button(self, 
                                    text=option[0], 
                                    command= lambda option=option: self.input.set(option[1]),
                                    )
                # some buttons should have specific positions
                if option[0] == "move":
                    button.grid(row=2, column=3, sticky="nsew", padx=5, pady=2)
                elif i < 4:
                    button.grid(row=0, column=i, sticky="nsew", padx=5, pady=2)
                elif i < 8:
                    button.grid(row=1, column=i-3, sticky="nsew", padx=5, pady=2)
                if option[0] == "Exit" and not options[0] == "move":
                    button.grid(row=2, column=3, sticky="nsew", padx=5, pady=2)
                
    
    def update(self, options: tuple, type: str = "None"):
        """ This function should update the buttons based on the options provided and return the selected option
            The options are a tuple of strings and a character that will be returned when the button is clicked
        """

        # destroy old widgets
        for widget in self.winfo_children():
            widget.destroy()

        # reset the input var
        self.input.set(None)

        # create new widgets
        if type == "movement":
            self.create_movement_widgets(options)
        else:
            self.create_widgets(options)

        # wait for and return the input
        self.wait_variable(self.input)
        input = self.input.get()
        for widget in self.winfo_children():
            widget.destroy()
        return input

    def create_movement_widgets(self, options):
        """ This function should create buttons for movement options"""
        for i, option in enumerate(options):
            button = ttk.Button(self, 
                                text=option[0], 
                                command= lambda option=option: self.input.set(option[1]),
                                )
            button.grid(row=direction_placements[option[1]][0], column=direction_placements[option[1]][1], sticky="nsew", padx=5, pady=5)


class Main_Frame(ttk.Frame):
    """ 
    The Main Frame of the UI will hold the PLayer Metrics, and a Notebook for the different tabs
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        
        # create a light gray background
        self.configure(style="LightGray.TFrame")

        # layout configuration
        self.layout_setup()

        # level up
        self.level_up = level_up(self)

        # show the player stats
        self.metrics_hud = self.show_player_metrics_hud()

        """ Notebook Approach"""
        # create a notebook
        self.notebook = Main_Notebook(self)
        self.notebook.grid(row=1, column=0, columnspan=4, sticky="nsew")

        

    def layout_setup(self):
        """ 
        Create a flexible Layout for the Main Frame
        Top Row is FIXED for the player metrics
        The rest is for the Notebook
        """
        # layout configuration
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=8)
        self.columnconfigure((0, 1, 2, 3), weight=1)
        
    def recreate_standard_widgets(self):
        self.notebook.grid()
        self.player_metrics_update()

    """ Metrics HUD """
    def show_player_metrics_hud(self):
        """
        This function should display the player stats in the first row of the main frame
        2. player exp/next level
        3. player level
        4. player gold
        """
        # display player health
        health_label = ttk.Label(self, text=f"Health: {self.parent.player.health}/{self.parent.player.max_health}")
        health_label.grid(row=0, column=0, sticky="nsew", padx=5, )

        # display player exp/next level
        exp_label = ttk.Label(self, text=f"Exp: {self.parent.player.exp}/{self.parent.player.exp_to_next}")
        exp_label.grid(row=0, column=1, sticky="nsew", padx=5,)

        # display player level
        level_label = ttk.Label(self, text=f"Level: {self.parent.player.level}")
        level_label.grid(row=0, column=2, sticky="nsew", padx=5, )

        # display player gold
        gold_label = ttk.Label(self, text=f"Gold: {self.parent.player.inventory[0].amount}")
        gold_label.grid(row=0, column=3, sticky="nsew", padx=5, )

    def player_metrics_update(self):
        """ upgrades, player metrics: destroy self and recreate the metrics hud"""
        
        if self.metrics_hud:
            self.metrics_hud.destroy()
        self.show_player_metrics_hud()
    
    """ Level Up """
    def show_level_up(self):
        for widget in self.winfo_children():
            widget.grid_remove()
        self.level_up.grid(row=0, column=0, columnspan=4,rowspan=2, sticky="nsew")
   

class level_up(ttk.Frame):
    """ Show the player the option to level up their stats and, once done, a summary"""
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def layout_setup(self):
        self.rowconfigure(0, weight=2)
        self.rowconfigure((1, 2, 3, 4, 5, 6), weight=1)
        self.columnconfigure((0, 1, 2), weight=1)
        self.rowconfigure(7, weight=2)

    def update_stats(self):
        """ This will be shown in the Level Up, the user can upgrade stats"""

        """ Hide the other widgets
        for widget in self.winfo_children():
            widget.grid_remove()
        """
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
                    widget.grid_remove()

                return stat_points_spent
            okay.set(0)
        
    def print_level_up_info(self, old_stats: dict, new_stats: dict):
        """ This will be shown after leveling up, the user can see the difference in stats
        """
        
        self.rowconfigure(0, weight=2)
        self.rowconfigure((1, 2, 3, 4, 5, 6), weight=1)
        self.columnconfigure((0, 1, 2), weight=3)
        self.rowconfigure(7, weight=2)

        label = ttk.Label(self, text="Your Stats have been upgraded")
        label.grid(row=0, column=0, columnspan=3, sticky="nsew")

        # Show the old and new stats to the player
        for i, stat in enumerate(old_stats):
            # label
            label = ttk.Label(self, text=f"{stat}: ")
            label.grid(row=i+1, column=0, sticky="nsew")
            # old stat
            label = ttk.Label(self, text=f"{old_stats[stat]} -> ")
            label.grid(row=i+1, column=1, sticky="nsew")
            # new stat
            label = ttk.Label(self, text=f" {new_stats[stat]}")
            label.grid(row=i+1, column=2, sticky="nsew")     
        
        okay = tk.IntVar(value=0)

        button = ttk.Button(self, text="Okay", command= lambda: okay.set(1))
        button.grid(row=7, column=0, columnspan=3, sticky="nsew")

        # wait for the player to press okay
        while True:
            self.wait_variable(okay)
            # remove the level-up widgets
            for widget in self.winfo_children():
                widget.grid_remove()
            # reset the layout
            self.parent.recreate_standard_widgets()
            return True
        

class Main_Notebook(ttk.Notebook):
    """ Notebook for the different tabs in the main frame, holds the Narration, Combat, Inventory, Stats and Map Tab"""
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.tabs = self.create_tabs()

    def create_tabs(self):
        # tab one - Narration
        self.narration = Narration(self)

        # tab two - Combat
        self.combat = Combat(self)

        # tab three - Inventory
        self.inventory = Inventory(self)

        # tab four - player stats
        self.stats = PlayerStats(self)

        # tab four - Map
        self.map = self.create_map()
        self.map.pack()
        self.map_update()

        # tab five - Information
        self.info = Info(self)
        self.info.pack()
        

        # add tabs to the notebook
        self.add(self.narration, text="Narration" )
        self.add(self.combat, text="Combat")
        self.add(self.inventory, text="Inventory")
        self.add(self.stats, text="Stats")
        self.add(self.map, text="Map")
        # info is invisible by default
        self.add(self.info, text="Info")
        self.hide(5)
        
   
        self.grid(row=1, column=0, columnspan=4, sticky="nsew")

    def update_tabs(self):
        self.create_tabs()
        self.select(0)

    """ Map Tab """

    def create_map(self):
        """ create 5x5 map tab"""
        map = ttk.Frame(master=self)
        map.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform="group1")
        map.columnconfigure((0, 1, 2, 3, 4), weight=1, uniform="group1")
        map.array = []
        for x in range(5):
            x_array = []
            for y in range(5):
                label = ttk.Label(master=map, text="Room", )
                label.grid(row=x, column=y, sticky="nsew", padx=10, pady=5)
                # draw a box around each room
                label.configure(relief="groove")
                
                x_array.append(label)
            map.array.append(x_array)
        map.array[2][2].configure(background="green")

        """ mark the player position"""
        map.array[2][2].configure(text="Player")
        
        return map

    def map_update(self):
        """ Update the 5x5 map of the rooms around the player"""

        # get the rooms around the player
        rooms = self.parent.parent.level.get_rooms_for_map_hud(self.parent.parent.player.pos[0], self.parent.parent.player.pos[1])

        for i, row in enumerate(rooms):
            for j, room in enumerate(row):
                try:
                    # if the room is not a room, set the text to " " and the relief to flat, so it looks like an empty space
                    if room == "Not a room":
                        self.map.array[i][j].configure(text=" ")
                        self.map.array[i][j].configure(relief="flat")
                        continue
                    # show the room, if it is explored
                    if room.explored:
                        self.map.array[i][j].configure(text=f"{room.scene}")
                    # if the room is not explored, show "unexplored"
                    else:
                        self.map.array[i][j].configure(text="unexplored")

                    self.map.array[i][j].configure(relief="groove")
                except IndexError:
                    print("DEBUG: Index Error in map_update", i, j, room)

    """ Info Tab"""
    def inform(self, items):
        """ Feed items that have a name and a description to the info tab"""
        self.info.update_info(items)
        self.add(self.info, text="Info")
        self.select(5)

class Narration(ttk.Frame):
    """ Narration Tab, will display the narration of the game to the player """
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.text = tk.StringVar(value="This will be the narration Tab")
        self.create_widgets()
        
        self.placeholder = ""
        self.index = 0
        self.type_tempo = 30 # speed of the typing effect


    def create_widgets(self):
        label = ttk.Label(self, textvariable=self.text, font = "Arial 13 ", anchor="w")
        label.pack()
    
    def update_text(self, text):
        try:
            self.placeholder += text[self.index]
            self.text.set(self.placeholder)
            self.index += 1
            self.parent.after(self.type_tempo, self.update_text, text)
        except IndexError:
            self.index = 0
            self.placeholder = ""
            return


class Inventory(ttk.Frame):
    """ Inventory Tab, will display the players inventory"""
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.app = parent.parent.parent
        self.create_widgets()

    def create_widgets(self, inventory=None):
        """ Create a notebok for the inventory"""
        self.item_type_notebook = ttk.Notebook(self)
        equipment = ttk.Frame(self.item_type_notebook)
        consumables = ttk.Frame(self.item_type_notebook)

        # grab equipment from the player
        if not inventory:
            inventory = self.app.player.inventory
        for i, item in enumerate(inventory):
            try:
                if item.equippable:
                    equiped = "Equipped" if item.equipped else ""
                    label = ttk.Label(equipment, text=f"{item.name} : {equiped}", font="Arial 13")
                elif item.consumable:
                    label = ttk.Label(consumables, text=f"{item} : {item.stack}", font="Arial 13")
                elif item.amount: # this is gold
                    continue
                label.pack(anchor="w", padx=5, pady=2, fill="both")
            except AttributeError:
                print("DEBUG: AttributeError in Inventory create_widgets", item, item.amount)

        
        self.item_type_notebook.add(equipment, text="Equipment")
        self.item_type_notebook.add(consumables, text="Consumables")
        self.item_type_notebook.pack(anchor="w", padx=5, pady=5, expand=True, fill="both")

    def update(self, inventory):
        for widget in self.winfo_children():
            widget.destroy()
        self.create_widgets(inventory)


class Combat(ttk.Frame):
    """ Show combataints and their health bars"""
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.app = parent.parent.parent
        self.create_widgets()

    def create_widgets(self):
        label = ttk.Label(self, text="This will be the Combat Tab", font = "Arial 10 ") # create a label
        label.pack()

    def draw_combat(self, enemies, player):
        """ Draws combattants and their health bars"""
        # destroy old widgets
        for widget in self.winfo_children():
            widget.destroy()
        # draw player to the left
        self.columnconfigure((0,1), weight=1)
        self.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        player_label = ttk.Label(self, text=f"{player.name} : {player.health}/{player.max_health}")
        player_label.grid(row=0, column=0, rowspan=6, sticky="nsew", padx=5, pady=5)
        # player_label.pack(anchor="w", padx=5, pady=5, fill="y", expand=True)
        for i, enemy in enumerate(enemies):
            enemy_label = ttk.Label(self, text=f"{enemy.name} : {enemy.health}/{enemy.max_health}")
            enemy_label.grid(row=i, column=1, sticky="nsew", padx=5, pady=5)
            # enemy_label.pack(anchor="e", padx=5, pady=5, fill="y", expand=True)

        self.parent.select(1)
        

class PlayerStats(ttk.Frame):
    """ Show the player stats"""
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.app = parent.parent.parent
        self.stats = ["Health", "Attack", "Spell Attack", "Defense", "Spell Defense", "Initiative"]
        self.player_stats = [self.app.player.health, self.app.player.attack, self.app.player.spell_attack, self.app.player.defense, self.app.player.spell_def, self.app.player.initiative]
        self.player_stats_tk = [tk.StringVar(value=stat) for stat in self.player_stats]
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()

        label = ttk.Label(self, text="Player Stats", font = "Arial 20 ") # create a label
        label.pack()
        # create a table
        table = ttk.Treeview(self, columns=("Stat", "Value"), show="headings")
        table.heading("Stat", text="Stat", anchor="w")
        table.heading("Value", text="Value", anchor="w")
        table.pack()
        # stats = self.app.player.get_stats_as_dict()
        for i, stat in enumerate(self.stats):
            table.insert("", "end", values=(stat, self.player_stats_tk[i].get()))
    
    def update(self):
        for i, stat in enumerate(self.stats):
            self.player_stats_tk[i].set(self.app.player.get_stats_as_dict()[stat])
        self.create_widgets()
            
            
class Info(ttk.Frame):
    """ Show information about items, enemies, etc."""
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.app = parent.parent.parent
        self.create_widgets()

    def create_widgets(self, items=None):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=2)
        if items:
            for i, item in enumerate(items):
                label = ttk.Label(self, text=f"{item.name}", font = "Arial 10 ")
                label.grid(row=i, column=0, sticky="nesw", padx=5, pady=5)
                information = ttk.Label(self, text=f"{item.description}", font = "Arial 10 ")
                information.grid(row=i, column=1, sticky="nesw", padx=5, pady=5 )
        else:
            label = ttk.Label(self, text="This will be the Info Tab", font = "Arial 10 ") # create a label
            label.pack()

    def update_info(self, items):
        for widget in self.winfo_children():
            widget.destroy()
        self.create_widgets(items)


class Log_Frame(ttk.Frame):
    """ Log Frame, will display the log of the game to the player"""
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.app = self.parent
        

        label = ttk.Label(self, text="Log")
        label.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        self.layout_setup()

        # create a text widget to display the log
        self.log = tk.Text(self, wrap="word", padx=5, pady=5)
        self.log.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        # create a timestamp for the log
        self.log_timestamp = tk.Text(self, wrap="word", padx=5, pady=5)
        self.log_timestamp.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

    def layout_setup(self):
        self.rowconfigure(0, weight=1, uniform="group2")
        self.rowconfigure(1, weight=10, uniform="group2")
        self.columnconfigure(0, weight=3, uniform="group2")
        self.columnconfigure(1, weight=1, uniform="group2")
    
    def update_log(self, message):
        if not message:
            return
        self.log.insert("end", f"{message}\n")
        # get hours, minutes and seconds
        now = datetime.datetime.now()

        timestamp = now.strftime("%H:%M:%S")
        if "\n" in message:
            timestamp += "\n"
        self.log_timestamp.insert("end", f"{timestamp}\n")


        self.log.see("end")
        self.log_timestamp.see("end")
        self.log.update()
        self.log_timestamp.update()
