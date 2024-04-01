"""
Main Game Loop GUI

- Window for possible Inputs
    - Text and Button-Based?
- Main Window
    - Window for Narration (collapsable) (Turned on or off by the player)
    - Window for Log (Optional, can be Overlay or Collapsable)
    - Minimap Overlay
    - Log Overlay
    - Inventory
        - Window for Inventory ()
        - Window for Stats ()
        - Full Minimap
    - simple combat visualisation
"""

""" Return any keypress with this?"""
window.bind("<KeyPress>", lambda e: print(e.char)) # any key press on the window



""" LEvelling up """
spin = ttk.Spinbox(master=window, from_=0, to=6, textvariable= spint_int, wrap= False)

""" Progress Bar
    - We can use them for Health, Mana, Exp etc. 
    - Maybe can create a timed minigame for the player with a progress bar and its start(ms) method

"""


""" Scrollable Text Input for NPC interaction"""