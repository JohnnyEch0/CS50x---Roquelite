import components.effects as effects

TACKLE_DATA = {
    "name": "Tackle",
    "damage": 40,
    "description": "Tackle is a basic attack."
}

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
    "description": "Feint is a weak attack that, in 30 percent of the cases, raises the user's evasion by 10."
}

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

FIREBOLT_DATA: dict = {
    "name": "Firebolt",
    "damage": 60,
    "accuracy": 90,
    "type": "special",
    "description": "Firebolt is a good spell used by goblin mages."
}


MENTAL_SPEAR_DATA: dict = {
    "name": "Mental Spear",
    "damage": 60,
    "accuracy": 90,
    "effect": [effects.buff, ["spell_attack"], [25], 10],
    "type": "special",
    "description": "Mental Spear is a powerful spell that, in 10 percent of the cases, raises the user's spell attack by 25 percent."
}

SURF_DATA: dict = {
    "name": "Tidal Wave",
    "damage": 90,
    "accuracy": 100,
    "type": "special",
    "description": "",
}


""" Ranged Attacks """



""" Boost Moves"""

BULK_UP_DATA = {
    "name": "Bulk Up",
    "stats": ["attack", "defense"],
    "amounts": [25, 25],
    "description": "Bulk Up raises the user's attack and defense by 25 percent."
}

TAKE_TIME_DATA = {
    "name": "Take Time",
    "stats": ["attack", "initiative"],
    "amounts": [50, -25],
    "description": "Take Time raises the user's attack by 50 percent and lowers their initiative by 25 percent."
}

INNER_FOCUS_DATA = {
    "name": "Inner Focus",
    "stats": ["spell_attack", "spell_def"],
    "amounts": [25, 25],
    "description": "Inner Focus raises the user's spell attack and spell defense by 25 percent."
}

MEMENTO_MORI_DATA: dict = {
    "name": "Memento Mori",
    "stats": ["spell_attack", "defense"],
    "amounts": [100, -50],
    "description": "Memento Mori raises the user's spell attack by 100 percent and lowers their defense by 50 percent."
}

MIND_OVER_MATTER_DATA: dict = {
    "name": "Mind Over Matter",
    "stats": ["spell_def", "spell_attack", "defense", "attack"],
    "amounts": [50, 50, -25, -25],
    "description": "Mind Over Matter raises the user's spell defense and spell attack by 50 percent and lowers their defense and attack by 25 percent."
}

WAR_DRUMS_DATA: dict = {
    "name": "War Drums",
    "stats": ["attack", "initiative"],
    "amounts": [10, 10],
    "description": "War Drums raises the attack and initiative of all allies."
}

INNER_FOCUS_DATA: dict = {
    "name": "Inner Focus",
    "stats": ["spell_attack"],
    "amounts": [50],
    "description": "Inner Focus raises the spell attack of the user by 50 percent."
}
""" Debuff Moves"""

""" Heal Moves"""