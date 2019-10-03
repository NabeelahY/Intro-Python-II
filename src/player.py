# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item


class Player:
    def __init__(self, name, room, inventory=None):
        self.name = name
        self.room = room
        if inventory is None:
            self.inventory = []

    def __str__(self):
        output = ''
        output += self.room.__str__()
        return output

    def get_item(self, item):
        self.inventory.append(item)
        print(
            f'\nYou took {item.name} from {self.room.name}. Its used for {item.desc}'
        )

    def drop_item(self, item):
        self.inventory.remove(item)
        print(f'\nYou dropped {item.name} in {self.room.name}')
