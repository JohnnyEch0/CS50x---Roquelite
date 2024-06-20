""" Data file for effects."""
import components.effects as effects

consumable_effects = {
    'Healing Potion': [effects.heal, 50],
    'Dust of Disappearance': [effects.stealth, 5]
}

equippable_effects = {
    "Ring of Health": [effects.equip_buff, ['health'], [10]],
    'Sword': [effects.equip_buff, ['attack'], [10]],
    'Shield': [effects.equip_buff, ['defense'], [10]],
    "Wand": [effects.equip_buff, ['spell_attack'], [10]],
    "Robe": [effects.equip_buff, ['spell_def'], [10]],
    "Boots": [effects.equip_buff, ['initiative'], [10]],
    "Vicious Knife": [effects.crit_buff, 1],
    "Evasive Cloak": [effects.ev_buff, 5],

    "Ring of Health II": [effects.equip_buff, ['health'], [20]],
    'Sword II': [effects.equip_buff, ['attack'], [20]],
    'Shield II': [effects.equip_buff, ['defense'], [20]],
    "Wand II": [effects.equip_buff, ['spell_attack'], [20]],
    "Robe II": [effects.equip_buff, ['spell_defense'], [20]],
    "Boots II": [effects.equip_buff, ['initiative'], [20]],
    "Vicious Knife II": [effects.crit_buff, 2],
    "Evasive Cloak II": [effects.ev_buff, 10],

    "Ring of Health III": [effects.equip_buff, ['health'], [30]],
    'Sword III': [effects.equip_buff, ['attack'], [30]],
    'Shield III': [effects.equip_buff, ['defense'], [30]],
    "Wand III": [effects.equip_buff, ['spell_attack'], [30]],
    "Robe III": [effects.equip_buff, ['spell_defense'], [30]],
    "Boots III": [effects.equip_buff, ['initiative'], [30]],
    "Vicious Knife III": [effects.crit_buff, 3],
    "Evasive Cloak III": [effects.ev_buff, 15],

    "Ring of Health IV": [effects.equip_buff, ['health'], [40]],
    'Sword IV': [effects.equip_buff, ['attack'], [40]],
    'Shield IV': [effects.equip_buff, ['defense'], [40]],
    "Wand IV": [effects.equip_buff, ['spell_attack'], [40]],
    "Robe IV": [effects.equip_buff, ['spell_defense'], [40]],
    "Boots IV": [effects.equip_buff, ['initiative'], [40]],
    "Vicious Knife IV": [effects.crit_buff, 4],
    "Evasive Cloak IV": [effects.ev_buff, 20],

    "Ring of Health V": [effects.equip_buff, ['health'], [50]],
    'Sword V': [effects.equip_buff, ['attack'], [50]],
    'Shield V': [effects.equip_buff, ['defense'], [50]],
    "Wand V": [effects.equip_buff, ['spell_attack'], [50]],
    "Robe V": [effects.equip_buff, ['spell_defense'], [50]],
    "Boots V": [effects.equip_buff, ['initiative'], [50]],
    "Vicious Knife V": [effects.crit_buff, 5],
    "Evasive Cloak V": [effects.ev_buff, 25],
}