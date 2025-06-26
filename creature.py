"""
define all stats
track mood based on thresholds
provide methods like:
 - feed(), give_water(), pet(), go_to_bathroom()
 - update_needs() (increases needs over time)
 - get_mood() (returns string or emoji based on current stats)
 - to_dict() / from_dict() for saving / loading
"""

class Creature():
    def __init__(self, name, hunger, thirst, bladder):
        self.name = name
        self.hunger = hunger
        self.thirst = thirst
        self.bladder = bladder
    
    def update_needs(self):
        # increase hunger, thirst, etc. over time
        pass

    def feed(self):
        # lower hunger stat
        pass

    # def give_water(self):
        # lower thirst stat
        # pass

    def go_to_bathroom(self):
        # lower bladder stat
        pass

    def pet(self):
        # increase happiness
        pass

    def get_mood(self):
        # returns mood description or emoji based on current stats
        pass

    def to_dict(self):
        # convert to dict for saving
        pass

    # @classmethod
    def from_dict(self):
        # recreates a Creature object from saved data
        pass