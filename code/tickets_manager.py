import json

ticket_file = "tickets.json"

def load_tickets():
    with open(ticket_file, 'r') as file:
        data = json.load(file)
    return data["tickets"]

def save_tickets(amount):
    with open(ticket_file, 'w') as file:
        json.dump({"tickets": amount}, file, indent=4)

'''
This will allow us to be able to keep track of tickets accross multiple game instances

in main file import tickets_manager

to set starting tickets(if everything is in class):
self.tickets = tickets_manager.load_tickets()

to update tickets at end of minigame:
tickets_manager.save_tickets(new amount)

'''