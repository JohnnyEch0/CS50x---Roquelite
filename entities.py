import random

import components.actions as actions
import utils
from data import moves_dat, items_dat, fighters_dat
from data.input_dicts import dict_directions, combat_keys
import items



class Entity:
    def __init__(self, name, faction=None):
        self.name = name
        self.faction = faction

class NPC(Entity):
    def __init__(self, name, faction=None):
        Entity.__init__(self, name, faction)
        self.name = name
        self.faction = faction
        # Additional NPC-specific attributes and initialization code can go here

class Trader(NPC):
    def __init__(self, name, faction=None, money_mod=0, inventory_mod=None):
        NPC.__init__(self, name, faction)
        self.money = self.generate_money(money_mod)
        if inventory_mod is None:
            inventory = []
        else:
            inventory = self.generate_inventory(inventory_mod)
        self.inventory = inventory

    def generate_inventory(self, mod):
        # this is a placeholder for now
        inventory = []
        if mod == 1:
            for i in range(random.randint(1, 3)):
                roll = utils.random_choice_list_tuple(items_dat.trash_items)
                inventory.append(items.Item(**roll))

        if mod == 3:
            for i in range(random.randint(1, 3)):
                roll = utils.random_choice_list_tuple(items_dat.uncommon_items)
                inventory.append(items.Item(**roll))

        if mod == 5:
            # generate 2 to 4 rare items
            for i in range(random.randint(2, 3)):
                roll = utils.random_choice_list_tuple(items_dat.rare_items)
                inventory.append(items.Item(**roll))


        return inventory



    def generate_money(self, mod):
        return random.randint(1, 10) * mod

class Fighter(Entity):
    def __init__(self, name,
                    level,
                    base_health,
                    base_attack,
                    base_spell_attack,
                    base_defense,
                    base_spell_def,
                    base_initiative,
                    moves=None,
                    faction=None,
                    exp_given=20,
                    evasion=0
                 ):
        Entity.__init__(self, name, faction)

        self.level = level
        self.health = self.calculate_health(base_health)
        self.attack = self.calculate_stats(base_attack)
        self.spell_attack = self.calculate_stats(base_spell_attack)
        self.defense = self.calculate_stats(base_defense)
        self.spell_def = self.calculate_stats(base_spell_def)
        self.initiative = self.calculate_stats(base_initiative)
        
        self.evasion = evasion
        self.moves = self.set_moves(moves)

        self.alive = True
        self.exp_given = exp_given
        self.max_health = self.calculate_health(base_health)
        self.invisible_timer = 0
        self.invisible = False
        self.crit_chance = 20 # d20 roll >= will crit

    """ Stats calculation, Level is only set once."""
    
    def calculate_health(self, base_value):
        # this will return the max health according to our level.
        return int((base_value * 2 + 110 ) / 20 * self.level )

    def calculate_stats(self, base_value):
        # this will return a stat based on our level
        return int((base_value * 2 + 5) / 20 * self.level)
    
    def get_stats(self):
        return f"Health: {self.health}/{self.max_health}\nAttack: {self.attack}\nDefense: {self.defense}\nSpell Attack: {self.spell_attack}\nSpell Defense: {self.spell_def}\nInitiative: {self.initiative}\n"
    
    def get_stats_as_dict(self):
        """ Returns the stats as a dictionary, First Letters are capitalized, empty spaces between words."""
        return {
            "Health": f"{self.health}/{self.max_health}",
            "Attack": self.attack,
            "Defense": self.defense,
            "Spell Attack": self.spell_attack,
            "Spell Defense": self.spell_def,
            "Initiative": self.initiative
        }
        
    def set_moves(self, moves=None):
                if moves is None:
                    moves = [actions.Attack(self, **moves_dat.TACKLE_DATA)]
                # self.moves = [moves]

                # if those moves are not of the class Action, we need to convert them
                for i, move in enumerate(moves):
                    if not isinstance(move, actions.Action):
                        # not every move is a attack, so we need to check if it is an attack
                        if "damage" in move:
                            if move["name"] == "Fist Combo":
                                moves[i] = actions.MultiAttack(self, **move)
                            else:
                                moves[i] = actions.Attack(self, **move)
                        elif "stats" in move:
                            # if the spell is called WAR_DRUMS_DATA
                            if move["name"] == "War Drums":
                                moves[i] = actions.group_buff(self, **move)
                            else:
                                moves[i] = actions.Buff(self, **move)
                print(moves)
                return moves
    """ Generic Battle Functions """

    def fight(self, entities_enc):
        # TODO better move ai
        roll = random.choice(self.moves)
        print(f"DEBUG: {self.name} uses {roll}")
        log = roll.use(self, entities_enc)
        return log

    def check_invisible(self):
        if self.invisible_timer > 0:
            self.invisible = True
        else:
            self.invisible = False
        print(self.invisible, "  for  " ,self.invisible_timer)

class Player(Fighter):
    def __init__(self,
                    pos,
                    name,
                    level,

                    base_health,
                    base_attack,
                    base_spell_attack, 
                    base_defense, base_spell_def, 
                    base_initiative,

                    moves,
                    faction="Heroes"
                 ):
        Fighter.__init__(self,
                            name,
                            level,

                            base_health, 
                            base_attack, base_spell_attack, 
                            base_defense, base_spell_def, 
                            base_initiative,

                            moves,
                            faction
                        )
        self.exp = 800
        # exp to next level is the item in the fighters.dat EXP_THRESHHOLDS corresponding to the players level
        self.level = 1
        self.exp_to_next = 300 #set for level 1, IH will update this
        self.pos = pos
        self.inventory = [items.Gold(100), items.Item(**items_dat.HEALING_POTION), items.Item(**items_dat.DUST_OF_DISAPPEARANCE)]
        self.prev_pos = None
        self.base_stats = { "health": base_health, "attack": base_attack, "spell_attack": base_spell_attack, "defense": base_defense, "spell_def": base_spell_def, "initiative": base_initiative }


    """ Player Stats calculation  """

    def calculate_health(self, base_value):
        # we need to take into account the players inputs on level up
        # the level up mechanic shall give us a dictionary 
        return int((base_value * 2 + 110 ) / 20 * self.level ) + fighters_dat.player_stat_upgrade["health"]

    def calculate_stats(self, base_value):
        return int((base_value * 2 + 5) / 20 * self.level) + fighters_dat.player_stat_upgrade["attack"]
    
    def update_stats(self, dict):
        self.max_health = self.calculate_health(self.base_stats["health"]) + dict["health"]
        self.health = self.max_health

        self.attack = self.calculate_stats(self.base_stats["attack"]) + dict["attack"]
        self.spell_attack = self.calculate_stats(self.base_stats["spell_attack"]) + dict["spell_attack"]

        self.defense = self.calculate_stats(self.base_stats["defense"]) + dict["defense"]
        self.spell_def = self.calculate_stats(self.base_stats["spell_def"]) + dict["spell_def"]

        self.initiative = self.calculate_stats(self.base_stats["initiative"]) + dict["initiative"]

    """ Player Battle Functions """

    def fight(self, entities_enc):
        prompt = "Your Turn:    "
        for i, move in enumerate(self.moves):
            # guess self.moves[i] == move here
            prompt += f"{self.moves[i].name} = {combat_keys[i]}  "
        fight_input = utils.get_input(prompt, combat_keys)

        for i, move in enumerate(self.moves):
            if fight_input == combat_keys[i]:
                self.moves[i].use(self, entities_enc)

        # no longer invisible after attacking
        self.invisible = False

    def move_back(self):
        self.pos = self.prev_pos


