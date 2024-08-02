""" This module will handle the encounter generation of each room."""

import data.npc_dat as npc_dat
import data.fighters_dat as fighters_dat
from data import items_dat
import items
import utils
import entities
import components.mechanics as mechanics
import random
import components.actions as actions

class Encounter():
    """Every room gets a encounter object, takes a type and a scene, generates entities and mechanics."""
    def __init__(self, type, scene):
        self.type = type
        self.scene = scene
        self.objects_ls = []
        self.entities, self.mechanic = None, None
        self.random_gold()
        self.done = False

    """encounter generation """

    def process_encounter(self, level):
        """ This should route encounter types to the appropriate function."""
        if self.type == "None":
            return [], None
        elif self.type == "Friendly":
            return self.roll_friendly_npc(level)
        elif self.type == "Risk & Reward":
            return self.roll_risk_rew(level)
        elif self.type == "Basic Combat":
            return self.basic_combat(level)
        elif self.type == "village":
            return self.village()
        else:
            return [], None

    def roll_enemies(self, player_level, weight: int):
        """ get random enemies, according to player level, weight is the heaviness of the encounter"""
        key = f"{player_level}, {weight}"
        amount, enemies = fighters_dat.encounter_weights[key]
        entities_ls = []
        for i in range(amount):
            roll = utils.random_choice_list_tuple(enemies)
            entities_ls.append(entities.Fighter(level=player_level, **roll))
        return entities_ls

    def roll_friendly_npc(self, level):
        """Roll for a friendly NPC."""
        entities_ls = []
        roll = utils.random_choice_list_tuple(npc_dat.npc_traders)
        entities_ls.append(entities.Trader(**roll))
        return entities_ls, mechanics.Trade()

    def roll_risk_rew(self, level):
        """Roll for a risk and reward encounter."""
        entities_ls = self.roll_enemies(level, weight=2)
        # items
        roll = utils.random_choice_list_tuple(items_dat.uncommon_items)
        self.objects_ls.append(items.Item(**roll))

        # 5% chance for a leveled item
        if random.randint(1, 100) > 70:
            roll_level_item = roll_leveled_item(level)
            self.objects_ls.append(items.Equipment(**roll_level_item))

        return entities_ls, mechanics.Risk_Reward()
    
    def basic_combat(self, level):
        """Roll for a basic combat encounter."""
        entities_ls = self.roll_enemies(level, weight=1)
        return entities_ls, mechanics.Combat()

    """ Village """

    def village(self):
        """Generate the village scene."""
        """ Static NPC'S """
        entities_ls = []
        entities_ls.append(entities.Trader(**npc_dat.WARDEN_TRADER))

        return entities_ls, mechanics.Village()

    """update"""

    def update(self, level):
        if self.done:
            self.objects_ls = []
            return [], None    
        
        self.entities, self.mechanic = self.process_encounter(level)
        """Tell the game: entities and mechanics of this room."""
        self.process_scene_objects(level)
        return self.entities, self.mechanic

    """misc"""
    def random_gold(self):
        """Randomly generate gold in the room"""
        if random.randint(1, 10) == 1:
            return
        n = int(random.triangular(2, 200))
        self.objects_ls.append(items.Gold(n))

    def process_scene_objects(self, level: int):
        """ Depending on the Scene, populate the room with objects"""
        if self.scene == "Training Grounds":
            object = items.Object("Combat Move Scroll", "A scroll with a combat move on it.", level)
            object.mechanic_argument = [actions.Attack(**move) for move in object.mechanic_argument]
            object.mechanic = mechanics.Move_Learning(object.mechanic_argument)
            
            self.objects_ls.append(object)

        
        elif self.scene == "ruined Wizard's Shop":
            object = items.Object("Spell Scroll", "A scroll that you can learn spell moves from.", level)
            # catch special move types
            for i, move in enumerate(object.mechanic_argument):
                if move["name"] == "Magic Projectiles":
                    object.mechanic_argument[i] = actions.MultiAttack(**move)
                else:
                    object.mechanic_argument[i] = move = actions.Attack(**move)
            object.mechanic = mechanics.Move_Learning(object.mechanic_argument)
            self.objects_ls.append(object)
        
        elif self.scene == "Sacred Grove":
            object = items.Object("Sacred Grove", "A grove that may teach you a boost move", level)
            object.mechanic_argument = [actions.Buff(**move) for move in object.mechanic_argument]
            object.mechanic = mechanics.Move_Learning(object.mechanic_argument)
            self.objects_ls.append(object)

        elif self.scene == "Shrine":
            object = items.Object("Shrine", "A shrine that you can pray to.", level)
            object.mechanic = mechanics.Shrine(object.mechanic_argument[0], object.mechanic_argument[1])
            self.objects_ls.append(object)


def roll_leveled_item(level):
    """Roll for a leveled item."""
    roll = utils.random_choice_list_tuple(items_dat.leveled_items)
    level_mod = int(level/4)

    # lucky find
    if random.randint(1, 100) > 95:
        level_mod += 1

    if level_mod == 2:
        roll["name"] += " II"
        roll["value"] += 150
    elif level_mod == 3:
        roll["name"] += " III"
        roll["value"] += 300
    elif level_mod == 4:
        roll["name"] += " IV"
        roll["value"] += 600
    elif level_mod > 4:
        roll["name"] += " V"
        roll["value"] += 1200
    return roll


