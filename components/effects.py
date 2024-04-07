import random

class Effect:
    def __init__(self):
        pass

    def use(self, actor):
        print("{actor} used SWOOSH")

def heal(target, amount):
    target.health = min(target.health + amount, target.max_health)
    print(f"{target.name} healed for {amount} health")

def stealth(actor, duration):
    print(f"{actor.name} is now invisible (not implemented)")

    actor.invisible_timer = duration
    actor.check_invisible()
    print(actor.invisible)
    pass


def buff(actor, stats: list, amounts: list, chance: int, flat: int = 0, target=None):
    """ boost the actors stat(s) by the given amount(s), chance to do so in percent """
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
    """ reduce the targets stat(s) by the given amount(s), chance to do so in percent """
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
    """ Damage the target based on how much health is missing from the actor."""
    damage = int((target.max_health - target.health) * mod / 100)
    target.health -= damage
    return f"{actor.name} used damage_via_health_missing on {target.name} for {damage} damage!"

def test_dvhm():
    class Actor:
        def __init__(self, name, health, max_health):
            self.name = name
            self.health = health
            self.max_health = max_health

    actor = Actor("actor", 50, 100)
    target = Actor("target", 20, 100)
    print(damage_via_health_missing(actor, 10, target))
    print(target.health)

