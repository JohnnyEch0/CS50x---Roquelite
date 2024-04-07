import utils, random, printers
from data.input_dicts import exp_keys, combat_keys, combat_keys_extended, dict_directions, direction_names
from items import Item
from data import fighters_dat

class InputHandler:
    def __init__(self, player, level, gui):
        self.player = player
        self.gui = gui # None
        self.notebook_gui = self.gui.main_frame.notebook if self.gui else None
        self.level = level
        

    def room_log(self, room):
        """This function will handle the room printing """
        
        if self.gui:
            self.gui.log_frame.update_log(f"You are in a {room.scene}.")
            #self.gui.main_frame.room_update(room)
        else:
            print(f"You are in a {room.scene}.\n")

    def log(self, message):
        if self.gui:
            self.gui.log_frame.update_log(message)
        else:
            print(message)

    def narrate(self, message):
        if self.gui:
            self.notebook_gui.narration.update_text(message)
        else:
            print(message)
        
    def movement(self, room):
        directions = room.walkable_tiles
        if self.gui:
            gui_options = []
            for direction in directions:
                gui_options.append((direction_names[direction], direction))
            # print("Movement to main window not implemented")
            mov_input = self.gui.input_widget.update(gui_options, type="movement")
        else:
            mov_input = utils.get_input(f"Where will you go: {directions}?", directions)


        self.player.prev_pos = utils.Vector2(self.player.pos[0], self.player.pos[1])

        self.player.pos += dict_directions[f"{mov_input}"]
        self.level.explore_room(self.player.pos[0], self.player.pos[1])

        if self.player.invisible:
            self.player.invisible_timer -= 1
            self.player.check_invisible()


    def exploration(self, objects, entitites, unf_mechanic=None):
        
        # print/gui part of the function
        while True:
            if self.gui:
                self.gui.main_frame.player_metrics_update()
                gui_options = []
                
                # self.gui.
                if objects:
                    gui_options.append(("Objects", exp_keys[0]))
                gui_options.append(("Inventory", exp_keys[1]))
                if unf_mechanic:
                    """ BUG: in the village, the unf mechanic results in a NPC"""
                    gui_options.append((f"Talk to {entitites[0].name}", exp_keys[-2]))
                gui_options.append(("move", exp_keys[-1]))
                input = self.gui.input_widget.update(gui_options)
                print(input)
            else:
                prompt, options = printers.explore_room(objects, entitites, unf_mechanic)
                input = utils.get_input(prompt, options)


            # input handling part of the function
            if input == exp_keys[0]:
                # TODO: Seperate Function.
                objects_selector = self.items_overview(objects)
                if objects_selector:
                    objects.remove(objects_selector)
                    # different route for gold
                    log = objects_selector.pick_up(self.player)
                    self.log(log)
                    self.gui.main_frame.notebook.inventory.update(self.player.inventory)

                # list objects, allow interaction
                # this may be items or structures
                # items can be added to the player inventory
                # structures give Lore or Clues
            elif input == exp_keys[1]:
                #TODO: is this varriable useless?
                inv_selector = self.inventory_overview()
            elif input == exp_keys[-2]:
                print("IH-explo return trigger unf mechanic")
                return 1 # trigger unf mechanic from main
            elif input == exp_keys[-1]:
                return 0 # trigger movement from main


    def items_overview(self, objects):
        """This function will handle the overview of up to 3 items in the room."""
        if self.gui:
            gui_options = []
            for i, item in enumerate(objects):
                gui_options.append((item.name, combat_keys_extended[i]))
            print("Items to main window not implemented")
            input = self.gui.input_widget.update(gui_options)
            options = [item[1] for item in gui_options]
        else:
            prompt, options = printers.items_overview(objects)
            input = utils.get_input(prompt, options)
        
        
        for i, item in enumerate(objects):
            if input == combat_keys[i]:
                return item
        
        return

    """
    Village Handlers
    """

    def village(self, entities):
        """ unfinished, untested """
        if self.gui:
            NPC_amt = len(entities)
            gui_options = []
            for i, entity in enumerate(entities):
                gui_options.append((f"Talk to {entity.name}", combat_keys_extended[i]))
            gui_options.append(("Rest", combat_keys_extended[NPC_amt]))
            gui_options.append(("Inventory", combat_keys_extended[NPC_amt + 1]))
            gui_options.append(("Move", combat_keys_extended[NPC_amt + 2]))
            input = self.gui.input_widget.update(gui_options)
            pass
        else:
            prompt, options = printers.village(entities)
            input = utils.get_input(prompt, options)

        """ input handling part of the function """

        
        for i, entity in enumerate(entities):
            # call dialoquge(entity[i]) OR just call Trade() ?
            if input == combat_keys_extended[i]:
                print(f"you talkt to {entity.name}")
        if input == combat_keys_extended[NPC_amt]:
            # return rest mechanic or rest inout handler
            self.rest()
            print(f"Sleep well")
        elif input == combat_keys_extended[NPC_amt+1]:
            # return training mechanic or rest inout handler
            print(f"Training hard, Level-Up Mechanic not implemented")

        # Inventory
        elif input == combat_keys_extended[NPC_amt+2]:
            self.inventory_overview()

        elif input == combat_keys_extended[NPC_amt+3]:
            # movement
            print(f"Move")



        return 0 # for now we return 0 if smth isnt implemented, so as to move the player

    def rest(self):
        """This function will handle the rest and training mechanic."""
        # depending on how much money the player wants to spend, he can add multipliers to his Exp or Health

        """ Healing mechanic """
        # first 5 gold will heal the player fully
        if self.player.inventory[0].amount < 5 * self.player.level:
            print("You do not have enough gold to rest.")
            return
        else:
            self.player.inventory[0].amount -= 5 * self.player.level
            self.player.health = self.player.max_health
            print(f"{self.player.name} healed fully.")

        """ exp boost mechanic"""
        price_exp_boost = (30 * self.player.level + 50 ) * int((random.randint(1, 30) + 80) / 100)

        if self.player.inventory[0].amount < price_exp_boost:
            print("You do not have enough gold to train.")
            return
        else:
            # prompt player to choose if they want to spend the money
            if self.gui:
                print("Exp boost to main window not implemented")
                gui_options = [("Yes", "Q"), ("No", "W")]
                input = self.gui.input_widget.update(gui_options)
            else:
                prompt = f"Would you like to spend {price_exp_boost} gold to train?    Yes = Q    No = W"
                input = utils.get_input(prompt, ["Q", "W"])

            if input == "Q":
                self.player.inventory[0].amount -= price_exp_boost
                self.player.exp = self.player.exp * 1.5
                print(f"{self.player.name} added 50% exp. New exp: {self.player.exp}")


        """ Levelling Up """
        # TODO: check wether the player has enough exp to level up
        while self.player.exp >= fighters_dat.EXP_THRESHHOLDS[self.player.level]:
            print("You have enough exp to level up.")
            self.level_up()
    

    def level_up(self):
        # get the users old stats
        old_stats = self.player.get_stats_as_dict()
        
        # get input on the how the user wants to spend their free 6 Attribute Points per Level:
        # prompt
        print("What do you want to spend your attribute points on?")
        
        if self.gui:
            print("Attribute points to main window not implemented")
            """ 
            1. Run Gui for stat upgrade 
            2. Return the dict with the new stats
            3. Update the player stats
            """
            self.gui.main_frame.show_level_up()
            stats_upgrade = self.gui.main_frame.level_up.update_stats()
            
            # stats_upgrade = self.gui.main_frame.update_stats()

            self.player.level += 1
            self.player.exp_to_next = fighters_dat.EXP_THRESHHOLDS[self.player.level]
            # update the player_stat dict in fighters_dat accordingly
            for stat in stats_upgrade:
                fighters_dat.player_stat_upgrade[stat] += stats_upgrade[stat]
            
            # update the player stats
            self.player.update_stats(fighters_dat.player_stat_upgrade)

            

            # print the level up info in the gui
            confirm = self.gui.main_frame.level_up.print_level_up_info(old_stats, new_stats=self.player.get_stats_as_dict())
            # confirm = self.gui.main_frame.print_level_up_info(old_stats, new_stats=self.player.get_stats_as_dict())
            if confirm:
                """ Show the player metrics hud - DO this inside of the GUi?"""
                self.gui.main_frame.show_player_metrics_hud()
                return
            
            
        else:
            att_points_spend = 0
            while att_points_spend < 6:
                prompt = ""
                if att_points_spend < 6:
                    available_points = 6 - att_points_spend
                    prompt += f"    You have {available_points} points left."
                prompt += f"    Health = Q    Attack = W    Spell Attack = E    Defense = R    Spell Defense = T    Initiative = Z"

                # get the input
                att_input = utils.get_input(prompt, combat_keys_extended[:6])
                
                amt_input = utils.get_input("How many points do you want to spend?", [str(i+1) for i in range(available_points)])

                if self.update_player_stat_points(att_input, amt_input):
                    att_points_spend += int(amt_input)
            self.player.level += 1
            self.player.exp_to_next = fighters_dat.EXP_THRESHHOLDS[self.player.level]
            self.player.update_stats(fighters_dat.player_stat_upgrade)
            self.print_level_up_info(old_stats)
        

        # update player exp to the next level
        

    def update_player_stat_points(self, att, amt):
        """ This function updates the player stat choices"""
        for i, stat in enumerate(fighters_dat.player_stat_upgrade):
            if att == combat_keys_extended[i]:
                fighters_dat.player_stat_upgrade[stat] += int(amt)
                return True
        return False

    def print_level_up_info(self, old_stats):
        print(f" \n ----Level up! {self.player.name} is now level {self.player.level}.----")
        # print(f"Old Stats: {old_stats}")
        # print(f"New Stats: \n{player.get_stats()}")
        # print stats like old-stat --> new stat
        new_stats = self.player.get_stats_as_dict()
        for stat in new_stats:
            print(f"{stat}: {old_stats[stat]} --> {new_stats[stat]}")



    """
    trade things
    """

    def trading(self, trader):
        """This function will handle the trading mechanic."""

        """ Print/Gui part of the function """
        if self.gui:
            print("Trading to main window not implemented")
            gui_options = [("Buy", combat_keys[0]), ("Sell", combat_keys[1]), ("Talk", combat_keys[2]), ("Exit", combat_keys[-1])]
            input = self.gui.input_widget.update(gui_options)
        else:
            prompt = "Buy = Q    Sell = W   Talk = E    Exit = Any Other Key"
            input = utils.get_input(prompt, combat_keys)

        """ Input handling part of the function """
        if input == combat_keys[0]:
            self.buying(trader)

        elif input == combat_keys[1]:
            self.selling(trader)

        elif input == combat_keys[2]:
            print("Talking not implemented")

        else:
            return

        self.trading(trader)

    def buying(self, trader):
        """This function will handle the buying mechanic."""
        if not trader.inventory:
                print(f"{trader.name} has no items to sell.")
                return

        """ Print/Gui part of the function"""
        if self.gui:
            print("Buying to main window not implemented")
            gui_options = []
            for i, item in enumerate(trader.inventory):
                print(item.name, combat_keys_extended[i])
                gui_options.append((item.name, combat_keys_extended[i]))
            gui_options.append(("Exit", combat_keys_extended[-1]))
            input = self.gui.input_widget.update(gui_options)
            # combat_keys = [item[1] for item in gui_options]
        else:
            prompt = "What would you like to buy?    "
            for i, item in enumerate(trader.inventory):
                prompt += f"{item.name} = {combat_keys[i]}    "
            prompt += f"Exit = {combat_keys[-1]}    "
            input = utils.get_input(prompt, combat_keys)
        
        """ Input handling part of the function """
        if input == combat_keys_extended[-1]:
            return
        else:
            for i, item in enumerate(trader.inventory):
                if input == combat_keys_extended[i]:
                    # check the gold item in the players inventory, if it is enough
                    if self.player.inventory[0].amount >= item.value:
                        self.player.inventory[0].amount -= item.value
                        self.player.inventory.append(item)
                        trader.inventory.remove(item)
                        print(f"{self.player.name} bought {item.name} for {item.value} gold.")
                    else:
                        print(f"{self.player.name} does not have enough gold to buy {item.name}.")
                    break
        self.buying(trader)
        return

    def selling(self, trader):
        """This function will handle the selling mechanic."""
        if not self.player.inventory or len(self.player.inventory) == 1:
            print(f"{self.player.name} has no items to sell.")
            return
        elif trader.money < 1:
            print(f"{trader.name} has no gold to buy items.")
            return
        
        """ Print/Gui part of the function"""
        if self.gui:
            print("Selling to main window not implemented")
            gui_options = []
            for i, item in enumerate(self.player.inventory[1:]):
                gui_options.append((item.name, combat_keys_extended[i]))
            gui_options.append(("Exit", combat_keys_extended[-1]))
            input = self.gui.input_widget.update(gui_options)
            # combat_keys = [item[1] for item in gui_options]
        else:
            prompt = "What would you like to sell?    "
            for i, item in enumerate(self.player.inventory):
                prompt += f"{item.name} = {combat_keys[i]}    "
            prompt += f"Exit = {combat_keys[-1]}    "
            input = utils.get_input(prompt, combat_keys)

        """ Input handling part of the function"""
        if input == combat_keys_extended[-1]:
            return
        else:
            for i, item in enumerate(self.player.inventory[1:]):
                if input == combat_keys_extended[i]:
                    # if the trader has enough gold, the player can sell the item
                    if trader.money >= item.value:
                        self.player.inventory[0].amount += item.value
                        trader.inventory.append(item)
                        self.player.inventory.remove(item)
                        print(f"{self.player.name} sold {item.name} for {item.value} gold.")
                    else:
                        print(f"{trader.name} does not have enough gold to buy {item.name}.")
                    break
        self.selling(trader)
        return

    """
    encounter things
    """

    def risk_reward(self, entities):
        """This function will handle the risk and reward encounter.
        --> allow the player to take a battle with high reward or flee"""

        info = self.risk_reward_info(entities)
        self.narrate(info)

        if self.gui:
            gui_options = [("Fight", combat_keys[0]), ("Flee", combat_keys[1])]
            input = self.gui.input_widget.update(gui_options)
        else:
            prompt = "Risk and Reward:    Fight = Q    Flee = W"
            input = utils.get_input(prompt, combat_keys)
        
        if input == combat_keys[0]:
            return 1
        elif input == combat_keys[1]:
            return 2

    def risk_reward_info(self, entities):
        """This function will handle the risk and reward information"""
        info = "You see: "
        for i, entity in enumerate(entities):
            info += (f"a {entity.name}  ")
            if i > 1:
                info += "and  "
        info += "\n They look dangerous, but have some good loot."
        return info
        

    def combat(self):
        """This function will handle any attack selection."""
        if self.gui:
            print("Combat to main window not implemented")
            gui_options = []
            for i, move in enumerate(self.player.moves):
                gui_options.append((move.name, combat_keys[i]))
            fight_input = self.gui.input_widget.update(gui_options)
        else:
            prompt = "Your Attacks: "
            for i, move in enumerate(self.player.moves):
                prompt += f"{move.name} = {combat_keys[i]}    "
            fight_input = utils.get_input(prompt, combat_keys)

        """ Input handling part of the function """
        for i, move in enumerate(self.player.moves):
            if fight_input == combat_keys[i]:
                return self.player.moves[i]
        pass

    def combat_menu(self):
        """This function will handle the combat menu."""
        if self.gui:
            print("Combat Menu to main window not implemented")
            gui_options = [("Attack", combat_keys[0]), ("Inventory", combat_keys[1]), ("Flee", combat_keys[2]), ("Wait", combat_keys[3])]
            input = self.gui.input_widget.update(gui_options)
        else:
            prompt = "Combat Menu:    Attack = Q    Inventory = W    Flee = E   Wait = R"
            input = utils.get_input(prompt, combat_keys)

        """ Input handling part of the function """
        if input == combat_keys[0]:
            return 1
        elif input == combat_keys[1]:
            print("Inventory in Battle not implemented")
            self.inv_items_consumables()
            
        elif input == combat_keys[2]:
            # return 2 to flee
            return 2
        else:
            return

    def invisible_risk_reward(self, entities, objects_ls=[]):
        """This function will handle the risk and reward encounter for invisible players."""

        self.risk_reward_info(entities)
        if self.gui:
            print("Risk and Reward to main window not implemented")
            gui_options = [("Fight", combat_keys[0]), ("Flee", combat_keys[1]), ("Stay Invisible", combat_keys[2])]
            if objects_ls:
                gui_options.append(("Steal the Loot", combat_keys[3]))
            input = self.gui.input_widget.update(gui_options)
        else:
            prompt = "Risk and Reward:    Fight = Q    Flee = W    Stay Invisible = E "
            # check if there is an item in the entities
            if objects_ls:
                prompt += f"    Steal the Loot = R"#
            input = utils.get_input(prompt, combat_keys)
        
        """ Input handling part of the function"""
        if input == combat_keys[0]:
            # start combat after the player gets a hit in
            return 1
        elif input == combat_keys[1]:
            # return 2 to flee
            return 2
        elif input == combat_keys[2]:
            # return 3 to stay invisible
            return 3
        elif input == combat_keys[3]:
            # return 4 to steal the item
            if objects_ls:
                return 4
            # if there is no item to steal, return 3 to stay invisible
            else:
                print("There is nothing to steal. \n staying invisible.")
                return 3

    def target_selection(self, enemies):
        """This function will handle the target selection for the player."""
        # check if there is only one enemy
        if len(enemies) == 1:
            return enemies[0]
        if self.gui:
            print("Target Selection to main window not implemented")
            gui_options = []
            for i, entity in enumerate(enemies):
                gui_options.append((entity.name, combat_keys_extended[i]))
            input = self.gui.input_widget.update(gui_options)
        else:
            prompt = "Who do you want to target?    "
            for i, entity in enumerate(enemies):
                prompt += f"{entity.name} = {combat_keys_extended[i]}    "
            input = utils.get_input(prompt, combat_keys_extended)
        
        for i, entity in enumerate(enemies):
            if input == combat_keys_extended[i]:
                return enemies[i]
        pass

    def combat_ui(self, enemies, player):
        """This function will handle the combat UI."""
        if self.gui:
            print("Combat UI to main window not implemented")
            self.notebook_gui.combat.draw_combat(enemies, player)
            # self.gui.main_frame.combat_ui.update(player, enemies)
        else:
            pass
    """
    inventory things
    """

    def inventory_overview(self):
        # prompt for selection of consumables or equipment
        # prompt += f"    Gold Total: {player.inventory[0].amount}"
        
        while True:
            # Gui part
            if self.gui:
                inv_options = [("Consumables", combat_keys[0]), 
                            ("Equipment", combat_keys[1]), 
                            ("Exit", combat_keys[-1])
                            ]
                print("Inventory to main window not implemented")
                input = self.gui.input_widget.update(inv_options)
            # Print part
            else:
                prompt, options = printers.inv_overview()
                input = utils.get_input(prompt, options)
            
            # input handling part

            if input == combat_keys[0]:
                self.inv_items_consumables()
            elif input == combat_keys[1]:
                print("Equipment not implemented")
            else:
                return 0
    

    def inv_items_consumables(self):
        if self.gui:
            gui_options = []
            print("Consumables to main window not implemented")
            for i, item in enumerate(self.player.inventory):
                if item.consumable:
                    gui_options.append((item.name, combat_keys_extended[i]))
            input = self.gui.input_widget.update(gui_options)
            options = [item[1] for item in gui_options]
        else:
            prompt, options = printers.inv_consumables(self.player)
            input = utils.get_input(prompt, options)
        
        if input in options:
            for i, item in enumerate(self.player.inventory):
                if input == combat_keys_extended[i]:
                    item.use(self.player, self.player)
                    break
        else:
            return

        # Wether smth was used or not, return to the previous menu
        return
