"""Build a map of the school

Create a matrix of room names. It's a List of Lists of Strings [ ['name','name'], ['name','name'], ['name','name'] ]

Function build_map() will build rooms from those names.

Each room has a name and may have items and a monster when built.

school_map is built using build_map() when this module is imported into schooladventure.
"""
from room import Room


school_map = []

"""
Add new rooms to this list. You can make the list anything you like.
You could add hallways. You could map out your own school's rooms or
a school you wish you went to. You could even add rooms that have nothing to do with a school.

ROOMS is a List of Lists of Strings
"""
ROOMS = [
    ['Library',    'Cafeteria', 'Gym', 'English', 'Algebra'],
    ['Stem Lab',   'Kitchen', 'Closet', 'Principal\'s Office', 'Study Hall'],
    ['Auditorium', 'Spanish', 'Art', 'Attendance Office', 'Shop'],
    ['French',     'Chemistry', 'Physics', 'Biology', 'Health'],
    ['PE Gym',     'Closet', 'Annex', 'Economics', 'Detention']
]


def build_map():
    """ build map is called when this module is imported into schooladventure
    The global statement tells python to use the school map object outside of the
    function when making updates. If we didn't d this python would look for a local function
    version of school_map when making updates.

    Notice that we don't have global on rooms. Since we are not making updates to rooms
    we don't need global.

    Loop through rows of rooms.
    Then loop through each room in a row.
    Finally, create a Room object and add it to the school_map.
    """
    global school_map
    for x, row in enumerate(ROOMS):
        school_map.append([])
        for y, room in enumerate(ROOMS[x]):
            school_map[x].append(Room(room))


build_map()