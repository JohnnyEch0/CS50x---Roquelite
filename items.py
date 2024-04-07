# import the consumable effects from data/effects_dat.py
import data.effects_dat as effects_dat

class Item:
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
        return f"{self.name} - {self.description}"
    
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
        # delete the item
        user.inventory.remove(self)
        effect_lookup = effects_dat.consumable_effects[self.name][0]
        amount = effects_dat.consumable_effects[self.name][1]
        effect_lookup(target, amount)
        # print(effect_lookup, amount)
        # use the effect

class Gold(Item):
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
