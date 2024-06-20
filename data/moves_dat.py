import components.effects as effects


move_tier_by_level_distribution = {
    1: [80, 20],
    2: [60, 40],
    3: [40, 50, 10],
    4: [25, 55, 20],
    5: [0, 60, 30 , 10],
    6: [0, 45, 40, 15],
    7: [0, 30, 50, 20],
    8: [0, 20, 60, 20],
    9: [0, 10, 65, 20, 5],
    10: [0, 0, 60, 30, 10],
    11: [0, 0, 50, 40, 10],
    12: [0, 0, 40, 50, 10],
    13: [0, 0, 30, 55, 15],
    14: [0, 0, 20, 60, 20],
    15: [0, 0, 10, 65, 25],
    16: [0, 0, 0, 60, 40],
    17: [0, 0, 0, 50, 50],
    18: [0, 0, 0, 40, 60],
    19: [0, 0, 0, 30, 70],
    20: [0, 0, 0, 20, 80],
}

TACKLE_DATA = {
    "name": "Tackle",
    "damage": 40,
    "description": "Tackle is a basic attack."
}

ADRENALINE_PUNCH_DATA = {
    "name": "Adrenaline Punch",
    "damage": 30,
    "accuracy": 90,
    "effect": [effects.buff, ["attack"], [25], 10],
    "type": "physical",
    "description": " a weak attack that, in 10 percent of the cases, raises the user's attack by 25."
}

""" TEST THIS ONE"""
DOUBLE_STRIKE_DATA = {
    "name": "Double Strike",
    "damage": 30,
    "accuracy": 90,
    "effect": [effects.secondary_attack, 15],
    "type": "physical",
    "description": "a weak attack that hits twice."
}

HIT_AND_RUN_DATA = {
    "name": "Hit and Run",
    "damage": 30,
    "accuracy": 95,
    "effect": [effects.buff, ["initiative"], [25], 10],
    "type": "physical",
    "description": " a weak attack that, in 10 percent of the cases, raises the user's initiative by 25."
}

SMACK_DATA = {
    "name": "Smack",
    "damage": 50,
    "accuracy": 80,
    "effect": [effects.debuff, ["defense"], [25], 10],
    "type": "physical",
    "description": " a weak attack that, in 10 percent of the cases, lowers the target's defense by 25."
}

phys_attacks_tier_1 = [
    (ADRENALINE_PUNCH_DATA, 1),
    (DOUBLE_STRIKE_DATA, 1),
    (HIT_AND_RUN_DATA, 1),
    (SMACK_DATA, 1),
]


FIST_COMBO_DATA = {
    "name": "Fist Combo",
    "damage": 18,
    "description": "Attack 2-5 times"
}

FEINT_DATA = {
    "name": "Feint",
    "damage": 20,
    "accuracy": 90,
    "effect": [effects.buff, ["evasion"], [10], 30, 10],
    "type": "physical",
    "description": " a weak attack that, in 30 percent of the cases, raises the user's evasion by 10."
}

PUNCH_DATA = {
    "name": "Punch",
    "damage": 60,
    "accuracy": 100,
    "description": " a reliable and strong attack."
}

BREAK_DATA = {
    "name": "Break",
    "damage": 80,
    "accuracy": 80,
    "description": " a strong attack"
}

phys_attacks_tier_2 = [
    (FEINT_DATA, 1),
    (FIST_COMBO_DATA, 1),
    (PUNCH_DATA, 1),
    (BREAK_DATA, 1),
]


WHERE_IT_HURTS_DATA: dict = {
    "name": "Where it hurts!",
    "damage": 80,
    "accuracy": 100,
    "description": "a really strong and precise attack"
}

EXPLOIT_WEAKNESS_DATA: dict = {
    "name": "Exploit Weakness",
    "damage": 60,
    "accuracy": 90,
    "effect": [effects.damage_via_health_missing, 10],
    "description": "a good attack that deals 10 percent of the target's missing health as damage."
}

SHATTERING_STRIKE_DATA: dict = {
    "name": "Shattering Strike",
    "damage": 70,
    "accuracy": 90,
    "effect": [effects.debuff, ["defense"], [25], 30],
    "description": "a good attack that, in 30 percent of the cases, lowers the target's defense by 25."
}

phys_attacks_tier_3 = [
    (WHERE_IT_HURTS_DATA, 1),
    (EXPLOIT_WEAKNESS_DATA, 1),
    (SHATTERING_STRIKE_DATA, 1),
]

KNOCKOUT_DATA: dict = {
    "name": "Knockout",
    "damage": 80,
    "accuracy": 80,
    "effect": [effects.stun, 25],
    "description": "a strong attack that, in 25 percent of the cases, stuns the target."
}

HEAVY_PUNCH_DATA = {
    "name": "Punch",
    "damage": 90,
    "accuracy": 100,
    "description": " a reliable and strong attack."
}

phys_attacks_tier_4 = [
    (KNOCKOUT_DATA, 1),
    (HEAVY_PUNCH_DATA, 1),
]

ARMOR_BREAKER_DATA: dict = {
    "name": "Armor Breaker",
    "damage": 80,
    "accuracy": 80,
    "effect": [effects.debuff, ["defense"], [50], 20],
    "description": "a strong attack that, in 20 percent of the cases, lowers the target's defense by 50%"
}

UPPERCUT_DATA: dict = {
    "name": "Uppercut",
    "damage": 100,
    "accuracy": 95,
    "description": "a really strong and precise attack"
}
phys_attacks_tier_5 = [
    (ARMOR_BREAKER_DATA, 1),
    (UPPERCUT_DATA, 1),
]



phys_attacks_tiers = [phys_attacks_tier_1, phys_attacks_tier_2, phys_attacks_tier_3, phys_attacks_tier_4, "phys_attacks_tier_5"]



SLOW_SPIT_DATA = {
    "name": "Spit",
    "damage": 40,
    "accuracy": 90,
    "effect": [effects.debuff, ["initiative"], [25], 30],
    "type": "physical",
    "description": "Spit is a weak attack that, in 30 percent of the cases, lowers the target's initiative by 25."
}

BIOLOGICAL_ARTILLERY_DATA = {
    "name": "Biological Artillery",
    "damage": 60,
    "accuracy": 90,
    "effect": [effects.debuff, ["defense"], [25], 30],
    "type": "physical",
    "description": "Biological Artillery is a good attack that, in 30 percent of the cases, lowers the target's defense by 25."
}

CONSUME_THE_WEAK_DATA = {
    "name": "Consume the Weak",
    "damage": 60,
    "accuracy": 90,
    "effect": [effects.damage_via_health_missing, 10],
    "type": "physical",
    "description": "Consume the Weak is a good attack that deals 10 percent of the target's missing health as damage."
}



""" Special Attacks """
MAGICAL_FINGER_PISTOL_DATA = {
    "name": "Finger Pistol",
    "damage": 40,
    "accuracy": 100,
    "type": "special",
    "description": "Magical Finger Pistol is a basic spell."
}

FIREBOLT_DATA: dict = {
    "name": "Firebolt",
    "damage": 60,
    "accuracy": 90,
    "type": "special",
    "description": "Firebolt is a good spell used by goblin mages."
}

MENTAL_DAGGER_DATA: dict = {
    "name": "Mental Spear",
    "damage": 40,
    "accuracy": 90,
    "effect": [effects.buff, ["spell_attack"], [25], 10],
    "type": "special",
    "description": "Mental Spear is a powerful spell that, in 10 percent of the cases, raises the user's spell attack by 25 percent."
}


spell_attacks_tier_1 = [
    (MAGICAL_FINGER_PISTOL_DATA, 3),
    (FIREBOLT_DATA, 2),
    (MENTAL_DAGGER_DATA, 1),   
]

""" Spells Tier 2 """
ACID_ARROW_DATA: dict = {
    "name": "Acid Arrow",
    "damage": 40,
    "accuracy": 100,
    "effect": [effects.debuff, ["defense"], [25], 10],
    "type": "special",
    "description": "a good spell that, in 10 percent of the cases, lowers the target's defense by 25%."
}

MAGIC_PROJECTILES_DATA: dict = {
    "name": "Magic Projectiles",
    "damage": 18,
    "type": "special",
    "description": "a good spell that hits 2-5 times."
}

CONFUSE_DATA: dict = {
    "name": "Confuse",
    "damage": 40,
    "accuracy": 90,
    "effect": [effects.stun, 10],
    "type": "special",
    "description": "a offensive spell that, in 10 percent of the cases, stuns the target."
}



spell_attacks_tier_2 = [
    (ACID_ARROW_DATA, 1),
    (MAGIC_PROJECTILES_DATA, 1),
    (CONFUSE_DATA, 1),    
]

""" Spells Tier 3 """

SURF_DATA: dict = {
    "name": "Tidal Wave",
    "damage": 80,
    "accuracy": 100,
    "type": "special",
    "description": "a strong and reliable spell",
}

ONE_STEP_AHEAD_DATA: dict = {
    "name": "One Step Ahead",
    "damage": 60,
    "accuracy": 90,
    "effect": [effects.buff, ["initiative"], [25], 10],
    "type": "special",
    "description": "a good spell that, in 10 percent of the cases, raises the user's initiative by 25."
}

MENTAL_SPEAR_DATA: dict = {
    "name": "Mental Spear",
    "damage": 60,
    "accuracy": 90,
    "effect": [effects.buff, ["spell_attack"], [25], 10],
    "type": "special",
    "description": "Mental Spear is a powerful spell that, in 10 percent of the cases, raises the user's spell attack by 25 percent."
}

spell_attacks_tier_3 = [
    (SURF_DATA, 1),
    (MENTAL_SPEAR_DATA, 1),
    (ONE_STEP_AHEAD_DATA, 1),
]

""" Spells Tier 4 """
MENTAL_OVERLOAD_DATA: dict = {
    "name": "Mental Overload",
    "damage": 80,
    "accuracy": 90,
    "effect": [effects.debuff, ["spell_def"], [25], 10],
    "type": "special",
    "description": "a strong spell that, in 10 percent of the cases, lowers the target's spell defense by 25."
}

SEIZE_THE_MIND_DATA: dict = {
    "name": "Seize the Mind",
    "damage": 60,
    "accuracy": 90,
    "effect": [effects.damage_via_health_missing, 15],
    "type": "special",
    "description": "a good spell that deals 15 percent of the target's missing health as damage."
}

spell_attacks_tier_4 = [
    (MENTAL_OVERLOAD_DATA, 1),
    (SEIZE_THE_MIND_DATA, 1),
]

""" Spells Tier 5 """
FIRE_BATH_DATA: dict = {
    "name": "Fire Bath",
    "damage": 100,
    "accuracy": 95,
    "type": "special",
    "description": "a really strong and precise spell"
}

TO_MUCH_TO_HANDLE: dict = {
    "name": "2Much 2Handle",
    "damage": 80,
    "accuracy": 95,
    "effect": [effects.stun, 30],
    "type": "special",
    "description": "a strong spell that, in 30 percent of the cases, stuns the target."
}

spell_attacks_tier_5 = [
    (FIRE_BATH_DATA, 1),
    (TO_MUCH_TO_HANDLE, 1),
]



spell_attack_tiers = [spell_attacks_tier_1, spell_attacks_tier_2, spell_attacks_tier_3, spell_attacks_tier_4, spell_attacks_tier_5]

""" Ranged Attacks """



""" Boost Moves"""

MUSCLE_UP_DATA = {
    "name": "Muscle Up",
    "stats": ["attack"],
    "amounts": [25],
    "description": "raises the user's attack by 25 percent."
}

CONCENTRATE_DATA = {
    "name": "Concentrate",
    "stats": ["spell_attack"],
    "amounts": [25],
    "description": "raises the user's spell attack by 25 percent."
}

DEFENSIVE_STANCE_DATA = {
    "name": "Defensive Stance",
    "stats": ["defense", "attack"],
    "amounts": [50, -25],
    "description": "a boost move that raises the user's defense by 50 percent and lowers their attack by 25 percent."
}

boosts_tier_1 = [
    (MUSCLE_UP_DATA, 1),
    (CONCENTRATE_DATA, 1),
    (DEFENSIVE_STANCE_DATA, 1),
]


BULK_UP_DATA = {
    "name": "Bulk Up",
    "stats": ["attack", "defense"],
    "amounts": [25, 25],
    "description": "Bulk Up raises the user's attack and defense by 25 percent."
}

TAKE_TIME_DATA = {
    "name": "Take Time",
    "stats": ["attack", "initiative"],
    "amounts": [40, -25],
    "description": "Take Time raises the user's attack by 40 percent and lowers their initiative by 25 percent."
}

INNER_FOCUS_DATA = {
    "name": "Inner Focus",
    "stats": ["spell_attack", "spell_def"],
    "amounts": [25, 25],
    "description": "Inner Focus raises the user's spell attack and spell defense by 25 percent."
}

boosts_tier_2 = [
    (BULK_UP_DATA, 3),
    (TAKE_TIME_DATA, 1),
    (INNER_FOCUS_DATA, 1),
]
                 

MIND_OVER_MATTER_DATA: dict = {
    "name": "Mind Over Matter",
    "stats": ["spell_def", "spell_attack", "defense", "attack"],
    "amounts": [50, 50, -25, -25],
    "description": "raises the user's spell defense and spell attack by 50 percent and lowers their defense and attack by 25 percent."
}

MOMENT_OF_CLARITY_DATA: dict = {
    "name": "Moment of Clarity",
    "stats": ["spell_attack", "initiative"],
    "amounts": [50, -25],
    "description": "Moment of Clarity raises the user's spell attack by 50 percent and their initiative by 25 percent."
}

BRAWN_OVER_BRAIN_DATA: dict = {
    "name": "Brawn Over Brain",
    "stats": ["attack", "defense", "spell_attack", "spell_defense"],
    "amounts": [50, 50, -25, -25],
    "description": "raises the user's attack and defense by 50 percent and lowers their spell attack and spell defense by 25 percent."
}

boosts_tier_3 = [
    (MIND_OVER_MATTER_DATA, 2),
    (MOMENT_OF_CLARITY_DATA, 1),
    (BRAWN_OVER_BRAIN_DATA, 2),
]


INNER_FOCUS_DATA: dict = {
    "name": "Inner Focus",
    "stats": ["spell_attack"],
    "amounts": [50],
    "description": "Inner Focus raises the spell attack of the user by 50 percent."
}

DANCING_DRAGON_DATA: dict = {
    "name": "Dancing Dragon",
    "stats": ["initiative", "attack"],
    "amounts": [25, 25],
    "description": "raises the user's initiative and attack by 25 percent."
}

FORT: dict = {
    "name": "Fort",
    "stats": ["defense", "spell_defense"],
    "amounts": [25, 25],
    "description": "raises the user's defense and spell defense by 25 percent."
}


boosts_tier_4 = [
    (INNER_FOCUS_DATA, 1),
    (DANCING_DRAGON_DATA, 1),
    (FORT, 1),
]

MEMENTO_MORI_DATA: dict = {
    "name": "Memento Mori",
    "stats": ["spell_attack", "defense"],
    "amounts": [100, -50],
    "description": "raises the user's spell attack by 100 percent and lowers their defense by 50 percent."
}

ALL_IN_DATA: dict = {
    "name": "All In",
    "stats": ["spell_defense", "attack"],
    "amounts": [-50, 100],
    "description": "All In raises the user's attack by 100 percent and lowers spell defense by 50 percent."
}

ONE_PUNCH_MAN = {
    "name": "One Punch - One Kill",
    "stats": ["attack"],
    "amounts": [60],
    "description": "raises the user's attack by 60 percent."
}

boosts_tier_5 = [
    (MEMENTO_MORI_DATA, 1),
    (ALL_IN_DATA, 1),
    (ONE_PUNCH_MAN, 1)
]

buff_tiers = [boosts_tier_1, boosts_tier_2, boosts_tier_3, boosts_tier_4, boosts_tier_5]

WAR_DRUMS_DATA: dict = {
    "name": "War Drums",
    "stats": ["attack", "initiative"],
    "amounts": [10, 10],
    "description": "War Drums raises the attack and initiative of all allies."
}




""" Debuff Moves"""

""" Heal Moves"""