""" Data and weights for random scene and encounter generation. """

import random
import utils

# scenes and weights for random scene generation
places = {
    "Forsaken Chapel": 3,
    "Whispering Alley": 7,
    "Shattered Plaza": 3,
    "Ruined Battlefield": 2,
    "Cursed Well": 4,
    "Collapsed Tower": 2,
    "Desolate Garden": 3,
    "Abandoned Warehouse": 3,
    "Ancient Crypt": 1,
    "Flooded Streets": 4,
    "Ruined Building": 9
}

useful_places = {
    "Training Grounds": 3,
    "Shrine": 1,
    "ruined Wizard's Shop": 3,
    "Sacred Grove": 3,
}

useful_places_not_implemented = {
    "Ancient Library": 2,
    "Healer's Hut": 2,
    "Mystic's Tower": 3,
    "Sacred Grove": 2,
    "Hidden Forge": 1,
    "Alchemist's Lab": 4,
    "Smithy": 3,
    
    "Artifact Collector": 2,
    "Eldritch Archive": 1,
    "Underground Market": 3,
    "Fabled Inn": 5,
    "Hermit's Cave": 2,
    "Teleportation Circle": 1
}

encounter_types = {
    "None": 2,
    "Friendly": 2,
    "Risk & Reward": 3,
    "Basic Combat": 2,
}

encounter_types_not_implemented = {
    "Rescue": 4,
    "Who Gets the Drop?": 4,
    "Catch the Scout": 3,
    "Time Limit": 4,
    "Corpses": 5,
    "Ambush": 2,
    "Lost Relic": 2,
    "Eldritch Anomaly": 3,
    "Forbidden Ritual": 1,
    "A Call for Help": 2
}




