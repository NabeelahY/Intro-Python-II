# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, desc, n_to=None, s_to=None, e_to=None, w_to=None):
        self.name = name
        self.desc = desc
        self.n_to = n_to
        self.w_to = w_to
        self.e_to = e_to
        self.s_to = s_to

