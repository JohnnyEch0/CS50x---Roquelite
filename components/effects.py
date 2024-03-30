class Effect:
    def __init__(self):
        pass

    def use(self, actor):
        print("{actor} used SWOOSH")

def heal(target, amount):
    target.health = min(target.health + 50, target.max_health)
    print(f"{target.name} healed for {amount} health")

def stealth(actor, duration):
    print(f"{actor.name} is now invisible (not implemented)")
    # make the actor invisible
    # actor.invisible = True
    # set a timer for invisibility
    # actor is invisible for duration moves
    actor.invisible_timer = duration
    actor.check_invisible()
    print(actor.invisible)
    pass