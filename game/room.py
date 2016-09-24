"""A Room defines a location that a player occupies

A room has a name and may contain one to two items and one monster.

Item count may be increased by changing MAX_ITEMS.

Monster count is fixed to either 1 or 0.

"""
import random
from items_monsters import MONSTERS, ITEMS


class Room():
    MAX_ITEMS = 2

    def __init__(self, name=None):
        self.name = 'Some Random Room' if name is None else name
        self.items = random.sample(ITEMS, random.randint(0, self.MAX_ITEMS))
        monster = random.sample(MONSTERS, random.randint(0, 1))
        self.monster = dict(monster[0]) if len(monster) > 0 else None

    def get_description(self):
        description = "\nYou are in the %s.\n" % self.name
        if len(self.items) > 0:
            description += "\nThere's some junk in here. It looks like a..."
            for index, item in enumerate(self.items):
                if index > 0:
                    description += "  and a %s" % item['name']
                else:
                    description += "  a %s" % item['name']
            description += "\n"
        if self.monster is not None:
            if self.monster['health'] > 0:
                description += "\nThere's a %s in here that looks angry.\n" % self.monster['name']
            else:
                description += "\nThere's a dead %s laying on the floor.\n" % self.monster['name']
        return description