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
    "Smithy": 4,
    "Shrine": 3,
    "Ancient Library": 2,
    "Healer's Hut": 2,
    "Mystic's Tower": 3,
    "Sacred Grove": 2,
    "Hidden Forge": 1,
    "Alchemist's Lab": 4,
    "Training Grounds": 3,
    "Artifact Collector": 2,
    "Eldritch Archive": 1,
    "Underground Market": 3,
    "Fabled Inn": 5,
    "Hermit's Cave": 2,
    "Teleportation Circle": 1
}

encounter_types = {
    "None": 4,
    "Friendly": 20,
    "Rescue": 4,
    "Risk & Reward": 30,
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





def test_scenes_dat():
    random_useful_places = [utils.random_choice(useful_places) for _ in range(5)]
    random_places = [utils.random_choice(places) for _ in range(5)]
    random_encounter_types = [utils.random_choice(encounter_types) for _ in range(5)]

    print(f" places = {random_places}")
    print(f" encounter_types = {random_encounter_types}")
    print(f" useful_places = {random_useful_places}")



