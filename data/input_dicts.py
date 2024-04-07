from utils import Vector2

dict_directions = {
    "W": Vector2(-1, 0),
    "D": Vector2(0, 1),
    "S": Vector2(1, 0),
    "A": Vector2(0, -1)
}


combat_keys = ["Q", "W", "E", "R"]
exp_keys = ["A", "S", "D", "F"]

combat_keys_extended = ["Q", "W", "E", "R", "T", "Z", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"]

# print(combat_keys_extended[:7])

direction_names = {
    "W": "North",
    "D": "East",
    "S": "South",
    "A": "West"
}

direction_placements = {
    "W": (0, 1),
    "D": (1, 2),
    "S": (2, 1),
    "A": (1, 0)
}