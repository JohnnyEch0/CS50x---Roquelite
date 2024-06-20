# Generative Roquelike
#### Video Demo: https://youtu.be/vGoqsGsdSMM
#### Description:
My final Project for CS50x is a roquelike game where the player navigates through rooms of a certain scene type that may hold encounters, objects and items. In general, this game is like a mixture of pokemon and tabletop fantasy RPG's like Dungeons & Dragons or Videogames like Dragon Quest.
The focus for this project was a solid and flexible game logic instead of pretty sprites and animations. I think what i achieved is a solid logic that makes it easy to implement further functionality for: moves, items, enemies. The same cannot be said for Encounter-Types and their corresponding mechanics and objects.


#### Game World

The Game world is generated on a room by room basis. A Level class holds an 2 dimensional array of rooms and that is derived from a level map, which one can modify via the data/level_map_gen.py module or change it in the data/level_map.py. This level map consists of another 2D array of characters, where each character represents different room types like "O" for outer city rooms (less dangerous then inner city ones), "W" for Walls (which can't be walked into/through) and gates (ways into the inner city). Also a start position is given and marked with "V" for Village.

##### Rooms
Every room object gets its type from the level_map and processes it into a scene, that may be a village, a useful or basic scene. Every non-Village room then generates itself an Encounter-Object via a random choice from a list in data.scenes_dat.py, each element of this list has a string for its name and a weight for the random choice.
Afterwards a encounter for this room is generated.

##### Encounters
The encounter object uses the scene and the randomly picked encounter from the room and processes these into a mechanic and a list of entities. Depending on the Encounter type there will be weighted rolls on enemies, traders or items. Right now there are 4 encounter types:
1. Risk and Reward: A difficult fight that the player may take or flee, which rewards good loot.
2. Friendly: A Trader is found.
3. Basic Combat: A fight that has to be taken.
4. Village: A place to rest and level up.

The Mechanic is a mechanic object that is picked accordingly to the encounter type. 


##### Enemy Generation
Enemies are picked by keying the player level and the encounter weight in a dictionary data.fighters_dat.encounter_weights[key]. This will give us an Amount and a Enemy Table to roll on.
Afterwards, we will roll Amount times on the picked table, which is, again, a weighted list to be rolled on by the random_choice_list_tuple() function in utils.py. We then return a list of the rolled enemies to the specific function that handles the encounter generation for this type of encounter.

##### Items Generation
A "Risk Reward" Encounter will also roll for items in a logic quite similiar to the enemy generation. These Items may be consumables, or in rare cases Equipment (which is scaled to the player level.) Also some rooms will get gold, rolled for in the random_gold() function.
Each item is created as an instance of the items.py Item class, or more specifically one of its children Gold, Equipment or Object. Most Items also get an effect that they get from data.effects_dat.py- which holds dictionaries where the keys are the item name and the values are effects with arguments.

##### Object Generation
If a room has a "useful scene" we generate a object according to this scene, taking into account the player level. This will be Combat-Move Tutors or a Shrine, that can increase player stats permanently.
Each Object is created as an instance of the items.py Object Class, and given a mechanic to be triggered when interacted with. 

#### Stats
Similar to Pokemon, we have 6 main stats: Health, Attack, Spell Attack, Defense, Spell Defense and Initiative which depend on the Fighters Level and their base-stats. Damage Calculations are done like the early generations of pokemon Games do. The Player stats are higher then the enemies' because the player constantly has to fight two, three or four against one battles. The Basic Formula is:
(Base-Stat * 2 + "flat_value") / 20 * level, where the flat value is different for Health and all the other stats. 

#### Mechanics
Most of the game logic is split between components/mechanics.py and /input_handlers.py. There are two types of combat implemented, also we have a stealth logic that is buggy as of now. The village mechanic is mainly done in the input handlers, though it takes a step through the village mechanic object. Move Tutors and Shrines get their seperate mechanics. This approach seems redundant sometimes, espacially for the village. 

#### Combat-Moves
Moves come in different forms: (Spell-)Attacks and Buffs.
Attacks have a Damage and an Accuracy value, some of them also have effects that may buff/debuff, hit again depending on the missing health of the target or have them flinch(skip a turn).
Buffs usually just have an Effect, which is a buff or debuff on specific stat(s) by given amount(s).
A player may learn new moves in specific scenes, via a scroll object, these scale according to player level.
The Code is in components/actions.py and /effects.py. The Data is found in data/moves_dat.py and/effects_dat.py.

#### Items
Items may be Consumable, like a Healing Potion or the Dust of Disappearance, or Equipable, like an array of leveled items that boost your base stats, crit-chance and evasion. 

When Levelling up, the player may increase his stats with 6 individual points, while also scaling according to a base stat * level / 20 formula that is also implemented like the early generations of pokemon- but broken down to 20 levels.

#### Enemies
Enemies are Fighter objects, the arguments for those objects are derived from data/fighters_dat.py. Right now they jsut randomly select moves in combat against the player and cannot interact with the game world. For now we have two types of enemies: Goblins and Abominations (mostly mutated bugs). They have a level that is corresponding to the players level when the encounter is generated.

#### GUI
Instead of using the obvious PyGame, i decided to learn the gui library "Tkinter" and use it to display basic game information and input options to my player. I switched from only text based input in the console to this solution because it was more pretty and a good way to learn this library.For most Widgets we are using the grid-based approach. My Approach is seperated into multiple widgets:

##### App(ttk.Window)
The object derived from this class is the main window and holds all the other windows. These Windows are:
1. Menu - a dropdown at the very top, where you can de-activate the log.
2. Input Frame - located at the bottom of the app, this is where we will create the buttons for the user to click. We iterate over all the options and create button in create_widgets(options) - which will be called from the update method. The update method waits for a "input" variable to change and returns it to the input handler method that called it.
3. Main Frame - This holds a Notebook which in turn holds multiple, switchable, widgets. More Information below.
4. Log Frame - Located to the right, close to every event in the game that is relevant to the player will be placed here and have a timestamp, older messages will disapper to the top, but the frame is scrollable.

##### Main_Frame
The object derived from this class will have 3 major components:
1. metrics Hud- almost permanently shows player health, level, gold and EXP.
2. a level_up widget, which is hidden by default, but shown when leveling up.
3. The Notebook contains a lot of functionality
    - A narration Tab where we can describe a scene to the player in type-writing style.
    - A combat Tab, which will show us the fighters and their health bars, it will automatically be shown when a comba staats
    - Inventory Tab, will hold the players inventory, is devided into consumables and equipment.
    - Map Tab, will get a 5x5 array of rooms around the player and show it in a simple table.
    - Information Tab, can display further information about basically anything, right now it is only used for move-tutors as to enable the player to make an educated Choice.






