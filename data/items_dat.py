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



# RARE_ITEMS: Items that are very useful.

RING_OF_HEALTH = {
    'name': 'Ring of Health',
    'value': 150,
    'description': 'A ring that increases your health by 10.',
}

SWORD = {
    'name': 'Sword',
    'value': 150,
    'description': 'A sword that increases your attack by 10.',
}

SHIELD = {
    'name': 'Shield',
    'value': 150,
    'description': 'A shield that increases your defense by 10.',
}

WAND = {
    'name': 'Wand',
    'value': 150,
    'description': 'A wand that increases your spell attack by 10.',
}

ROBE = {
    'name': 'Robe',
    'value': 150,
    'description': 'A robe that increases your spell defense by 10.',
}

BOOTS = {
    'name': 'Boots',
    'value': 150,
    'description': 'A pair of boots that increases your initiative by 10.',
}

VICIOUS_KNIFE = {
    'name': 'Vicious Knife',
    'value': 150,
    'description': 'A knife that increases your critical chance by 1.',
}

EVASIVE_CLOAK = {
    'name': 'Evasive Cloak',
    'value': 150,
    'description': 'A cloak that increases your evasion by 5.',
}

uncommon_items = [
    (HEALING_POTION, 3),
    (DUST_OF_DISAPPEARANCE, 2),
]


leveled_items = [
    (RING_OF_HEALTH, 1),
    (SWORD, 1),
    (SHIELD, 1),
    (WAND, 1),
    (ROBE, 1),
    (BOOTS, 1),
    (VICIOUS_KNIFE, 1),
    (EVASIVE_CLOAK, 1),
]

