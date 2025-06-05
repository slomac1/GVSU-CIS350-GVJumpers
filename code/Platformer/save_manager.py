import json
from setting import *

save_file = "save.json"

default = {
    "offset_x": 0,
    "offset_y": 0,
    "p_index": 0,
    "p_rectx": WINDOW_WIDTH / 2,
    "p_recty": WINDOW_HEIGHT / 2,
    "p_health": 100
}

def load():
    try:
        with open(save_file, 'r') as file:
            data = json.load(file)
        print('Save loaded')
    except:
        print('Unable to load save, loading default')
        return default
    return data

def save(assets):
    with open(save_file, 'w') as file:
        json.dump(assets, file, indent=4)
