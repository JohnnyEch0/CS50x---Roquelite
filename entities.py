import random

import actions
import utils
from data import moves_dat, items_dat
from dicts import dict_directions, combat_keys
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
                 health,
                 attack,
                 spell_attack,
                 defense=0,
                 spell_def=0,
                 initiative=1,
                 evasion=0,
                 moves=None,
                 alive=True,
                 faction=None,
                 exp_given=20):
        Entity.__init__(self, name, faction)

        self.health = health
        self.attack = attack
        self.spell_attack = spell_attack
        self.defense = defense
        self.spell_def = spell_def
        self.initiative = initiative
        self.evasion = evasion
        if moves is None:
            moves = [actions.Attack(self, **moves_dat.TACKLE_DATA)]
        self.moves = [moves]
        self.alive = alive
        self.exp_given = exp_given
        self.max_health = health
        self.invisible_timer = 0
        self.invisible = False

    def roll_4_initiative(self):
        return random.randint(1, 10) + self.initiative

    def fight(self, entities_enc):
        # TODO better move ai
        roll = random.choice(self.moves)
        roll[0].use(self, entities_enc)

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
                 health,
                 attack,
                 spell_attack,
                 defense,
                 spell_def,
                 initiative,
                 evasion,
                 moves,
                 alive,
                 faction="Heroes"
                 ):
        Fighter.__init__(self,
                         name,
                         health,
                         attack,
                         spell_attack,
                         defense,
                         spell_def,
                         initiative,
                         evasion,
                         moves,
                         alive,
                         faction)
        self.exp = 0
        self.pos = pos
        self.inventory = [items.Gold(100), items.Item(**items_dat.HEALING_POTION), items.Item(**items_dat.DUST_OF_DISAPPEARANCE)]
        self.prev_pos = None

    def fight(self, entities_enc):
        prompt = "Your Turn:    "
        for i, moves in enumerate(self.moves):
            prompt += f"{self.moves[i].name} = {combat_keys[i]}  "
        fight_input = utils.get_input(prompt, combat_keys)

        for i, moves in enumerate(self.moves):
            if fight_input == combat_keys[i]:
                self.moves[i].use(self, entities_enc)
        
        # no longer invisible after attacking
        self.invisible = False

    def move(self, room_mv):
        # this was N, E, S, W
        # we need to get the same from the new system
        directions = room_mv.walkable_tiles
        # print(f"---&debug walkable_tiles @player.move: {directions}")

        passage_input = utils.get_input(f"Where will you go: {directions}?", directions)
        
        self.prev_pos = utils.Vector2(self.pos[0], self.pos[1])
        # print("before move", self.pos[0], self.pos[1], "prev: ", self.prev_pos[0], self.prev_pos[1])

        self.pos += dict_directions[f"{passage_input}"]

        # check if the player is invisible
        if self.invisible:
            self.invisible_timer -= 1
            self.check_invisible()
        
        # print("after move", self.pos[0], self.pos[1], "prev: ", self.prev_pos[0], self.prev_pos[1])
    
    def move_back(self):
        self.pos = self.prev_pos


