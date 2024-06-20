""" Main file for the game. This file will run the game loop and handle the game state. """

import threading
import components.actions as actions

import entities
from entities import Fighter

from data import moves_dat, fighters_dat

from components import input_handlers
from utils import Vector2
import map.proc_gen as proc_gen
import gui


Game = True

level1 = proc_gen.Level()

player_name = "John"  # input("What is your Name? \n")
print(f"Hello {player_name}! \n")



player = entities.Player(Vector2(14, 13),
                         player_name,
                         **fighters_dat.PLAYER_START_DATA)
player.moves = [
    actions.Attack(**moves_dat.TACKLE_DATA),
]



GUI = gui.App(player, level1)
InputHandler = input_handlers.InputHandler(player, level1, GUI)

narrator= GUI.main_frame.notebook.narration


narrator.update_text("You are in a village. \n\nYou can explore the village or move to the next scene.")


def update(player_upd, level_upd):
    """Main game loop. This function will update the game state and return a boolean"""
    room_rn = level_upd.room_array[player_upd.pos[0]][player_upd.pos[1]]
    # print(f"You are in a {room_rn.scene}.\n")
    InputHandler.room_log(room_rn)

    """
    resolve the rooms encounter if its forced
    """
    
    entities, mechanic = room_rn.encounter.update(player_upd.level)
    unforced_mechanic = None
    if mechanic:
        if mechanic.forced:
            forc = mechanic.execute(entities, player_upd, InputHandler, objects_ls=room_rn.encounter.objects_ls)
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
                room_rn.encounter.done = True
        else:
            unforced_mechanic = mechanic

    """
    resolve the exploration
    """

    # this will return 1 when mechanic should be raised, 0 if moving to the next scene
    expo = InputHandler.exploration(room_rn.encounter.objects_ls, entities, unforced_mechanic)
    if expo == 1 and unforced_mechanic:
        unforced_mechanic.execute(entities, InputHandler)
    elif expo == 0:
        InputHandler.movement(room_rn)

    return True

def game_loop(gui):
    Game = True
    while Game:
        Game = update(player, level1)
        gui.after(0, gui.update_gui)
        
    if not Game:
        print("Game Over")
        narrator.update_text("Game Over")

    # end of game


threading.Thread(target=game_loop, args=(GUI,)).start()
GUI.mainloop()




