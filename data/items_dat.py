# import components/effects


# Description: Contains data for items in the game.
# TRASH_ITEMS: Items that are not very useful.

BONE = {
    'name': 'Bone',
    'value': 1,
    'description': 'A bone. Not very useful.',
}

STICK = {
    'name': 'Stick',
    'value': 1,
    'description': 'A stick. Not very useful.',
}

STONE = {
    'name': 'Stone',
    'value': 1,
    'description': 'A stone. Not very useful.',
}

trash_items = [
    (BONE, 1),
    (STICK, 3),
    (STONE, 1),
]
# COMMON_ITEMS: Items that are somewhat useful.

# UNCOMMON_ITEMS: Items that are useful.
HEALING_POTION = {
    'name': 'Healing Potion',
    'value': 50,
    'description': 'A potion that heals 50 HP.',
    'consumable': True,
    'stackable': True
}

DUST_OF_DISAPPEARANCE = {
        'name': 'Dust of Disappearance',
        'value': 200,
        'description': 'A small pouch of sparkling dust. Will let you avoid enemies in the next 5 scenes.',
        'consumable': True,
        'stackable': False
    }

uncommon_items = [
    (HEALING_POTION, 3),
    (DUST_OF_DISAPPEARANCE, 1),
]

# RARE_ITEMS: Items that are very useful.

INFERNAL_DAGGER = {
    'name': 'Infernal Dagger',
    'value': 500,
    'description': 'A dagger that is always warm to the touch.'
}

rare_items = [
    (INFERNAL_DAGGER, 1)
]

