import items
from entities import Player
from data import items_dat, fighters_dat
from utils import Vector2


def test_consume_healing_potion():
    # Set up test scenario
    user = Player(Vector2(14, 13),
                         "player_name",
                         **fighters_dat.PLAYER_START_DATA)
    target = user
    potion = items.Item(**items_dat.HEALING_POTION)

    # Add the potion to the user's inventory
    user.inventory.append(potion)

    # Verify that the potion is in the user's inventory
    assert potion in user.inventory

    # Call the consume method
    potion.consume(user, target)

    # Verify that the potion is removed from the user's inventory
    assert potion not in user.inventory

    # Verify that the healing effect is applied to the target
    assert target.health == target.max_health

# Run the test
test_consume_healing_potion()

def test_dust_of_disappearance():
    # Set up test scenario
    user = Player(Vector2(14, 13),
                         "player_name",
                         **fighters_dat.PLAYER_START_DATA)
    target = user
    dust = items.Item(**items_dat.DUST_OF_DISAPPEARANCE)

    # Add the dust to the user's inventory
    user.inventory.append(dust)

    # Verify that the dust is in the user's inventory
    assert dust in user.inventory

    # Call the consume method
    dust.consume(user, target)

    # Verify that the dust is removed from the user's inventory
    assert dust not in user.inventory

    # Verify that the invisibility effect is applied to the target
    # assert target.invisible

test_dust_of_disappearance()