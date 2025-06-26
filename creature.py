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
    def __init__(self, name, hunger, bathroom):
        self.name = name
        self.hunger = hunger
        self.bathroom = bathroom
    
    def update_needs(self):
        # increase hunger, thirst, etc. over time
        pass

    def feed(self):
        self.hunger = max(0, self.hunger - 20)

    def go_to_bathroom(self):
        self.bathroom = max(0, self.bathroom - 30)

    # might increase happiness
    def pet(self):
        return "The blob rumbles softly."

    def get_mood(self):
        # return "authentic" mood later
        return '^^'

    def to_dict(self):
        return {'name': self.name, 'hunger': self.hunger, 'bathroom': self.bathroom}

    @classmethod
    def from_dict(cls, data):
        return cls(name = data['name'], hunger = data['hunger'], bathroom = data['bathroom'])