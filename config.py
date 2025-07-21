"""
constants (e. g. max stat values, timer speed)
- max hunger, thirst, etc.
- stat increase rates
- update interval (e. g. every 5 seconds)
"""

# max values for stats
MAX_HUNGER = 100
MAX_BLADDER = 100
MAX_HAPPINESS = 100

# how often stats updates (mil sec)
UPDATE_INTERVAL = 1000

# stat increase rate
HUNGER_RATE = 2
BLADDER_RATE = 1
HAPPINESS_RATE = 1

# saving file path
SAVE_FILE = 'creature_save.json'