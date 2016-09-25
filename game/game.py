"""Where everything begins.

The player is created and the map is imported.
The game loop starts and only ends if the player chooses to quit.

"""
import time

from game.gamemap import school_map
from game.player import Player
from logit import logit


def start():
    """Where everything gets kicked off

    Look at the bottom of this module to see where start() is called.

    Create the player and start the command loop.
    Only end if do_command returns False
    """
    print('\n\nWelcome to school !!! OooohhhooooOOOhhh! (act scared)\n')
    player_name = input('What is your name? ')
    player = Player(player_name)

    look_around(player)

    keep_going = True
    while keep_going:
        keep_going = do_command(player)


def do_command(player):
    """Get a command and do something.

    1. Get a command from the player.
    2. If the command is found, pull any other data need for the command from the sentence.
    3. Call the command function.

    If a command is not found 'else' then show an error.
    If the command sentence is incomplete an exception is thrown 'except' and an error is shown.
    """
    sentence = input('\nHey %s, what do you want to do? ' % player.name).lower()
    command = sentence.split(' ')[0]
    try:
        if command == 'help':
            get_help()
        elif command == 'quit':
            health(player)
            print('bye ', player.name)
            return False
        elif command == 'attack':
            item_name = sentence.split(' ')[2]
            attack(player, item_name)
        elif command == 'go':
            direction = sentence.split(' ')[1]
            go(player, direction)
        elif command == 'where':
            where_am_i(player)
        elif command == 'look':
            look_around(player)
        elif command == 'take':
            item_name = sentence.split(' ')[1]
            take(player, item_name)
        elif command == 'health':
            health(player)
        elif command == 'dude':
            dude()
        elif command == 'gary':
            gary()
        elif command == "eat":
            item_name = sentence.split(' ')[1]
            eat(player, item_name)
        else:
            print('\n%s\'s brain sez, "I don\'t understand - %s"\n' % (player.name, sentence))
            get_help()

    except Exception as e:
        print(str(e))
        print('\n%s\'s brain sez, "I don\'t understand - %s"\n' % (player.name, sentence))
        get_help()
    return True


def dude():
    """dude
    You can add your own funny commands.
    Just create a function and call it from the do_command() if statement
    """
    return "I know what dude I am! I'm the dude, playing a dude, disguised as another dude!"


def gary():
    """gary
    Another funny command.
    """
    return "Gary? Gary? pfpfpfpfppff    pfpfpfpfppff Gary? Guys, I can't find Gary."


def get_help():
    """help
    Add commands to this or leave them off to make them secret.
    """
    return ("Welcome to Memphis. Home of the Tigers. Land of the chicken strip. See the help card for assistance.", """"

Your commands are:

  help                 'help'                 Print this stuff.
  quit                 'quit'                 Leave game.
  attack with item     'attack with spoon'    Any item may be used in an attack. Some are better than others.
  go direction         'go east'              You may not travel into the abyss.
  where am i           'where am it'          Display current room position. You may enter just 'where'.
  look around          'look around'          Displays it all including room names surrounding you.
  take item            'take spoon'           Pick up an item. Carried items may be used in attacks.
  health               'health'               Displays your player current stats.

  """)


def attack(player, item_name):
    """attack with item
    Make sure the player has the item.
    Make sure that a live monster is in the room.
    Deduct monster health by the attack value on the item.
    Counter attack by the monster does the same to the player.
    If the monster health < 1 then it is dead.
    If the player's health is < 1 then the player becomes a zombie.

    OPPORTUNITY:
      add the amount of health points deducted from the monster during attack to player.points
      so player.points += item['attack']
      see player module for other changes needed
    """
    attack_status = "There was no attack. Either you don\'t have a %s or there is no monster." % item_name
    attack_progress = ""
    player_room = school_map[player.location[0]][player.location[1]]

    for index, item in enumerate(player.items):
        if item_name == item['name'] and (school_map[player.location[0]][player.location[1]].monster['health'] > 0 or
                                                  item['attack'] < 0):
            attack_progress += "%s shall feel the wrath of your %s.  " % (
                player_room.monster['name'], item['name'])
            if item['attack'] < 5:
                attack_progress += "You know, %s is not a very effective weapon. " % item['name']

            attack_progress += 'ATTACKING %s WITH YOUR %s! ' % (player_room.monster['name'], item['name'])

            player_room.monster['health'] -= item['attack']

            # HERE is where you would increase the player points with the item attack points
            player.points += item['attack']

            if player_room.monster['health'] > 0:
                attack_progress += "%s's health is now %d." % (player_room.monster['name'],
                                                               player_room.monster['health'])
                attack_progress += "\n%s counter attacks NOW!\n " % player_room.monster['name']

                attack_progress += 'ATTACKING!'

                player.health -= player_room.monster['attack']
                attack_progress += "You lose %d health points. Your health is now %d." % (
                player_room.monster['attack'], player.health)
                if player.health < 1:
                    player.name = 'Zombie ' + player.name
                    attack_progress += "%s, you are now a zombie!" % player.name
                if player.health <= 10:
                    attack_progress += "%s, your health is quite low!" % player.name
            else:
                attack_progress += "\n%s is now dead. Long live %s!" % (player_room.monster['name'], player.name)
            attack_status = "Attack complete."
            break

    return attack_progress + " " + attack_status


def go(player, direction):
    """go direction
    Player can travel north, south, east or west.
    Player may not go off the map...abyss.
    """
    go_progress = ""
    x, y = player.location
    save_x, save_y = player.location
    try:
        if direction == 'north':
            x -= 1
        elif direction == 'south':
            x += 1
        elif direction == 'east':
            y += 1
        elif direction == 'west':
            y -= 1
        else:
            go_progress += 'Try north, south, east, or west. '

        if x >= len(school_map) or x < 0 or y >= len(school_map[x]) or y < 0:
            go_progress += '%s\'s brain sez, "Huh, I can\'t let you go there. That\'s the abyss." ' % player.name
        else:
            player.location[0] = x
            player.location[1] = y

        go_progress += look_around(player)
    except Exception as e:
        logit(str(e), 'ERROR')
        player.location[0] = save_x
        player.location[1] = save_y
        go_progress = 'I think you just tried to jump into the abyss.'
    return go_progress


def where_am_i(player):
    """where am i
    List the details of the current room.
    """
    return school_map[player.location[0]][player.location[1]].get_description()


def look_direction(location, direction):
    """Not a command. returns the name of the room in the direction related to the players current location."""
    room = ''
    try:
        x, y = location
        if direction == 'north':
            x -= 1
        elif direction == 'south':
            x += 1
        elif direction == 'east':
            y += 1
        elif direction == 'west':
            y -= 1

        if x > len(school_map) or x < 0 or y > len(school_map[x]) or y < 0:
            room = 'the abyss'
        else:
            room = school_map[x][y].name
    except:
        room = 'the abyss'

    return "To the %s is %s." % (direction, room)


def look_around(player):
    """look around
    List the current room description and list the names of all the rooms around the player.
    """
    my_space = "%s %s %s %s %s"
    return my_space % (
        school_map[player.location[0]][player.location[1]].get_description(),
        look_direction(player.location, 'north'),
        look_direction(player.location, 'east'),
        look_direction(player.location, 'south'),
        look_direction(player.location, 'west'))


def take(player, item_name):
    """take item
    Make sure the item is in the room. If it is add to the player items and remove it from the room.
    """
    take_progress = ""
    found = False
    player_room = school_map[player.location[0]][player.location[1]]
    for index, item in enumerate(player_room.items):
        if item_name == item['name']:
            player.items.append(item)
            del player_room.items[index]
            found = True
            break
    if found:
        take_progress += "The %s is yours." % item_name
    else:
        take_progress += "There is no %s in %s." % (item_name, player_room.name)
    return take_progress


def health(player):
    """health
    Show the players name, health and items.
    """
    return player.get_description()


def eat(player, item_name):
    """eat an item to add to player's health
    Some items may deduct health.
    """
    # look at each item in player.items
    # by iterating through all items in player.items
    # then use an if statement to check for item_name == item['name']
    # if found then add item['health'] to player.health and
    # print some clever message and finally
    # break to end call
    eat_progress = ""
    for index, item in enumerate(player.items):
        if item_name == item['name']:
            player.health = player.health + item['health']
            del player.items[index]
            if 0 < item['health'] < 5:
                eat_progress += 'A %s does not taste good.\n' % item['name']
            elif item['health'] <= 0:
                eat_progress += 'A %s hurts you.\n' % item['name']
            else:
                eat_progress += 'A %s helps.\n' % item['name']
            eat_progress += health(player)
            break
    return eat_progress


# this module is only named __main__ if called using python schooladventure.py
if __name__ == '__main__':
    start()
