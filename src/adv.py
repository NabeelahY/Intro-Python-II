from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':
    Room("Outside Cave Entrance", "North of you, the cave mount beckons",
         [Item('Axepick', 'digging yourself out of tunnels')]),
    'foyer':
    Room(
        "Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
        [Item('Sunglass', 'shielding your eyes from the sun\'s rays')]),
    'overlook':
    Room(
        "Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
        [Item('Binoculars', 'searching for clues in a vast area')]),
    'narrow':
    Room(
        "Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
        [Item('Gasmask', 'shielding yourself from the poisonous fumes')]),
    'treasure':
    Room(
        "Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
        [Item('Keys', 'unlocking mysteries or perhaps a treasure chest')]),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player(input('Input name: \n> '), room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
# l = room['outside'].list
# print(l[0])


def wrong_key():
    print('You\'re not allowed to move this way.')
    user_input = input('Choose another path \n>')


def pick_item():
    print_inventory()
    choice = input(
        'To pick item from this room, type "Take" and the name of the item: ')
    if choice.split(' ')[0] == 'Take':
        player_choice = choice.split(' ')[1]
        for i in player1.room.list:
            if player_choice == i.name:
                player1.get_item(i)
                player1.room.remove_item(i)
            else:
                print(f'There is no {player_choice} in {player1.room.name}')


def print_inventory():
    if len(player1.inventory) > 0:
        print(f'\nThese are the items you have in your inventory\n')
        for i in player1.inventory:
            print(f'{i}\n')
    else:
        print('You have no items in your inventory')


def drop_item():
    print_inventory()
    drop = input(
        'To drop an item in this room, type "Drop" and the name of the item: ')
    if drop.split(' ')[0] == 'Drop':
        player_choice = drop.split(' ')[1]
        for i in player1.inventory:
            if player_choice == i.name:
                player1.drop_item(i)
                player1.room.add_item(i)
            else:
                print(f'There is no {player_choice} in {player1.room.name}')


while True:
    if player1.room is not None:
        print(f'\n{player1}  \n')
        user_input = input(
            'Please input the direction you would like to go: North(n), East(e), West(w), South(s) : \n=>'
        )
        if user_input == 'q':
            print('Game end')
            break
        elif user_input == 'n':
            if player1.room.n_to is not None:
                player1.room = player1.room.n_to
            else:
                wrong_key()
        elif user_input == 'e':
            if player1.room.e_to is not None:
                player1.room = player1.room.e_to
            else:
                wrong_key()
        elif user_input == 'w':
            if player1.room.w_to is not None:
                player1.room = player1.room.w_to
            else:
                wrong_key()
        elif user_input == 's':
            if player1.room.s_to is not None:
                player1.room = player1.room.s_to
            else:
                wrong_key()
        elif user_input == 'p':
            pick_item()
        elif user_input == 'd':
            drop_item()
        elif user_input == 'i':
            print_inventory()

        else:
            print('You entered the wrong cardinal letter')
            user_input = input(
                'Please choose from the following: North(n), East(e), West(w), South(s) \n>'
            )
