# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self,
                 name,
                 desc,
                 list,
                 n_to=None,
                 s_to=None,
                 e_to=None,
                 w_to=None):
        self.name = name
        self.desc = desc
        self.list = list
        self.n_to = n_to
        self.w_to = w_to
        self.e_to = e_to
        self.s_to = s_to

    def __str__(self):
        room_details = ''
        room_details += '  ' + self.name + '\n'
        room_details += '  ' + self.desc + '\n' + '\n'
        room_details += '  ' + '***********' + ' Room items ' + '***********+' + '\n'
        if len(self.list) == 0:
            room_details = f'There are no items in {self.name}'
        for i in self.list:
            room_details += '\n' + '  ' + str(i) + '\n'
        return room_details
