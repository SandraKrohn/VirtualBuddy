import json
import os
from config import SAVE_FILE
from creature import Creature

def save_creature(creature):
    try:
        with open(SAVE_FILE, 'w') as file:
            json.dump(creature.to_dict(), file)
        print(f'Saved creature: {creature.name}')
    except Exception as e:
        print(f'Error saving creature: {e}')


def load_creature():
    try:
        with open(SAVE_FILE, 'r') as f:
            content = f.read().strip()
            if not content:
                os.remove(SAVE_FILE)
                raise ValueError("Save file was empty and has been deleted.")
            data = json.loads(content)
        print("Loaded creature data.")
        return Creature.from_dict(data)
    
    except (FileNotFoundError, ValueError) as e:
        print(f"No valid save file found: {e}")
        return None
    
    except Exception as e:
        print(f"Error loading creature: {e}")
        return None

