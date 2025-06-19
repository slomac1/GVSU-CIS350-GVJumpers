import json, os
from .setting import *

default = {
    "offset_x": 0,
    "offset_y": 0,
    "p_index": 0,
    "p_rectx": WINDOW_WIDTH / 2,
    "p_recty": WINDOW_HEIGHT / 2,
    "p_health": 100
}

''' 
Used chatGPT for this the get_save_path. Was able to have it work with a straight path for load and save tickets.
But needed something more advanded in order to create the executable.
'''

def get_save_path(filename):
    # Use user's Documents folder or AppData
    save_dir = os.path.join(os.path.expanduser("~"), "JumperSaveData")
    os.makedirs(save_dir, exist_ok=True)
    return os.path.join(save_dir, filename)

def load():
    try:
        with open(get_save_path("save.json"), 'r') as file:
            data = json.load(file)
    except:
        return default
    return data

def save(assets):
    if assets == None:
        assets = default
    with open(get_save_path("save.json"), 'w') as file:
        json.dump(assets, file, indent=4)
