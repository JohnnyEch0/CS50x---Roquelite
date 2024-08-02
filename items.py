""" This module contains the classes for items and objects in the game world. Items are objects that can be picked up and used by the player. Objects are interactable objects in the game world that cannot be picked up. """

import data.effects_dat as effects_dat
import random
import utils
import data.moves_dat as moves_dat

class Item:
    """ The base class for all items in the game. Items can be picked up and/or used by the player."""
    def __init__(self, name, value, description, consumable=False, stackable=False, equippable=False):
        self.name = name
        self.value = value
        self.description = description
        self.equipped = False
        self.consumable = consumable
        self.stackable = stackable
        self.stack = 1
        self.equippable = equippable

    
    # we can use this for logging
    def __str__(self):
        log = f"{self.name}"
        if self.stackable and self.stack > 1:
            log += f" x{  self.stack}"
        return log
    
    def pick_up(self, player):
        """ adds self to the players inventory, returns log message"""
        # check if the item is stackable
        if self.stackable:
            # check if the player has the item in their inventory
            for item in player.inventory:
                if item.name == self.name:
                    item.stack += 1
                    # print(f"You picked up {self.name}. You now have {item.stack} {self.name}s.")
                    log = f"You picked up {self.name}. You now have {item.stack} {self.name}s."
                    return log
            # if the player does not have the item in their inventory
            player.inventory.append(self)
            log = f"You picked up {self.name}."
        else:
            player.inventory.append(self)
            log = f"You picked up {self}."
        return log

    
    def use(self, user, target):
        if self.consumable:
            self.consume(user, target)
        else:
            # unconsumable but usable item
            pass
    
    def consume(self, user, target):
        if self.stackable and self.stack > 1:
            self.stack -= 1
        else:
            user.inventory.remove(self)
        effect_lookup = effects_dat.consumable_effects[self.name][0]
        amount = effects_dat.consumable_effects[self.name][1]
        effect_lookup(target, amount)
        

class Gold(Item):
    """ A subclass of Item that represents a stack of gold coins."""
    def __init__(self, amount):
        self.amount = amount
        super().__init__("Gold", amount, "A shiny gold coin.")
    
    def pick_up(self, player):
        print(f"You picked up {self.amount} gold.")
        player.inventory[0].amount += self.amount
        log = f"You picked up {self.amount} gold."
        return log
    
    def __str__(self):
        return f"{self.amount} Gold Pieces"

class Equipment(Item):
    """ A subclass of Item that represents an equippable item."""
    def __init__(self, name, value, description, consumable=False, stackable=False, equippable=True):
        super().__init__(name, value, description, consumable, stackable, equippable)
        self.equipped = False
        self.effect = effects_dat.equippable_effects[self.name][0]
        self.effect_args = effects_dat.equippable_effects[self.name][1:]
    
    def equip(self, player):
        if self.equipped:
            log = self.unequip(player)
            if self.effect:
                log += self.effect(player, *self.effect_args, mode="unequip")
        else:
            self.equipped = True
            print(self.effect_args)
            if len(player.equipment) <= 2:
                player.equipment.append(self)
                log = f"You equipped {self.name}."
                if self.effect:
                    log += self.effect(player, *self.effect_args, mode="equip")
            else:
                log = "You can only equip 3 items at once."
        return log
    
    def unequip(self, player):
        if self.equipped:
            self.equipped = False
            player.equipment.remove(self)
            log = f"You unequipped {self.name}."
        else:
            log = (f"You do not have {self.name} equipped.")
        return log
    
    def use(self, user, target):
        self.equip(user)

class Object:
    """ A class for objects in the game world that cannot be picked up."""
    def __init__(self, name, description, level:int ):
        """ Objects cannot be picked up, they are interactable objects in the game world"""
        self.name = name
        self.mechanic_argument = self.process_name(level)
        self.description = description
    
    def __str__(self):
        return f"{self.name} - {self.description}"
    
    def process_name(self, level:int):
        if self.name == "Combat Move Scroll":
            # create a random list of moves
            moves = []
            for i in range(2):
                # roll for the tier
                tier_roll = roll_move_tier(level)
                # roll for the move
                move = utils.random_choice_list_tuple(moves_dat.phys_attacks_tiers[tier_roll])
                moves.append(move)   
            return moves
        elif self.name == "Spell Scroll":
            moves = []
            for i in range(2):
                tier_roll = roll_move_tier(level)
                move = utils.random_choice_list_tuple(moves_dat.spell_attack_tiers[tier_roll])
                moves.append(move)
            return moves
        elif self.name == "Sacred Grove":
            moves = []
            for i in range(2):
                tier_roll = roll_move_tier(level)
                move = utils.random_choice_list_tuple(moves_dat.buff_tiers[tier_roll])
                moves.append(move)
            return moves
        elif self.name == "Shrine":
            return shrine_roll(level)

    
def roll_move_tier(level:int):
    tier_roll = random.randint(1, 100)
    tier_distribution = moves_dat.move_tier_by_level_distribution[level]

    for i in range(len(tier_distribution)):
        if tier_roll <= sum(tier_distribution[:i+1]):
            return i
        
def shrine_roll(level:int):
    roll = random.randint(1, 100)
    stat = random.choice(["health", "attack", "defense", "spell_attack", "spell_def", "initiative"])
    level_mod = int(level/3 + 1)
    if roll <= 10:
        mod = -2
    elif roll <= 25:
        mod = -1
    elif roll <= 60:
        mod = 1
    elif roll <= 85:
        mod = 2
    elif roll <= 100:
        mod = 3
    return (stat, mod*level_mod)

