import random

import utils
from dicts import combat_keys

# Targetting System

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
    def __init__(self, fighter, name, effect=None):
        self.fighter = fighter
        self.name = name
        self.effect = effect

    


class Heal(Action):
    def __init__(self, fighter, name, amount, effect=None):
        Action.__init__(self, fighter, name, effect=None)
        self.roll = amount
        self.effect = effect

    def use(self, fighter, entities_enc):
        # TODO different mod then the damage_mod
        heal_amt = fighter.spell_attack
        # TODO target = smth from entities_enc
        target = fighter
        target.health += heal_amt
        print(f"{fighter.name} healed {target.name} for {heal_amt}, new HP: {target.health} ")
        if self.effect:
            print("Effect!")


class Attack(Action):
    def __init__(self, fighter, name, damage, accuracy=100, effect=None):
        Action.__init__(self, fighter, name, effect=None)
        self.damage = damage
        self.accuracy = accuracy
        self.effect = effect

    def use(self, fighter, entities_enc):
        target = get_target(entities_enc, fighter)

        # miss chance
        if random.randint(1, 100) > self.accuracy - target.evasion:
            print(
                f"{fighter.name} missed {target.name}")

        random_mod = random.randint(60, 100) / 100
        damage = int(fighter.attack + self.damage - target.defense * random_mod)

        target.health -= damage
        print(
            f"{fighter.name} hit {target.name} for {damage} dmg, it is at {target.health} HP")
        if self.effect:
            print("Effect! nnnnot implemented yet!")
            # self.effect.use(fighter, entities_enc)
