""" This file contains the functions that print the prompts and options for the player to choose from. 
Used when the GUI is turned off.
"""
from data.input_dicts import exp_keys, combat_keys, combat_keys_extended

def explore_room(objects, entities, unf_mechanic):
    options = []
    prompt = f"What would you like to do? "
    if objects:
        prompt += f"    Objects = {exp_keys[0]}"
        options.append(exp_keys[0])
        
    prompt += f"    Inventory = {exp_keys[1]}"
    options.append(exp_keys[1])
    if unf_mechanic:
        # TODO: Make the Village Start-option different
        prompt += f"   Talk to {entities[0].name} = {exp_keys[-2]}"
        options.append(exp_keys[-2])
    prompt += f"    Move to the next scene = {exp_keys[-1]}"
    options.append(exp_keys[-1])

    return prompt, options

def inv_overview():
    options = [combat_keys[0], combat_keys[1], "Any other key"]
    prompt = "Inventory:    Consumables = Q    Equipment = W    Exit = Any Other Key"

    return prompt, options

def inv_consumables(player):
    options = []
    prompt = "Consumables:  "
    for i, item in enumerate(player.inventory):
        if item.consumable:
            prompt += f"{item.name} = {combat_keys_extended[i]}    "
            options.append(combat_keys_extended[i])
    prompt += f"    Exit = Any other key"
    options.append("Any other key")


    return prompt, options

def village(entities):
    NPC_amt = len(entities)
    options = []
    prompt = "Village:    "
    for i, entity in enumerate(entities):
        prompt += f"Talk to {entity.name} = {combat_keys_extended[i]}    "
        options.append(combat_keys_extended[i])
    
    prompt += f"    Rest = {combat_keys_extended[NPC_amt]}    "
    prompt += f"Access ur inventory = {combat_keys_extended[NPC_amt + 1]}   Move to the next scene = {combat_keys_extended[NPC_amt + 2]}"
    options.extend(combat_keys_extended[NPC_amt:NPC_amt+3])
    
    prompt += f"    Exit = Any other key"
    options.append("Any other key")

    return prompt, options


def item_overview(objects):
    prompt = "Items:    "
    options = []
    for i, item in enumerate(objects):
        prompt += f"{item.name} = {combat_keys_extended[i]}    "
        options.append(combat_keys_extended[i])
    prompt += f"    Exit = Any other key"
    options.append("Any other key")
    return prompt, options