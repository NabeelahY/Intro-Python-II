from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':
    Room("Outside Cave Entrance", "North of you, the cave mount beckons",
         [Item('Axepick', 'Dig yourself out of tunnels')]),
    'foyer':
    Room(
        "Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
        [Item('Sunglass', 'Shield your eyes from the sun\'s rays')]),
    'overlook':
    Room(
        "Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
        [Item('Binoculars', 'Search for clues in a vast area')]),
    'narrow':
    Room(
        "Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
        [Item('Gasmask', 'Shield yourself from the poisonous fumes')]),
    'treasure':
    Room(
        "Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
        [Item('Keys', 'Unlock mysteries or perhaps a treasure chest')]),
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
                print('You\'re not allowed to move this way.')
                user_input = input('Choose another path \n>')
        elif user_input == 'e':
            if player1.room.e_to is not None:
                player1.room = player1.room.e_to
            else:
                print('You\'re not allowed to move this way.')
                user_input = input('Choose another path \n>')
        elif user_input == 'w':
            if player1.room.w_to is not None:
                player1.room = player1.room.w_to
            else:
                print('You\'re not allowed to move this way.')
                user_input = input('Choose another path \n>')
        elif user_input == 's':
            if player1.room.s_to is not None:
                player1.room = player1.room.s_to
            else:
                print('You\'re not allowed to move this way.')
                user_input = input('Choose another path \n>')
        else:
            print('You entered the wrong cardinal letter')
            user_input = input(
                'Please choose from the following: North(n), East(e), West(w), South(s) \n>'
            )
