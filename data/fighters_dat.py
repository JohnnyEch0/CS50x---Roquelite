from data import moves_dat

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
    # total stats: 720
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
    # total stats: 260 (exluding spell_attack)
}

GOBLIN_BRUISER_DATA = {
    "name": "Goblin Bruiser",
    "base_health": 100, 
    "base_attack": 70, "base_spell_attack": 0,
    "base_defense": 50, "base_spell_def": 20,
    "base_initiative": 40,
    "evasion": 5,
    "moves": [moves_dat.FIST_COMBO_DATA, moves_dat.BULK_UP_DATA],
    "faction": "Goblins",
    "exp_given": 150
    # total stats: 280
}

GOBLIN_WAR_DRUMMER_DATA = {
    "name": "Goblin War Drummer",
    "base_health": 60, 
    "base_attack": 40, "base_spell_attack": 40,
    "base_defense": 40, "base_spell_def": 40,
    "base_initiative": 60,
    "evasion": 5,
    "moves": [moves_dat.WAR_DRUMS_DATA, moves_dat.FIREBOLT_DATA],
    "faction": "Goblins",
    "exp_given": 150
}

goblins = [
    (GOBLIN_DATA, 10), 
    (GOBLIN_BRUISER_DATA, 3),
    (GOBLIN_WAR_DRUMMER_DATA, 4)
]

""" Tier 2 Enemies """
DELIRIOUS_MAW_DATA = {
    "name": "Delirious Maw",
    "base_health": 80, 
    "base_attack": 80, "base_spell_attack": 0,
    "base_defense": 50, "base_spell_def": 50,
    "base_initiative": 50,
    "evasion": 0,
    "moves": [moves_dat.SLOW_SPIT_DATA, moves_dat.BIOLOGICAL_ARTILLERY_DATA],
    "faction": "Aberrations",
    "exp_given": 300
    # total stats: 310
}

GIANT_BLADE_BUG_DATA = {
    "name": "Giant Blade Bug",
    "base_health": 100,
    "base_attack": 100, "base_spell_attack": 0,
    "base_defense": 100, "base_spell_def": 60,
    "base_initiative": 70,
    "evasion": 0,
    "moves": [moves_dat.FEINT_DATA, moves_dat.CONSUME_THE_WEAK_DATA],
    "faction": "Aberrations",
    "exp_given": 300
    # total stats: 430
}

LESSER_EYE_DATA = {
    "name": "Eye Monster",
    "base_health": 80,
    "base_attack": 60, "base_spell_attack": 100,
    "base_defense": 60, "base_spell_def": 70,
    "base_initiative": 90,
    "evasion": 0,
    "moves": [moves_dat.MENTAL_SPEAR_DATA, moves_dat.INNER_FOCUS_DATA],
    "faction": "Aberrations",
    "exp_given": 300
    # total stats: 460
}

aberrations = [
    (DELIRIOUS_MAW_DATA, 6),
    (GIANT_BLADE_BUG_DATA, 3),
    (LESSER_EYE_DATA, 2)
]

""" Tier 3 Enemies """


""" Overviews """
# we need to pick an enemy Tier depending on player level and encounter weight7
""" the first value of the key is the player level, the second is the encounter weight"""
encounter_weights = {
    "1, 1": (1, goblins),
    "1, 2": (2, goblins),
    "2, 1": (2, goblins),
    "2, 2": (3, goblins),
    "3, 1": (4, goblins),
    "3, 2": (2, aberrations),
    "4, 1": (3, aberrations),
    "4, 2": (4, aberrations),

}

enemy_tiers = (goblins, aberrations, "tier3", "tier4", "tier5")