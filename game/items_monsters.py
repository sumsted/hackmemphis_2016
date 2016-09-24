""" All possible items and monsters are kept here.
These are imported into room when building each room object.

ITEMS - list of dictionaries containing
  name - name of the room
  attack - number of points deducted from monster during attack
  health - number of points added to player if eaten


MONSTERS - list of dictionaries containing
  name - name of monster
  attack - number of points deducted from player during counter attack
  health - starting health of monster

"""
STARTING_ITEM = 0

ITEMS = [
    {'name': 'spoon', 'attack': -5, 'health': -1},
    {'name': 'sword', 'attack': 8, 'health': -100},
    {'name': 'chair', 'attack': 5, 'health': 1},
    {'name': 'thimble', 'attack': 1, 'health': 0},
    {'name': 'branch', 'attack': 6, 'health': 1},
    {'name': 'book', 'attack': 4, 'health': 2},
    {'name': 'marker', 'attack': 2, 'health': -1},
    {'name': 'teacher', 'attack': 4, 'health': 2},
    {'name': 'soda', 'attack': 1, 'health': 6},
    {'name': 'skittles', 'attack': 0, 'health': 4},
    {'name': 'pen', 'attack': 23, 'health': -1},
    {'name': 'table', 'attack': 30, 'health': -10},
    {'name': 'pizza', 'attack': 2, 'health': 100},
    {'name': 'unicorn', 'attack': 20, 'health': 30},
    {'name': 'chicken', 'attack': 0, 'health': 10}
]

MONSTERS = [
    {'name': 'Grover', 'attack': 1, 'health': 5},
    {'name': 'Elmo', 'attack': 2, 'health': 10},
    {'name': 'Cookie Monster', 'attack': 8, 'health': 20},
    {'name': 'Big Bird', 'attack': 10, 'health': 30},
    {'name': 'Potato Man', 'attack': 6, 'health': 20},
    {'name': 'Peanutbot', 'attack': 5, 'health': 12}
]
