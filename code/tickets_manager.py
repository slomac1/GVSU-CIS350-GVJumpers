import json, os

default = {
    "tickets": 0
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

def load_tickets():
    try:
        with open(get_save_path('tickets.json'), 'r') as file:
            data = json.load(file)
    except:
        data = default
    return data["tickets"]

def save_tickets(amount):
    with open(get_save_path('tickets.json'), 'w') as file:
        json.dump({"tickets": amount}, file, indent=4)

'''
This will allow us to be able to keep track of tickets accross multiple game instances

in main file import tickets_manager

to set starting tickets(if everything is in class):
self.tickets = tickets_manager.load_tickets()

to update tickets at end of minigame:
tickets_manager.save_tickets(new amount)

'''