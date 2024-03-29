
KORGRIM = {
    "name": "Korgrim, the Immense",
    "faction": "Giants",
    "money_mod": 50,
    "inventory_mod": 5
}


WARDEN_DRONE = {
    "name": "Warden Drone",
    "faction": "Hive",
    # "description": "Part of the village's hive mind, will offer loot for gold.",
    # "dialogue": "I am a Warden Drone. I am part of the village's hive mind. I will offer you loot for gold.",
    "money_mod": 5,
    "inventory_mod": 3
}

MIRA = {
    "name": "Mira, the Antiquarian",
    "faction": "Adventure Guild",
    "money_mod": 25,
    "inventory_mod": 1
}

npc_traders = [
    (WARDEN_DRONE, 9),
    (MIRA, 3),
    (KORGRIM, 1),  # Very rare, trades in powerful, cursed items.
]