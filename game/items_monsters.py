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

OLD_ITEMS = [
    {'name': 'spoon', 'attack': 1, 'health': -1},
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


ITEMS = [
    {'name': 'sword', 'attack': 30, 'health': -1},
    {'name': 'Kansas Big Jay', 'attack': 10, 'health': 4},
    {'name': 'South East Missouri Otahkian', 'attack': 8, 'health': 2},
    {'name': 'Bowling Green Bandit', 'attack': 1, 'health': 1},
    {'name': 'Ole Miss Rebel', 'attack': 30, 'health': 3},
    {'name': 'Temple Owl', 'attack': 15, 'health': 10},
    {'name': 'Tulane GreenWave', 'attack': 15, 'health': 2},
    {'name': 'Navy Midshipman', 'attack': 20, 'health': 1},
    {'name': 'Tulsa Captain Cane', 'attack': 10, 'health': 2},
    {'name': 'SMU Mustang', 'attack': 10, 'health': 5},
    {'name': 'USF Rocky the Bull', 'attack': 20, 'health': 10},
    {'name': 'Cincinnati Bearcat', 'attack': 20, 'health': 2},
    {'name': 'Houston Shasta', 'attack': 30, 'health': 1},
    {'name': 'Garabaldis Pizza', 'attack': 2, 'health': 30},
    {'name': 'noodles', 'attack': 2, 'health': 10},
    {'name': 'skittles', 'attack': 2, 'health': 10},
    {'name': 'unicorn', 'attack': 20, 'health': 30},
    {'name': 'chicken', 'attack': 0, 'health': 10},
    {'name': 'Chick fill a', 'attack': 20, 'health': 30},
    {'name': 'Red bull', 'attack': 5, 'health': 50}
]


OLD_MONSTERS = [
    {'name': 'Grover', 'attack': 1, 'health': 5},
    {'name': 'Elmo', 'attack': 2, 'health': 10},
    {'name': 'Cookie Monster', 'attack': 8, 'health': 20},
    {'name': 'Big Bird', 'attack': 10, 'health': 30},
    {'name': 'Potato Man', 'attack': 6, 'health': 20},
    {'name': 'Peanutbot', 'attack': 5, 'health': 12}
]


MONSTERS = [
    {'name': 'Grover', 'attack': 1, 'health': 5},
    {'name': 'Elmo', 'attack': 2, 'health': 10},
    {'name': 'Cookie Monster', 'attack': 8, 'health': 20},
    {'name': 'Big Bird', 'attack': 10, 'health': 30},
    {'name': 'Potato Man', 'attack': 6, 'health': 20},
    {'name': 'Peanutbot', 'attack': 5, 'health': 12},
    {'name': 'Count von Count', 'attack': 10, 'health': 30},
    {'name': 'Ernie', 'attack': 5, 'health': 12},
    {'name': 'Bert', 'attack': 5, 'health': 12},
    {'name': 'Kermit', 'attack': 5, 'health': 5},
    {'name': 'Herry the Monster', 'attack': 20, 'health': 20}
]
