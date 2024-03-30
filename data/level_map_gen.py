map_size = 15
city_size = 5

# Initialize the map with 'O' (outside the city)
game_map = [['O' for _ in range(map_size)] for _ in range(map_size)]

# Calculate the starting position of the city
city_start = (map_size // 2) - (city_size // 2)

# Fill the city area with 'I' (inside the city)
for i in range(city_start, city_start + city_size):
    for j in range(city_start, city_start + city_size):
        game_map[i][j] = 'I'

# Add walls around the city
for i in range(city_start - 1, city_start + city_size + 1):
    game_map[i][city_start - 1] = 'W'  # Left wall
    game_map[i][city_start + city_size] = 'W'  # Right wall

for j in range(city_start - 1, city_start + city_size + 1):
    game_map[city_start - 1][j] = 'W'  # Top wall
    game_map[city_start + city_size][j] = 'W'  # Bottom wall

# Add gates to the city
gate_positions = [(city_start - 1, city_start + city_size // 2),  # Top gate
                  (city_start + city_size // 2, city_start - 1),  # Left gate
                  (city_start + city_size, city_start + city_size // 2),  # Bottom gate
                  (city_start + city_size // 2, city_start + city_size)]  # Right gate

for gate_pos in gate_positions:
    game_map[gate_pos[0]][gate_pos[1]] = 'G'

game_map[0][0] = 'V'

# Print the game map
for row in game_map:
    print(' '.join(row))
    # Save the game map to a separate .py file called level_map.py
    with open('C:\\Users\\Chill\\Desktop\\python\\generative_roquelike\\data\\level_map.py', 'w') as file:
        file.write("level_map = [\n")
        for row in game_map:
            file.write(f"    {row},\n")
        file.write("]\n")