from proc_gen import Level

def test_generate_rooms():
    # Set up the level map
    level_map = [
        ['O', 'O', 'O', 'O', 'O'],
        ['G', 'W', 'O', 'O', 'O'],
        ['O', 'G', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'W', 'O'],
        ['O', 'O', 'O', 'O', 'O']
    ]


    # Create an instance of the Level class
    level = Level(level_map)

    # Print the generated rooms to the console
    for row in level.room_array:
        row_text = ""
        for room in row:
            row_text += f"{room.walkable_tiles}"
        print(row_text)
            

# Run the test
test_generate_rooms()