"""This module will contain the different mechanics that can be used in the game."""

import random
from entities import Fighter

class Mechanic():
    def __init__(self, forced=False):
        self.forced = forced

class Village(Mechanic):
    """ 
    This could probably be removed and done in Input Handlers
    """

    def __init__(self, forced=False):
        super().__init__(forced)

    def execute(self, entities, InputHandler):
        """ This Input Handler should return us the trade or level up or rest machanic"""
        InputHandler.village(entities)

class Trade(Mechanic):
    """
    This class will handle the trading mechanics.
    Right now a lot of it is still inside the input handler
    Maybe we can move it there alltogether
    """
    def __init__(self, forced=False):
        super().__init__(forced)


    def execute(self, entities, InputHandler):
        print(f"Welcome to my shop! Would you like to buy or sell something?")
        InputHandler.trading(entities[0])

class Risk_Reward(Mechanic):
    """This class will handle the risk and reward mechanics."""
    def __init__(self, forced=True):
        super().__init__(forced)

    def execute(self, entities, player, InputHandler, objects_ls=[] ):
        # invisibility route
        if player.invisible:
            # get player input
            result_invis = self.execute_invisible(entities, player,InputHandler , objects_ls )
            return result_invis

        result = InputHandler.risk_reward(entities)
        if result == 1:
            # grab fighter entities in entities via isinstance
            entities = [entity for entity in entities if isinstance(entity, Fighter)]
            result = Combat().execute(entities, player, InputHandler)
        return result

    def execute_invisible(self, entities, player, InputHandler, objects_ls=[]):
        # different input handler for invisible player
            result_invis = InputHandler.invisible_risk_reward(entities, objects_ls)

            if result_invis == 1:
                # the player decided to fight
                return self.combat_out_stealth(entities, player, InputHandler, objects_ls)
            elif result_invis == 2:
                # the player decided to flee
                return 2
            elif result_invis == 3:
                # the player decided to stay invisible
                return 0
            elif result_invis == 4:
                # the player decides to try and steal the item
                # think this can handle multiple items now
                steal_success = self.steal(entities, player, InputHandler , objects_ls=objects_ls)
                if steal_success == 0:
                    return 0
                else:
                    return self.combat_out_stealth(entities, player)

    def steal(self, entities, player,  objects_ls=[]):
        """This function will handle the stealing of an item from the risk and reward encounter."""

        # get the number of fighters
        num_fighters = len([entity for entity in entities if isinstance(entity, Fighter)])
        # roll a dice for each fighter and for the player
        player_roll = random.randint(1, 10) + int(player.evasion / 10)
        fighter_rolls = [random.randint(1, 5) for i in range(num_fighters)]
        # check if the player roll is higher than the fighter rolls
        if player_roll > max(fighter_rolls):
            print("You stole the item!")
            for item in objects_ls:
                player.inventory.append(item)
                print(f"You added {item.name} to your inventory. {player.inventory}")
            return 0
        else:
            print("You failed to steal the item! \n You may get a Move in before it gets ugly.")
            return 1

    def combat_out_stealth(self, entities, InputHandler, player):
        """This function will handle the combat after the player has failed to steal an item."""
        move_input = InputHandler.combat()
        move_input.use(player, entities)
        player.invisible = False
        result = Combat().execute(entities, player, InputHandler)
        return result

class Combat(Mechanic):
    """This class will handle the combat mechanics."""
    def __init__(self, forced=True):
       super().__init__(forced)

    def execute(self, entities, player, InputHandler, objects_ls=[]):
        print("Combat!")
        round = 0
        enemies = [entity for entity in entities if entity.faction != "Heroes"]
        entities.append(player)
        ini_list = sorted(entities, key=lambda x: x.initiative, reverse=True)
        remember_stats = player.get_stats_as_dict()
        remember_stats["Evasion"] = player.evasion
        while True:
            InputHandler.log(f"\n----Round {round}----")
            round += 1

            InputHandler.combat_ui(enemies, player)

            # get user combat/inv/flee input
            menu_input = InputHandler.combat_menu()

            # returning 2 means trying to fleeing
            if menu_input == 2:
                # entitites mod should be the average if the entitites initiative
                enemies_mod = sum([entity.initiative for entity in enemies]) / len(enemies) 
                result = self.flee(player, enemies_mod)
                if result == 2:
                    player.move_back()
                    print("You fled!")
                    reset_stats(player, remember_stats)
                    return 2 # player fled
                else:
                    print("You failed to flee!")

            if menu_input == 1:
                # player is fighting
                move_input = InputHandler.combat()


            # fight for a round
            for i in ini_list:
                if i.health < 1:
                    ini_list.remove(i)
                    enemies.remove(i)
                    print(f"{i.name} died. ")
                    if i.faction != "Heroes":
                        player.exp += i.exp_given
                        InputHandler.log(f"{i.name} gave {i.exp_given} exp.")
                    continue
                    
                    
                if i.faction == "Heroes":
                    if menu_input == 1:
                        # target selection in InputHandler
                        # check if the move is targeted
                        if move_input.targeted:
                            target = InputHandler.target_selection(enemies)
                        else:
                            target = None
                        # move_input.use should get the target from the input handler
                        log = move_input.use(player, ini_list, target)
                        InputHandler.log(log)
                else:
                    log = i.fight(ini_list)
                    InputHandler.log(log)
            
            if player.health < 1:
                print("You died!")
                return 1
            if len(ini_list) <= 1:
                # reset the players stats
                reset_stats(player, remember_stats)
                

                InputHandler.log("----Scene cleared of enemies!----\n")
                return 0

    def flee(self, player, enemy_mod):
        """This function will handle the fleeing of the player."""
        if random.randint(0, 100) + enemy_mod > player.initiative:
            print("You fled!")
            return 2
        else:
            print("You failed to flee!")
            return 1


def reset_stats(player, remember_stats):
    """
    This function will reset the players stats to their base stats.
    Used in Combat because of temporary boosts and debuffs.
    """
    player.attack = remember_stats["Attack"]
    player.defense = remember_stats["Defense"]
    player.spell_attack = remember_stats["Spell Attack"]
    player.spell_def = remember_stats["Spell Defense"]
    player.initiative = remember_stats["Initiative"]
    player.evasion = remember_stats["Evasion"]


""" Object Mechanics"""

class Move_Learning(Mechanic):
    """ Takes a list of moves and lets the player choose one to learn."""
    def __init__(self, moves: list, forced=False):
        super().__init__(forced)
        self.moves = moves

    def execute(self, entities, player, InputHandler):
        InputHandler.move_learning_selection(self.moves)
        return 0
    
class Shrine(Mechanic):
    """
    This class will handle the shrine mechanics.
    An object that will boost the players stats permanently.
    """
    def __init__(self, stat, amount, forced=False):
        super().__init__(forced)
        self.stat = stat
        self.amount = amount

    def execute(self, entities, player, InputHandler):
        player.base_stats[self.stat] += self.amount 
        InputHandler.log(f"Your base {self.stat} increased by {self.amount}.")
        return 0