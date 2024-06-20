""" This module contains the functions for the various effects that can be applied to actors. """

import random

def heal(target, amount):
    boost = int(target.max_health * amount / 100)
    target.health += boost
    target.health = min(target.health, target.max_health)
    print(f"{target.name} healed for {boost} health")

def stealth(actor, duration):
    """ BUG: Stealth is buggy right now"""
    print(f"{actor.name} is now invisible (not implemented)")

    actor.invisible_timer = duration
    actor.check_invisible()

def buff(actor, stats: list, amounts: list, chance: int, flat: int = 0, target=None):
    """Used by attacks, boost the actors stat(s) by the given amount(s), chance to do so in percent """
    if random.randint(1, 100) < chance:
        log = ""
        for i, stat in enumerate(stats):
            boost = getattr(actor, stat)
            boost += boost * amounts[i] / 100 
            boost += flat
            setattr(actor, stat, int(boost))
            log += f"{actor.name} buffed {stat} to {boost} !"
            if i == 0 and len(stats) > 1:
                log += "\n"
    else:
        return None
    return log
            
def debuff(actor, stats: list, amounts: list, chance: int, flat: int = 0, target=None):
    """used by attacks, reduce the targets stat(s) by the given amount(s), chance to do so in percent """
    if random.randint(1, 100) < chance:
        log = ""
        for i, stat in enumerate(stats):
            boost = getattr(target, stat)
            boost -= boost * amounts[i] / 100 
            boost -= flat
            setattr(target, stat, int(boost))
            log += f"{target.name} was debuffed: {stat} to {boost} !"
            if i == 0 and len(stats) > 1:
                log += "\n"
    else:
        return None
    return log

def damage_via_health_missing(actor, mod, target):
    """Used by Attacks, Damage the target based on how much health is missing from the actor."""
    damage = int((target.max_health - target.health) * mod / 100)
    target.health -= damage
    return f"{actor.name} used damage_via_health_missing on {target.name} for {damage} damage!"

def secondary_attack(actor, mod, target):
    """ Perform a secondary attack on the target with the given modifier."""
    # TODO: redundant damage calculation
    crit_roll = 2 if random.randint(1, 20) <= actor.crit_chance else 1
    lev_crit = actor.level * crit_roll / 5 + 2
    damage = (lev_crit * actor.attack / target.defense * mod / 50 + 2) * random.randint(85, 100) / 100
    target.health -= damage
    return f"secondary_attack on {target.name} for {damage} damage!"

def stun(actor, chance, target):
    """ Used by moves, may Stun the target with a given chance."""
    # TODO: Test this.
    if random.randint(1, 100) < chance:
        target.stunned = True
        return f"{actor.name} stunned {target.name}!"
    else:
        return None


""" Equipment Effects """

def equip_buff(actor, stats: list, amounts: list, mode: str):
    """ boost the actors stat(s) by the given amount(s) """
    if mode == "equip":
        log = ""
        for i, stat in enumerate(stats):
            boost = actor.stat_upgrades[stat]
            boost += amounts[i]
            actor.stat_upgrades[stat] = boost
            log += f"{actor.name} buffed {stat} to {boost} !"
            if i == 0 and len(stats) > 1:
                log += "\n"
        actor.update_stats()
        return log
    elif mode == "unequip":
        log = ""
        for i, stat in enumerate(stats):
            boost = actor.stat_upgrades[stat]
            boost -= amounts[i]
            actor.stat_upgrades[stat] = boost
            log += f"{actor.name} debuffed {stat} to {boost} !"
            if i == 0 and len(stats) > 1:
                log += "\n"
        actor.update_stats()
        return log
    
def crit_buff(actor, chance, mode):
    """ Buffs crit chance by the given amount."""
    if mode == "equip":
        actor.crit_chance -= chance
        return f"{actor.name} gained {chance} crit chance!"
    elif mode == "unequip":
        actor.crit_chance += chance
        return f"{actor.name} gained {chance} crit chance!"

def ev_buff(actor, amt, mode):
    """ Buffs evasion by the given amount."""
    if mode == "equip":
        actor.evasion += amt
        return f"{actor.name} gained {amt} evasion!"
    elif mode == "unequip":
        actor.evasion -= amt
        return f"{actor.name} lost {amt} evasion!"

