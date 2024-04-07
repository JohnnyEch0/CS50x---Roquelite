import random

import utils
from data.input_dicts import combat_keys

""" This module contains the classes for the different actions that can be taken in combat. """

def get_target(entities_enc, fighter):
        """Returns the target of the action. 
        If there is only one enemy, it will return that enemy. 
        Otherwise, it will prompt the player to choose a target.
        NPCs will choose a target at random."""

        enemies = get_enemies(fighter, entities_enc)
        if len(enemies) == 1:
            target = enemies[0]
            return target
        else:
            if fighter.faction == "Heroes":
                prompt = "Target: "
                acc_values = []
                for i, enemy in enumerate(enemies):
                    prompt += f"{enemy.name} ({combat_keys[i]})  "  # Use ASCII codes for letters
                    acc_values.append(combat_keys[i])  # Add letters to acceptable values

                input = utils.get_input(prompt, acc_values)
                target_index = combat_keys.index(input)  # Find index of pressed key
                return enemies[target_index]  # Get enemy at that index  # Convert input to index
            else:
                return random.choice(enemies)

def get_enemies(fighter, entities_enc):
    """Returns a list of all entities in the encounter that are not in the same faction as the fighter."""
    attack_targets = []
    for i in entities_enc:
        if i.faction != fighter.faction:
            attack_targets.append(i)
    return attack_targets


class Action:
    def __init__(self, fighter, name, effect=None, targeted=True, description: str = "A Combat Action"):
        self.fighter = fighter
        self.name = name
        self.effect = effect
        self.targeted = targeted
        self.description = description


class Heal(Action):
    def __init__(self, fighter, name, amount, effect=None):
        Action.__init__(self, fighter, name, effect)
        self.amount = amount

    def use(self, fighter, entities_enc=[], target=None):
        heal_amt = self.amount
        # TODO target = smth from entities_enc
        target = fighter
        target.health += heal_amt
        print(f"{fighter.name} healed {target.name} for {heal_amt}, new HP: {target.health} ")
        if self.effect:
            print("Effect!")


class Attack(Action):
    def __init__(self, fighter, name, damage, accuracy=100, effect=None, type="physical", description: str = None):
        Action.__init__(self, fighter, name, effect=None, description=description)
        self.damage: int = damage
        self.accuracy: int  = accuracy
        self.effect: list = effect
        self.type: str = type

    def use(self, fighter, entities_enc, target=None):

        # check if the fighter is a player or an NPC
        if fighter.faction != "Heroes":
            target = get_target(entities_enc, fighter)

        # miss chance
        if random.randint(1, 100) > self.accuracy - target.evasion:
            return f"{fighter.name} missed {target.name}"
            
        """ Damage calculation """
        damage = self.damage_calc(fighter, target)
        target.health -= damage

        log = f"{fighter.name} hit {target.name} with {self.name} for {damage} dmg!"
        
        if self.effect:
            # print("Effect! nnnnot implemented yet!")
            log_effect = self.effect[0](fighter, *self.effect[1:], target=target)
            if log_effect:
                log += "\n" + log_effect


        return log

        
    
    def damage_calc(self, fighter, target):
        """ THis will calc the damage, Pokemon Style """
        # level and crit
        crit_roll = 2 if random.randint(1, 20) <= fighter.crit_chance else 1
        lev_crit = fighter.level * crit_roll / 5 + 2
        # Move power, Attack and Defense
        if self.type == "physical":
            atk_def = fighter.attack / target.defense
        else:
            atk_def = fighter.spell_attack / target.spell_def

        non_rand = lev_crit * atk_def * self.damage / 50 + 2

        # random modifier
        random_mod = random.randint(85, 100) / 100

        return int(non_rand * random_mod)


class MultiAttack(Attack):
    def __init__(self, fighter, name, damage=18, accuracy=70, effect=None, type="physical", min_hits=2, max_hits=5, description=None):
        Attack.__init__(self, fighter, name, damage, accuracy, effect=None, type="physical", description=description)
        self.min_hits = min_hits
        self.max_hits = max_hits

    def use(self, fighter, entities_enc, target=None):
        # check if the fighter is a player or an NPC
        if fighter.faction != "Heroes":
            target = get_target(entities_enc, fighter)

        # miss chance
        if random.randint(1, 100) > self.accuracy - target.evasion:
            print(f"{fighter.name} missed {target.name}")
            return None
            

        hits = self.roll_hits()
        damage_total = 0
        for i in range(hits):
            

            """ Damage calculation """
            damage = self.damage_calc(fighter, target)
            target.health -= damage
            damage_total += damage

        
        
        if self.effect:
            print("Effect! nnnnot implemented yet!")

        return f"{fighter.name} hit the {target.name} {hits} times for {damage_total} dmg!"

    def roll_hits(self):
        # weighted random roll
        weights = []
        for i in range(self.max_hits-self.min_hits):
            # get progressively higher weights
            weights.insert(0, 1*(i)+1)

        # min weight should be low
        weights.insert(0, 1)
        
        return random.choices(range(self.max_hits-self.min_hits+1), weights=weights)[0] + 2
    

class Buff(Action):
    """ A move that will buff stats by a amount percent."""
    def __init__(self, fighter, name, stats: list, amounts: list = [25, 25] , effect=None, description = None):
        Action.__init__(self, fighter, name, effect=None, targeted=False, description=description)
        self.effect = effect
        self.stats = stats
        self.amounts = amounts

    def use(self, fighter, ini_list=None, target=None, friends=None):
        # buff the stats by 25*amount percent
        log = ""
        for i, stat in enumerate(self.stats):
            boost = getattr(fighter, stat)
            boost += boost * self.amounts[i] / 100
            setattr(fighter, stat, int(boost))
            log += f"{fighter.name} buffed {stat} by {self.amounts[i]} %!"
            if i == 0 and len(self.stats) > 1:
                log += "\n"
            # print(boost, fighter.attack, fighter.defense)

            
        

        return log


class group_buff(Buff):
    """ A move that will buff stats by a amount percent for all friends."""
    def __init__(self, fighter, name, stats: list, amounts: list = [25, 25] , effect=None, description = None):
        Buff.__init__(self, fighter, name, stats, amounts, effect, description)

    def use(self, fighter, entities=None):
        friends = [i for i in entities if i.faction == fighter.faction]
        for friend in friends:
            for i, stat in enumerate(self.stats):
                boost = getattr(friend, stat)
                boost += boost * self.amounts[i] / 100
                setattr(friend, stat, int(boost))
                
                

        return f"{fighter.name} buffed all his friends' atk and ini by 10%!"

    