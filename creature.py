from config import HUNGER_RATE, BLADDER_RATE, MAX_HUNGER, MAX_BLADDER, MAX_HAPPINESS

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
        self.happiness = MAX_HAPPINESS
    
    def update_needs(self):
        # increase needs over time
        self.hunger = min(MAX_HUNGER, self.hunger + HUNGER_RATE)
        self.bathroom = min(MAX_BLADDER, self.bathroom + BLADDER_RATE)
        self.happiness = max(0, self.happiness - 1)
    
    def get_mood_value(self):
        penalties = self.hunger * 0.7 + self.bathroom * 0.7
        mood_value = self.happiness - penalties
        return max(0, min(MAX_HAPPINESS, int(mood_value)))

    def feed(self):
        self.hunger = max(0, self.hunger - 20)

    def go_to_bathroom(self):
        self.bathroom = max(0, self.bathroom - 30)

    def pet(self):
        increase_amount = 10
        old_happiness = self.happiness
        self.happiness = min(MAX_HAPPINESS, self.happiness + increase_amount)
        print(f'Pet: happiness increased from {old_happiness} to {self.happiness}')
        return f'{self.name} rumbles softly.'

    # and is this necessary?
    def get_mood_string(self):
        # return "authentic" mood later
        return '^^'

    def to_dict(self):
        return {'name': self.name, 'hunger': self.hunger, 'bathroom': self.bathroom, 'happiness': self.happiness}

    @classmethod
    def from_dict(cls, data):
        creature = cls(data['name'], data['hunger'], data['bathroom'])
        creature.happiness = data.get('happiness', MAX_HAPPINESS)
        return creature