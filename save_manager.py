import json

"""
handles saving and loading creature state:
- check for save file on startup
- load JSON into a dict and pas it to Creature.from_dict()
- write Creature.to_dict() to JSON when saving
- optionally store last_played timestamp to simulate time passing while app is closed (suggested by ChatGPT, but I don't think I like that, lol)
"""

def load_creature(filepath):
    # load creature data from file, returns a Creature instance or None
    pass

def save_creature(creature, filepath):
    # save creature data to file
    pass
