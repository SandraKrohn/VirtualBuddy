import json
import os
# NEW NEW NEW NEW NEW NEW: SAVE_FILES instead of singular
from config import SAVE_FILES
from creature import Creature

# NEW NEW NEW NEW NEW NEW: added save_file as parameter, replaced SAVE_FILE with save_file (with open...),
# added "to {save_file}" in print
def save_creature(creature, save_file):
    try:
        with open(save_file, 'w') as file:
            json.dump(creature.to_dict(), file)
        print(f'Saved creature: {creature.name} to {save_file}')
    except Exception as e:
        print(f'Error saving creature: {e}')

# NEW NEW NEW NEW NEW NEW: added save_file as parameter, using it in with open and os.remove, adding it to print
def load_creature(save_file):
    try:
        with open(save_file, 'r') as f:
            content = f.read().strip()
            if not content:
                os.remove(save_file)
                raise ValueError("Save file was empty and has been deleted.")
            data = json.loads(content)
        print(f"Loaded creature from {save_file}.")
        return Creature.from_dict(data)
    
    except (FileNotFoundError, ValueError) as e:
        print(f"No valid save file found: {e}")
        return None
    
    except Exception as e:
        print(f"Error loading creature: {e}")
        return None

