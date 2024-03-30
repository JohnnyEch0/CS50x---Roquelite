import data.npc_dat as npc_dat
import data.fighters_dat as fighters_dat
from data import items_dat
import items
import utils
import entities
import components.mechanics as mechanics
import random

class Encounter():
    """This class will handle the encounter handling of each room."""
    def __init__(self, type):
        self.type = type
        self.objects_ls = []
        self.entities, self.mechanic = self.process_encounter()
        self.random_gold()

    """encounter generation """

    def process_encounter(self):
        """ This should route encounter types to the appropriate function."""
        if self.type == "None":
            return [], None
        elif self.type == "Friendly":
            return self.roll_friendly_npc()
        elif self.type == "Risk & Reward":
            return self.roll_risk_rew()
        elif self.type == "Village":
            # generate Village scene
            # maybe this should be called every time we get into the hub
            # rn this is getting called by the room, when it is generated
            return self.village()
            pass
        else:
            return [], None

    def roll_friendly_npc(self):
        """Roll for a friendly NPC."""

        entities_ls = []
        # rn this is only traders
        roll = utils.random_choice_list_tuple(npc_dat.npc_traders)
        # print(roll)
        entities_ls.append(entities.Trader(**roll))
        return entities_ls, mechanics.Trade()

    def roll_risk_rew(self):
        """Roll for a risk and reward encounter."""
        entities_ls = []
        for i in range(random.randint(2, 4)):
            roll = utils.random_choice_list_tuple(fighters_dat.goblins)
            entities_ls.append(entities.Fighter(**roll))

        roll = utils.random_choice_list_tuple(items_dat.uncommon_items)
        self.objects_ls.append(items.Item(**roll))

        return entities_ls, mechanics.Risk_Reward()

    """ Village """
    def village(self):
        """Generate the village scene."""
        """ Static NPC'S """
        entities_ls = []
        entities_ls.append(entities.Trader(**npc_dat.WARDEN_TRADER))
        entities_ls.append(entities.Trader(**npc_dat.WARDEN_INNKEEPER))
        entities_ls.append(entities.Trader(**npc_dat.WARDEN_SENSEI))
        
        """ ´Sometimes there should be a fourth NPC"""
        # TODO

        return entities_ls, mechanics.Village()

    """update"""

    def update(self):
        """Tell the game: entities and mechanics of this room."""
        return self.entities, self.mechanic

    """misc"""
    def random_gold(self):
        """Randomly generate gold in the room"""
        if random.randint(1, 10) > 7:
            return
        n = int(random.triangular(2, 200))
        self.objects_ls.append(items.Gold(n))



# enc = Encounter("Friendly")
