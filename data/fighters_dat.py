# Description: Contains the data for the fighters in the game.
PLAYER_START_DATA = {
    "health": 200,
    "attack": 30,
    "spell_attack": 30,
    "defense": 40,
    "spell_def": 30,
    "initiative": 30,
    "evasion": 0,
    "moves": None,
    "alive": True,
    "faction": "Heroes"
}

# goblin data
GOBLIN_DATA = {
    "name": "Goblin",
    "health": 20,
    "attack": 20,
    "spell_attack": 25,
    "defense": 25,
    "spell_def": 15,
    "initiative": 25,
    "evasion": 5,
    "moves": None,
    "faction": "Goblins",
    "exp_given": 20
}

GOBLIN_BRUISER = {
    "name": "Goblin Bruiser",
    "health": 30,
    "attack": 30,
    "spell_attack": 0,
    "defense": 30,
    "spell_def": 10,
    "initiative": 15,
    "evasion": 5,
    "moves": None,
    "faction": "Goblins",
    "exp_given": 30
}

goblins = [
    (GOBLIN_DATA, 10),
    (GOBLIN_BRUISER, 3)
]

