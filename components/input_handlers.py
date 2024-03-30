import utils
from dicts import exp_keys, combat_keys, combat_keys_extended
from items import Item

def exploration(objects, player, entitites, unf_mechanic=None):
    # print part of the function
    prompt = f"What would you like to do? "
    if objects:
        prompt += f"    Objects = {exp_keys[0]}"
    prompt += f"    Inventory = {exp_keys[1]}"
    if unf_mechanic:
        prompt += f"   Talk to {entitites[0].name} = {exp_keys[-2]}"
    prompt += f"    Move to the next scene = {exp_keys[-1]}"
    input = utils.get_input(prompt, exp_keys)

    # input handling part of the function
    if input == exp_keys[0]:
        # TODO: Seperate Function.
        objects_selector = items_overview(objects)
        if objects_selector:
            objects.remove(objects_selector)
            # different route for gold
            if objects_selector.name == "Gold":
                objects_selector.pick_up(player)
            else:
                player.inventory.append(objects_selector)
                print(f"{player.name} added {objects_selector.name} to their inventory.")
        print("room-Objects not implemented")
        # list objects, allow interaction
        # this may be items or structures
        # items can be added to the player inventory
        # structures give Lore or Clues
    elif input == exp_keys[1]:
        inv_selector = inventory_overview(player)
        # Moved further inv handeling to inv_overview

    elif input == exp_keys[-2]:
        return 1
    elif input == exp_keys[-1]:
        return 0

    return 0 # for now we return 0 if smth isnt implemented, so as to move the player

def items_overview(objects):
    """This function will handle the overview of up to 3 items in the room."""
    prompt = "Items:    "
    for i, item in enumerate(objects):
        prompt += f"{item} = {combat_keys[i]}    "
    prompt += f"Exit = {combat_keys[-1]}    "
    input = utils.get_input(prompt, combat_keys)
    if input == combat_keys[-1]:
        return
    else:
        for i, item in enumerate(objects):
            if input == combat_keys[i]:
                return item
    return

"""
Village Mechanics
"""
def village(entitites, player):
    # print part of the function
    NPC_amt = len(entitites) # count NPC'S
    options = []
    prompt = f"What would you like to do? "
    if entitites:
        for i, entity in enumerate(entitites):
            # maximum of 5 entitites
            # 3 will always be present
            # but the inkeep and the sensei get seperate options
            prompt += f"    Talk to {entity.name} = {combat_keys_extended[i]}"
            options.append( combat_keys_extended[i] )

    prompt += f"    Rest = {combat_keys_extended[NPC_amt]}
                    Training = {combat_keys_extended[NPC_amt + 1]}
                    Access ur inventory = {combat_keys_extended[NPC_amt + 2]}
                    Move to the next scene = {combat_keys_extended[NPC_amt + 3]}
                "
                    # add 4 additional options
                    # do we need to do these seperately with append??
                    options.append ( combat_keys_extended[:NPC_amt:NPC_amt+3])
    input = utils.get_input(prompt, options)

    # input handling part of the function
    for i in entities:
        # call dialoquge(entity[i]) OR just call Trade() ?
        # dont call this for Training and Rest
        if input == combat_keys_extended[i]:
            print(f"you talkt to {i.name}")
        elif input == combat_keys_extended[NPC_amt]:
            # return rest mechanic or rest inout handler
            print(f"Sleep well")
        elif input == combat_keys_extended[NPC_amt+1]:
            # return training mechanic or rest inout handler
            print(f"Training hard, Level-Up Mechanic not implemented")

        elif input == combat_keys_extended[NPC_amt+2]:
            inventory_overview(player)
            # print(f"Inv")

        elif input == combat_keys_extended[NPC_amt+3]:
            # movement
            print(f"Move")



    return 0 # for now we return 0 if smth isnt implemented, so as to move the player
"""
trade things
"""

def trading(trader, player):
    prompt = "Buy = Q    Sell = W   Talk = E    Exit = Any Other Key"
    input = utils.get_input(prompt, combat_keys)
    if input == combat_keys[0]:
        buying(trader, player)

    elif input == combat_keys[1]:
        selling(trader, player)

    elif input == combat_keys[2]:
        print("Talking not implemented")

    else:
        return

    trading(trader, player)

def buying(trader, player):
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
                if player.inventory[0].amount >= item.value:
                    player.inventory[0].amount -= item.value
                    player.inventory.append(item)
                    trader.inventory.remove(item)
                    print(f"{player.name} bought {item.name} for {item.value} gold.")
                else:
                    print(f"{player.name} does not have enough gold to buy {item.name}.")
                break
    buying(trader, player)
    return

def selling(trader, player):
    if not player.inventory:
        print(f"{player.name} has no items to sell.")
        return
    prompt = "What would you like to sell?    "
    for i, item in enumerate(player.inventory):
        prompt += f"{item.name} = {combat_keys[i]}    "
    prompt += f"Exit = {combat_keys[-1]}    "
    input = utils.get_input(prompt, combat_keys)
    if input == combat_keys[-1]:
        return
    else:
        for i, item in enumerate(player.inventory[1:]):
            if input == combat_keys[i]:
                # if the trader has enough gold, the player can sell the item
                if trader.money >= item.value:
                    player.inventory[0].amount += item.value
                    trader.inventory.append(item)
                    player.inventory.remove(item)
                    print(f"{player.name} sold {item.name} for {item.value} gold.")
                break
    selling(trader, player)
    return

"""
encounter things
"""

def risk_reward(entities, player):
    """This function will handle the risk and reward encounter.
     --> allow the player to take a battle with high reward or flee"""

    risk_reward_info(entities)

    prompt = "Risk and Reward:    Fight = Q    Flee = W"
    input = utils.get_input(prompt, combat_keys)
    if input == combat_keys[0]:
        return 1
    elif input == combat_keys[1]:
        return 2

def risk_reward_info(entities):
    """This function will handle the risk and reward information"""
    info = "You see"
    for i, entity in enumerate(entities):
        info += (f"a {entity.name}  ")
        if i > 2:
            info += "and "
    info += "\n They look dangerous, but have some good loot."
    print(info)


def combat(player):
    """This function will handle any attack selection."""
    prompt = "Your Attacks: "
    for i, move in enumerate(player.moves):
        prompt += f"{move.name} = {combat_keys[i]}    "
    fight_input = utils.get_input(prompt, combat_keys)
    for i, move in enumerate(player.moves):
        if fight_input == combat_keys[i]:
            return player.moves[i]


    pass

def combat_menu(player):
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

def invisible_risk_reward(player, entities, objects_ls=[]):
    """This function will handle the risk and reward encounter for invisible players."""

    risk_reward_info(entities)


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

def inventory_overview(player):
    # prompt for selection of consumables or equipment
    prompt = "Inventory:    Consumables = Q    Equipment = W    Exit = Any Other Key"
    prompt += f"    Gold Total: {player.inventory[0].amount}"
    input = utils.get_input(prompt, combat_keys)
    if input == combat_keys[0]:
        inv_items_consumables(player)
    elif input == combat_keys[1]:
        print("Equipment not implemented")
    else:
        return 0
    return

def inv_items_consumables(player):
    prompt = "Consumables:    "
    options = []
    for i, item in enumerate(player.inventory):
        if item.consumable:
            prompt += f"{item.name} = {combat_keys_extended[i]}    "
            options.append(combat_keys_extended[i])
    prompt += f"Exit = Any other key"
    input = utils.get_input(prompt, combat_keys_extended)
    if input in options:
        for i, item in enumerate(player.inventory):
            if input == combat_keys_extended[i]:
                item.use(player, player)
                break
    else:
        return

    return
