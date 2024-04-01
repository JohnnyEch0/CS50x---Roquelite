""" Description: Contains the data for the fighters in the game. """

""" Player data First """

# Base stats for player, 720 total points
PLAYER_START_DATA = {
    "level": 1,

    "base_health": 120,
    "base_attack": 120,
    "base_spell_attack": 120,
    "base_defense": 120,
    "base_spell_def": 120,
    "base_initiative": 120,

    "moves": None,
    "faction": "Heroes"
}

player_stat_upgrade = {
    "health": 0,
    "attack": 0,
    "spell_attack": 0,
    "defense": 0,
    "spell_def": 0,
    "initiative": 0,
}

# Used D&D 5e's exp thresholds
EXP_THRESHHOLDS = {
    1: 300,
    2: 900,
    3: 2700,
    4: 6500,
    5: 14000,
    6: 23000,
    7: 34000,
    8: 48000,
    9: 64000,
    10: 85000,
    11: 100000,
    12: 120000,
    13: 140000, 
    14: 165000,
    15: 195000,
    16: 225000,
    17: 265000,
    18: 305000,
    19: 305000,
}

""" Enemy data """


""" Goblins """

# goblin data
GOBLIN_DATA = {
    "name": "Goblin",
    "base_health": 60, 
    "base_attack": 60, "base_spell_attack": 20,
    "base_defense": 40, "base_spell_def": 20,
    "base_initiative": 80,
    "evasion": 5,
    "moves": None,
    "faction": "Goblins",
    "exp_given": 100
}

GOBLIN_BRUISER_DATA = {
    "name": "Goblin Bruiser",
    "base_health": 100, 
    "base_attack": 70, "base_spell_attack": 0,
    "base_defense": 50, "base_spell_def": 20,
    "base_initiative": 40,
    "evasion": 5,
    "moves": None,
    "faction": "Goblins",
    "exp_given": 150
}

GOBLIN_WAR_DRUMMER_DATA = {
    "name": "Goblin War Drummer",
    "base_health": 60, 
    "base_attack": 40, "base_spell_attack": 40,
    "base_defense": 40, "base_spell_def": 40,
    "base_initiative": 60,
    "evasion": 5,
    "moves": None,
    "faction": "Goblins",
    "exp_given": 150
}

goblins = [
    (GOBLIN_DATA, 10)
    # , (GOBLIN_BRUISER, 3)
]

