""" This module contains the classes for the procedural generation of the map. """

from data.level_map import level_map
import data.scenes_dat as scenes_dat
import random
import utils
import map.encounters as encounters


class Room:
    def __init__(self, walkable_tiles, type):
        self.walkable_tiles = walkable_tiles
        self.type = type
        self.explored = False
        self.scene = self.rand_scene()
        self.encounter = encounters.Encounter(self.random_encounter_type(), self.scene) # function call is unnecessary?
        

    def rand_scene(self):
        if self.type == "village":
            self.explored = True
            return "village"
        
        roll = random.randint(1, 10)
        if roll < 5:
            return utils.random_choice(scenes_dat.useful_places)
        else:
            return utils.random_choice(scenes_dat.places)
        
    def random_encounter_type(self):
        if self.type == "village":
            return "village"
        
        return utils.random_choice(scenes_dat.encounter_types)
            
    
    

class Level:
    def __init__(self, level_map=level_map):
        self.level_map = level_map
        self.room_array = self.generate_rooms()
        self.entities_list = []

    def generate_rooms(self):
        """Generate rooms based on the level map."""
        rooms = []
        for row_index, row in enumerate(self.level_map):
            room_row = []
            for col_index, char in enumerate(row):  # Add 'col_index' variable and enumerate over the columns
                
                # Create a new room based on the character
                if char != 'W':
                    # These rooms are walkable
                    walkable_tiles = self.walkable_tiles(row_index, col_index)
                    
                    
                    # inner city room
                    if char == 'I':
                        room = Room(walkable_tiles, type="proc_gen_inner")
                    
                    # outer city room
                    elif char == 'O':
                        room = Room(walkable_tiles, type="proc_gen_outer")
                    
                    # gate room
                    elif char == 'G':
                        room = Room(walkable_tiles, type="gate")  
                    
                    elif char == 'V':
                        room = Room(walkable_tiles, type="village")
                            
                else:
                    # walls are not walkable
                    room = Room(walkable_tiles=[], type="wall")
                room_row.append(room)
            rooms.append(room_row)
                
        return rooms

    def walkable_tiles(self, row_index, col_index):
        """Return a list of walkable tiles around the current tile."""

        walkable_tiles = []

        # Check if the tile to the north is walkable
        if row_index > 0 and self.level_map[row_index-1][col_index] != 'W':
            walkable_tiles.append('W')

        # Check if the tile to the east is walkable
        # print(f"---&debug col_index: {col_index}")
        if col_index < len(self.level_map[row_index]) - 1 and self.level_map[row_index][col_index+1] != 'W':
            walkable_tiles.append('D')

        # Check if the tile to the south is walkable
        if row_index < len(self.level_map) - 1 and self.level_map[row_index+1][col_index] != 'W':
            walkable_tiles.append('S')

        # Check if the tile to the west is walkable
        if col_index > 0 and self.level_map[row_index][col_index-1] != 'W':
            walkable_tiles.append('A')

        return walkable_tiles

    def explore_room(self, player_x: int, player_y: int):
        """Set the room as explored."""
        self.room_array[player_x][player_y].explored = True

    def get_rooms_for_map_hud(self, player_x: int, player_y: int):
        """Return the rooms surrounding the player."""
        
        rooms = []
        

        for row_index, row in enumerate(self.room_array[player_x - 2:player_x + 3]):
            row_list = []
            
            for col_index, room in enumerate(row[player_y - 2:player_y + 3]):
                try:
                    row_list.append(room)

                except IndexError:
                    """ This is not needed."""
                    row_list.append("Not a room")

            rooms.append(row_list)
        
        # append None if there is no room in rooms in th 5x5 grid
        for i in range(5):
            try:
                if len(rooms[i]) < 5:
                    rooms[i].append("Not a room")
            except IndexError:
                rooms.append(["Not a room" for _ in range(5)])

        return rooms