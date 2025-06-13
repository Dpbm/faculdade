# from 

# http://christianthompson.com
# Twitter: @tokyoedtech

# Welcome to my "office hours" for October 10, 2019.
# If you have any Python questions - ask in chat
# Please provide any code via pastebin.com link

# OS: Ubuntu Linux 19.04
# Programming Editor: Geany

# Link to Explanation Video on YouTube: https://www.youtube.com/watch?v=5JuslgfVoFY

class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []

class Player(object):
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inventory = []

class Item(object):
    def __init__(self, name, description, is_movable):
        self.name = name
        self.description = description
        self.is_movable = is_movable

# Create items
# Closet Items
shelf = Item("shelf", "The shelf is empty.", False)
uniform = Item("uniform", "The uniform is blue and drab.", True)
        
# Control Room Items
guard = Item("guard", "The guard looks mean and menacing.", False)
electronic_lock = Item("lock", "The lock is in front of a large door to the east.", "False")
id = Item("id", "The id is silver with a barcode on it.", True)

# Airlock Items
spacesuit = Item("spacesuit", "The spacesuit looks old, but safe.", True)
button = Item("button", "The big red button has a warning symbol on it.", False)

# Create Rooms
# Closet
closet = Room("The Closet", "You are in a small nondescript closet.")
closet.items.append(shelf)
closet.items.append(uniform)

# Control Room
control_room = Room("The Control Room", "You are in a small room that looks like it controls something. There is an airlock to the east.")
control_room.items.append(guard)
control_room.items.append(electronic_lock)
control_room.items.append(id)

# Airlock
airlock = Room("The Airlock", "You are in a small room that is clearly an airlock. There is a window to space in the east. There is an airlock door to the west.")
airlock.items.append(spacesuit)
airlock.items.append(button)

# Create exits
closet.exits["n"]= control_room
control_room.exits["s"] = closet
airlock.exits["w"] = control_room

# Create the player
player = Player("The Player", closet)


started = False

def play(command):
    output = ""
    status = 0

    global started

    if not started:
        output += "Welcome to My Space Adventure\n"
        output += "You wake up on a space station.\n"
        started = True
    
    output += "\n"
    output += player.location.name + "\n"
    output += player.location.description + "\n"
    output += "Here are the exits: \n"
    for exit_loc in player.location.exits:
        output += exit_loc+"\n"
    output += "You see the following: \n"
    for item in player.location.items:
        output += item.name + "\n"
        
    words = command.split()
    verb, noun = '', ''
    if len(words) > 0:
        verb = words[0]
    if len(words) > 1:
        noun = words[1]
    
    if verb == "examine":
        for item in player.location.items:
            if item.name == noun:
                output += item.description + "\n"
        for item in player.inventory:
            if item.name == noun:
                output += item.description + "\n"

    if verb == "get":
        for item in player.location.items:
            if item.name == noun:
                if item.is_movable:
                    output += "You take the {}\n".format(item.name)
                    player.location.items.remove(item)
                    player.inventory.append(item)
                
                else:
                    output += "Sorry, you can't move that.\n"

    if verb == "drop":
       for item in player.inventory:
            output += "You drop the {}.\n".format(item.name)
            player.inventory.remove(item)
            player.location.items.append(item)
        
    if verb in ["inv", "inventory"]:
        output += "You have the following: \n"
        for item in player.inventory:
            output += item.name + "\n"

    if verb in ["n", "s", "e", "w", "u", "d"]:
        if verb in player.location.exits:
            player.location = player.location.exits[verb]
            output += "You go {} and find yourself in a new room.\n".format(verb)
            

    # Room specific code
    # Control Room
    if player.location == control_room:
        if uniform not in player.inventory:
            output += "The guard sees you. Without saying a word, he pulls his laser gun and kills you. Game over.\n"
            status = 1
        else:
            output += "The guard looks up, looks at the uniform, and turns his head back to the display.\n"

    if player.location == control_room:
        if verb == "open" and noun == "airlock":
            if id in player.inventory:
                output += "You swipe the id and the airlock opens.\n"
                control_room.exits["e"] = airlock
                
            else:
                output += "The airlock won't open. You must need some id to open it.\n"

    # Airlock
    if player.location == airlock:
        if "w" in airlock.exits:
            del(airlock.exits["w"])
            output += "The airlock door closes! You are trapped.  There is no lock on this side.\n"
            
    if player.location == airlock:
        if verb == "press" and noun == "button":
            if spacesuit in player.inventory:
                output += "You put on the spacesuit and push the red button.\n"
                output += "The outer airlock door opens!\n"
            else:
                output += "The outer airlock door opens.  You are sucked into the vacuum of space and die.\n"
                status = 1

    return output, status            
