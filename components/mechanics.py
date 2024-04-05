
import random
from entities import Fighter

class Mechanic():
    def __init__(self, forced=False):
        self.forced = forced

class Village(Mechanic):
    def __init__(self, forced=False):
        # Maybe we shouldn't force this one?
        super().__init__(forced)

    def execute(self, entities, InputHandler):
        print("Welcome to the Village!")
        """ This Input Handler should return us the trade or level up or rest machanic"""
        InputHandler.village(entities)

class Trade(Mechanic):
    """
    This class will handle the trading mechanics.
    Right now a lot of it is still inside the input handler :c
    """
    def __init__(self, forced=False):
        super().__init__(forced)


    def execute(self, entities, InputHandler):
        print(f"Welcome to my shop! Would you like to buy or sell something?")
        InputHandler.trading(entities[0])

class Risk_Reward(Mechanic):
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

    def execute(self, entities, player, InputHandler):
        print("Combat!")
        round = 0
        enemies = [entity for entity in entities if entity.faction != "Heroes"]
        entities.append(player)
        ini_list = sorted(entities, key=lambda x: x.initiative, reverse=True)
        while True:
            print(f"\n----Round {round}----")
            round += 1

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
                    return 2 # player fled
                else:
                    print("You failed to flee!")

            if menu_input == 1:
                # player is fighting
                # should return the move the player wants to use
                move_input = InputHandler.combat()


            # fight for a round
            for i in ini_list:
                if i.health < 1:
                    ini_list.remove(i)
                    enemies.remove(i)
                    print(f"{i.name} died. ")
                    if i.faction != "Heroes":
                        player.exp += i.exp_given
                        print(f"You gained {i.exp_given} exp!")
                    
                    
                if i.faction == "Heroes":
                    # target selection should be done inside of input handler
                    target = InputHandler.target_selection(enemies)

                    # move_input.use should get the target from the input handler
                    move_input.use(player, ini_list, target)
                else:
                    i.fight(ini_list)
            if player.health < 1:
                print("You died!")
                return 1
            if len(ini_list) <= 1:
                print(f"----room cleared----\n")
                return 0

    def flee(self, player, enemy_mod):
        """This function will handle the fleeing of the player."""
        if random.randint(0, 100) + enemy_mod > player.initiative:
            print("You fled!")
            return 2
        else:
            print("You failed to flee!")
            return 1


