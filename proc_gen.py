from data.level_map import level_map
import data.scenes_dat as scenes_dat
import random
import utils
import encounters

class Room:
    def __init__(self, walkable_tiles, type):
        self.walkable_tiles = walkable_tiles
        self.type = type
        self.scene = self.rand_scene()
        self.encounter = encounters.Encounter(self.random_encounter_type()) # function call is unnecessary?

    def rand_scene(self):
        if self.type == "village":
            return "village"
        
        roll = random.randint(1, 10)
        if roll < 3:
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


