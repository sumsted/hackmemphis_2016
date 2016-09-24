"""Defines a Player

Players have a name, a location, health and a single item.
Player health begins at 100 but can be changed through STARTING_HEALTH.
STARTING_LOCATION can be changed, upper left of map is is 0,0

COULD ADD

POINTS
  add self.points = 0 in __init__()
  print self.points in get_description()
  Then in schooladventure add to the player.points the number of health points deducted from a monster during attack.

"""
from items_monsters import ITEMS, STARTING_ITEM


class Player():
    STARTING_HEALTH = 100
    STARTING_LOCATION = [0, 0]

    def __init__(self, player_name):
        self.name = player_name
        self.location = self.STARTING_LOCATION
        self.health = self.STARTING_HEALTH
        self.items = [ITEMS[STARTING_ITEM]]
        self.points = 0
        # you may create a self.points variable and set it to zero

    def get_description(self):
        description = "\n\nI know what dude I am.  I'm %s!\n" % self.name
        description += "\nMy health is %d. I have %d points. and I'm carrying ....let me see... I'm carrying...\n" % (self.health, self.points)
        for index, item in enumerate(self.items):
            if index > 0:
                description += "\n      and a %s" % item['name']
            else:
                description += "\n          a %s" % item['name']
        description += "\n"

        # you may add points to description here

        return description
