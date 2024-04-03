import utils, random, printers, gui
from data.input_dicts import exp_keys, combat_keys, combat_keys_extended, dict_directions, direction_names
from items import Item
from data import fighters_dat

class InputHandler:
    def __init__(self, player, level):
        self.player = player
        self.gui = gui.App(player, level) # None
        

    def movement(self, room):
        directions = room.walkable_tiles
        if self.gui:
            gui_options = []
            for direction in directions:
                gui_options.append((direction_names[direction], direction))
            print("Movement to main window not implemented")
            mov_input = self.gui.input_widget.update(gui_options)
        else:
            mov_input = utils.get_input(f"Where will you go: {directions}?", directions)


        self.player.prev_pos = utils.Vector2(self.player.pos[0], self.player.pos[1])

        self.player.pos += dict_directions[f"{mov_input}"]

        if self.player.invisible:
            self.player.invisible_timer -= 1
            self.player.check_invisible()


    def exploration(self, objects, entitites, unf_mechanic=None):
        # print/gui part of the function
        while True:
            if self.gui:
                gui_options = []
                """ if we have a gui, describe the room in the main window and give options in the input widget"""
                print("Room to gui not implemented")
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
                    if objects_selector.name == "Gold":
                        objects_selector.pick_up(self.player)
                    else:
                        self.player.inventory.append(objects_selector)
                        print(f"{self.player.name} added {objects_selector.name} to their inventory.")
                print("room-Objects not implemented")
                # list objects, allow interaction
                # this may be items or structures
                # items can be added to the player inventory
                # structures give Lore or Clues
            elif input == exp_keys[1]:
                #TODO: is this varriable useless?
                inv_selector = self.inventory_overview()
                # Moved further inv handeling to inv_overview

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
            self.inventory_overview(self.player)

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
        price_exp_boost = (30 * self.player.level + 50 ) * (random.randint(1, 30) + 80) / 100

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
                print(f"{self.player.name} added 50% exp.")


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
            stats_upgrade = self.gui.main_frame.update_stats()

            self.player.level += 1
            # update the player_stat dict in fighters_dat accordingly
            for stat in stats_upgrade:
                fighters_dat.player_stat_upgrade[stat] += stats_upgrade[stat]
            
            # update the player stats
            self.player.update_stats(fighters_dat.player_stat_upgrade)

            

            # print the level up info in the gui
            confirm = self.gui.main_frame.print_level_up_info(old_stats, new_stats=self.player.get_stats_as_dict())
            if confirm:
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
            self.player.update_stats(fighters_dat.player_stat_upgrade)
            self.print_level_up_info(old_stats)
            
        # execute the level up

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
        prompt = "Buy = Q    Sell = W   Talk = E    Exit = Any Other Key"
        input = utils.get_input(prompt, combat_keys)
        if input == combat_keys[0]:
            buying(trader, self.player)

        elif input == combat_keys[1]:
            selling(trader, self.player)

        elif input == combat_keys[2]:
            print("Talking not implemented")

        else:
            return

        self.trading(trader, self.player)

    def buying(self, trader):
        prompt = "What would you like to buy?    "
        if not trader.inventory:
            print(f"{trader.name} has no items to sell.")
            return
        for i, item in enumerate(trader.inventory):
            prompt += f"{item.name} = {combat_keys[i]}    "
        prompt += f"Exit = {combat_keys[-1]}    "
        input = utils.get_input(prompt, combat_keys)
        if input == combat_keys[-1]:
            return
        else:
            for i, item in enumerate(trader.inventory):
                if input == combat_keys[i]:
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
        if not self.player.inventory:
            print(f"{self.player.name} has no items to sell.")
            return
        prompt = "What would you like to sell?    "
        for i, item in enumerate(self.player.inventory):
            prompt += f"{item.name} = {combat_keys[i]}    "
        prompt += f"Exit = {combat_keys[-1]}    "
        input = utils.get_input(prompt, combat_keys)
        if input == combat_keys[-1]:
            return
        else:
            for i, item in enumerate(self.player.inventory[1:]):
                if input == combat_keys[i]:
                    # if the trader has enough gold, the player can sell the item
                    if trader.money >= item.value:
                        self.player.inventory[0].amount += item.value
                        trader.inventory.append(item)
                        self.player.inventory.remove(item)
                        print(f"{self.player.name} sold {item.name} for {item.value} gold.")
                    break
        self.selling(trader)
        return

    """
    encounter things
    """

    def risk_reward(self, entities):
        """This function will handle the risk and reward encounter.
        --> allow the player to take a battle with high reward or flee"""

        self.risk_reward_info(entities)

        prompt = "Risk and Reward:    Fight = Q    Flee = W"
        input = utils.get_input(prompt, combat_keys)
        if input == combat_keys[0]:
            return 1
        elif input == combat_keys[1]:
            return 2

    def risk_reward_info(self, entities):
        """This function will handle the risk and reward information"""
        info = "You see"
        for i, entity in enumerate(entities):
            info += (f"a {entity.name}  ")
            if i > 2:
                info += "and "
        info += "\n They look dangerous, but have some good loot."
        print(info)


    def combat(self):
        """This function will handle any attack selection."""
        prompt = "Your Attacks: "
        for i, move in enumerate(self.player.moves):
            prompt += f"{move.name} = {combat_keys[i]}    "
        fight_input = utils.get_input(prompt, combat_keys)
        for i, move in enumerate(self.player.moves):
            if fight_input == combat_keys[i]:
                return self.player.moves[i]


        pass

    def combat_menu(self):
        prompt = "Combat Menu:    Attack = Q    Inventory = W    Flee = E   Wait = R"
        input = utils.get_input(prompt, combat_keys)
        if input == combat_keys[0]:
            return 1
        elif input == combat_keys[1]:
            print("Inventory not implemented")
        elif input == combat_keys[2]:
            return 2
        else:
            return

    def invisible_risk_reward(self, entities, objects_ls=[]):
        """This function will handle the risk and reward encounter for invisible players."""

        self.risk_reward_info(entities)


        prompt = "Risk and Reward:    Fight = Q    Flee = W    Stay Invisible = E "
        # check if there is an item in the entities
        if objects_ls:
            prompt += f"    Steal the Loot = R"


        input = utils.get_input(prompt, combat_keys)
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
