import random

import actions

import entities
from entities import Fighter

from data import moves_dat, fighters_dat

from components import effects, input_handlers
from utils import Vector2
import proc_gen


Game = True
Level_Dim = 5

player_name = "John"  # input("What is your Name? \n")
print(f"Hello {player_name}! \n")

level1 = proc_gen.Level()

player = entities.Player(Vector2(14, 13),
                         player_name,
                         **fighters_dat.PLAYER_START_DATA)
player.moves = [
    actions.Attack(player, **moves_dat.TACKLE_DATA),
    actions.Heal(player, "Heal", 40)
]



def update(player_upd, level_upd):
    """Main game loop. This function will update the game state and return a boolean"""
    room_rn = level_upd.room_array[player_upd.pos[0]][player_upd.pos[1]]

    """
    resolve the rooms encounter if its forced
    """

    print(f"You are in a {room_rn.scene}.\n")
    entities, mechanic = room_rn.encounter.update()
    unforced_mechanic = None
    if mechanic:
        if mechanic.forced:
            forc = mechanic.execute(entities, player_upd, objects_ls=room_rn.encounter.objects_ls)
            # returning 2 shall sent the player back to the previous room
            if forc == 2:
                player_upd.move_back()
                return True
            # returning 1 means the player died :(
            elif forc == 1:
                return False
            # returning 0 means the room is cleared
            elif forc == 0:
                # clear entities that are not NPC'S
                entities = [entity for entity in entities if not isinstance(entity, Fighter)]
        else:
            unforced_mechanic = mechanic

    """
    resolve the exploration
    """

    # this will return 1 when mechanic should be raised, 0 if moving to the next scene
    expo = input_handlers.exploration(room_rn.encounter.objects_ls, player_upd, entities, unforced_mechanic)
    if expo == 1 and unforced_mechanic:
        unforced_mechanic.execute(entities, player_upd)
    elif expo == 0:
        player_upd.move(room_rn)
    # other things are done by the input handler (Inventory)


    return True

while Game:
    Game = update(player, level1)
