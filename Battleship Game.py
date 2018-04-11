import random
import Image

# Variables for the game
field_size = 8 # Set field size by choosing a number (e.g. 8 will provide 8x8)
attack_range = 1 # Range of cells (next to focal cell) affected when firing a missle
total_user_ships = 1 # Number of ships for the user
total_user_subms = 1 # Number of submarines for the user
total_cpu_ships = 1 # Number of ships for the CPU
total_cpu_subm = 1 # Number of submarines for the CPU
username = "" # Username of the player
opponentlist = ["Marco Polo", "Queen Elizabeth", "Thomas Raffles", "Michiel de Ruyter", "Napoleon Bonaparte", "William of Orange", "Sun Tzu"]
opponent = random.choice(opponentlist) # Name of CPU opponent

# Fields in the game
# User boards
above_water = [] # User field above water          
under_water = [] # User field under water

# CPU boards
above_water_cpu = [] # CPU field above water         
under_water_cpu = [] # CPU field under water

# User hit boards
# Stores the hits of the user on empty enemy boards
above_water_hits = [] # User hits above water         
under_water_hits = [] # User hits under water

row = 0 # ?

# Counter variables
user_ships = 0 # Ships
user_subms = 0 # Submarines
cpu_ships = 0 # CPU's ships
cpu_subm = 0 # CPU's submarines
total_hits = (total_user_ships + total_user_subms) * 3 # Number of positions to be hit by the CPU
total_cpu_hits = (total_cpu_ships + total_cpu_subm) * 3 # Number of positions to be hit by the USER

# Defining the functions of the game

def clean_screen():
    """Clean screen for next move in the game."""
    print("\n" * 70)

def start_game():
    print("""\nWelcome to Nanyang Battelship+ Destroyer!
Ready to conquer the seas and achieve victory?""")
    
    image = Image.open('images/')
    image.show()

    try:
        global game_info
        game_info = int(input("\nPress [0] to start a game, or [1] to receive game play instructions: "))
        return game_info
    except ValueError:
        print("This is an invalid input. Please try again!")
        start_game()

def game_instructions(game_info): # Check if the value is correctly entered (either 0 or 1)
    if game_info > 1:
        print("This is an invalid input. Please try again!")
        start_game()

    if game_info == 1:
            print("""\n

GOAL OF THE GAME
In this game, you will fight against enemies around the globe.
The goal of Nanyang Battleship+ Destroyer is to sink all the enemy ships by targeting missles.

BEFORE THE GAME
Before starting the game, you will be provided with two fields: surface and subsea.
You are requested to place a boat and a submarine on the fields. The boat can only be placed
on the surface, whilst the submarine can be placed on both fields.

PLACEMENT OF THE SHIPS
To place a ship, you need to provide both a vertical and horizontal coordinate on the field.
The ships are 3 units long, meaning that the boat will be placed on the two following fields.
The placement of these subsequent fields is dependent on the placement: horizontal or vertical.
For example, placing the boat on vertical: 3, horizontal: 3, placement: vertical, results in
the following placements: (3,3), (4,3) and (5,3).

ATTACKING THE OPPONENT
After placing the boats, you need to provide attack coordinates. These coordinates will be
targeted on the enemies' ships. The enemy has the following amount of boats on the board:
ships ({}) and submarines ({}).

By providing attack coordinates, the fields in a range of {} will also be hit.""".format(total_cpu_ships,total_cpu_subm,attack_range))

    else:
        pass

# Function that retrieves the username
def get_username():
    """ Request the username from the user. """
    global username
    clean_screen()
    print("\nGET STARTED WITH A USERNAME")
    username = str(input("Provide your username: "))
    clean_screen()

def create_boards():
    """ The function creates the fields for the game. """
    
    # Numerize the fields horizontally
    s = "  "
    for i in range(field_size):
        if i > 9:
            s += str(i+1) + "  "
        else:
            s += " " + str(i+1) + "  "

    # Append the horizontal numerization to the fields
    above_water.append([s])
    under_water.append([s])
    above_water_cpu.append([s])
    under_water_cpu.append([s])
    above_water_hits.append([s])
    under_water_hits.append([s]) 

    # Create the content of the fields
    for x in range(field_size):
        above_water.append([str(x+1)] + ([" ~ "] * field_size))
        
    for x in range(field_size):
        under_water.append([str(x+1)] + ([" ~ "] * field_size))

    for x in range(field_size):
        above_water_cpu.append([str(x+1)] + ([" ~ "] * field_size))
    
    for x in range(field_size):
        under_water_cpu.append([str(x+1)] + ([" ~ "] * field_size))

    for x in range(field_size):
        above_water_hits.append([str(x+1)] + ([" ~ "] * field_size))
    
    for x in range(field_size):
        under_water_hits.append([str(x+1)] + ([" ~ "] * field_size))

# The following functions print the fields during the game

def print_user_boards():
    """ The function prints both the above and under water fields of the user."""

    print("\nSURFACE {} \n".format(str.upper(username)))
    
    for row in above_water:
        print (" ".join(row)) # Connects the row values

    print("\n\nSUBSEA {} \n".format(str.upper(username)))
    
    for row in under_water:
        print (" ".join(row))

def print_user_hit_boards():
    """ The function prints the boards that show the hits on the enemy boards by the user."""

    print("\nSURFACE {} [CPU] \n".format(str.upper(opponent))) # Print the user's playing fields for game initialization

    for row in above_water_hits:
        print (" ".join(row))

    print("\n\nSUBSEA {} [CPU] \n".format(str.upper(opponent)))

    for row in under_water_hits:
        print(" ".join(row))


# Functions for placing the ships of user and CPU

def ship_placement_check(vertical, horizontal, placement): # Function for the placement of the ships

    if (vertical < 1 or vertical > field_size) or (horizontal < 1 or horizontal > field_size): # Check input of coordinates
        return False
    else:
        pass

    if placement == 0 or placement == 1:
        if (placement == 0) and (horizontal + 2 > field_size): # Check if parts of the boat cannot be placed on the board (size = 3)
            return False
            
        elif (placement == 1) and (vertical + 2 > field_size):
            return False
        else:
            pass
    else:
        return False

    # Check if a boat is already placed on one of the selected coordinates
    if placement == 0:
        if above_water[vertical][horizontal] == " D " or above_water[vertical][horizontal + 1] == " D " or above_water[vertical][horizontal + 2] == " D ":
            return False
        else:
            pass

    if placement == 1:
        if above_water[vertical][horizontal] == " D " or above_water[vertical + 1][horizontal] == " D " or above_water[vertical + 2][horizontal] == " D ":
            return False
        else:
            pass

def place_ships(vertical, horizontal, placement):
    if placement == 0: # Place the ship either horizontal or vertical according to user input
        above_water[vertical][horizontal] = " D "
        above_water[vertical][horizontal + 1] = " D "
        above_water[vertical][horizontal + 2] = " D "
    else:
        above_water[vertical][horizontal] = " D "
        above_water[vertical + 1][horizontal] = " D "
        above_water[vertical + 2][horizontal] = " D "

def ship_placement():
    global user_ships
    global total_user_ships
    
    while user_ships < total_user_ships:
        print("\nPlace a ship by entering the coordinates. You have {} in total.\n".format(total_user_ships))
        vertical = int(input("Provide vertical coordinate: "))
        horizontal = int(input("Provide horizontal coordinate: "))
        placement = int(input("Horizontal [0] or vertical [1] placement: "))

        while ship_placement_check(vertical, horizontal, placement) == False: # Check if the placement is correct
            print("\nThe placement is incorrect. Please provide new coordinates.\n")
            vertical = int(input("Provide vertical coordinate: "))
            horizontal = int(input("Provide horizontal coordinate: "))
            placement = int(input("Horizontal [0] or vertical [1] placement: "))
    
        place_ships(vertical, horizontal, placement)
        user_ships += 1 # Add count

        clean_screen()
        print_user_boards() # Prints the field for user reference

    else:
        pass

def subm_placement_check(vertical, horizontal, placement, board):

    if (vertical < 1 or vertical > field_size) or (horizontal < 1 or horizontal > field_size): # Check input of coordinates
        return False
    else:
        pass
    
    if (placement == 0) or (placement == 1) and (board == 0) or (board ==1): # Check input of submarine placement
        while (placement == 0) and (horizontal + 2 > field_size): # Check if parts of the boat cannot be placed on the board (size = 3)
            return False
        if (placement == 1) and (vertical + 2 > field_size):
            return False
        else:
            pass
    else:
        return False

def place_subms(vertical, horizontal, placement, board):
    if placement == 0 and board == 0:
        above_water[vertical][horizontal] = " S "
        above_water[vertical][horizontal + 1] = " S "
        above_water[vertical][horizontal + 2] = " S "
    elif placement == 1 and board == 0:
        above_water[vertical][horizontal] = " S "
        above_water[vertical + 1][horizontal] = " S "
        above_water[vertical + 2][horizontal] = " S "
    elif placement == 0 and board == 1:
        under_water[vertical][horizontal] = " S "
        under_water[vertical][horizontal + 1] = " S "
        under_water[vertical][horizontal + 2] = " S "
    else:
        under_water[vertical][horizontal] = " S "
        under_water[vertical + 1][horizontal] = " S "
        under_water[vertical + 2][horizontal] = " S "
       
def subm_placement():
    global user_subms
    global total_user_subms
    
    while user_subms < total_user_subms:
        print("\nPlace a submarine by entering the coordinates. You have {} in total.\n".format(total_user_subms))
        vertical = int(input("Provide vertical coordinate: "))
        horizontal = int(input("Provide horizontal coordinate: "))
        placement = int(input("Horizontal [0] or vertical [1] alignment: "))
        board = int(input("Above sea [0] or under sea [1]: "))

        while subm_placement_check(vertical, horizontal, placement, board) == False:
            print("\nThe placement is incorrect. Please provide new coordinates.\n")
            vertical = int(input("Provide vertical coordinate: "))
            horizontal = int(input("Provide horizontal coordinate: "))
            placement = int(input("Horizontal [0] or vertical [1] alignment: "))
            board = int(input("Above sea [0] or under sea [1]: "))

        place_subms(vertical, horizontal, placement, board)
        user_subms += 1 # Add count

        clean_screen()
        print_user_boards() # Prints the field for user reference
        
    else:
        input("\nPress [Enter] for the placement of the opponent...") # User presses enter to continue with CPU placement

def ship_placement_cpu_check(vertical, horizontal, placement):
    """ Function that checks placement of the ship. """
    if (placement == 0) and (horizontal + 2 > field_size): # Check if parts of the boat cannot be placed on the board (size = 3)
        return False
    elif (placement == 1) and (vertical + 2 > field_size): # Try new random integers
        return False
    else:
        pass

    if placement == 0: # Check if there is already a boat on the coordinates (horizontal placement)
        if above_water_cpu[vertical][horizontal] == " D " or above_water_cpu[vertical][horizontal + 1] == " D " or above_water_cpu[vertical][horizontal + 2] == " D ":
            return False
        else:
            pass

    if placement == 1: # Check if there is already a boat on the coordinates (vertical placement)
        if above_water_cpu[vertical][horizontal] == " D " or above_water_cpu[vertical + 1][horizontal] == " D " or above_water_cpu[vertical + 2][horizontal] == " D ":
            return False
        else:
            pass

def subm_placement_cpu_check(vertical, horizontal, placement, board):
    if placement == 0 and horizontal + 2 > field_size: # Check if parts of the boat cannot be placed on the board (size = 3)
        return False
    elif placement == 1 and vertical + 2 > field_size:
        return False
    else:
        pass
    
    if placement == 0 and board == 0: # Check if there is a boat or submarine present on the places
        if above_water_cpu[vertical][horizontal] == " D " or above_water_cpu[vertical][horizontal + 1] == " D " or above_water_cpu[vertical][horizontal + 2] == " D " or above_water_cpu[vertical][horizontal] == " S " or above_water_cpu[vertical][horizontal +1] == " S " or above_water_cpu[vertical][horizontal + 2] == " S ":
            return False
        else:
            pass

    if placement == 1 and board == 0: 
        if above_water_cpu[vertical][horizontal] == " D " or above_water_cpu[vertical + 1][horizontal] == " D " or above_water_cpu[vertical + 2][horizontal] == " D " or above_water_cpu[vertical][horizontal] == " S " or above_water_cpu[vertical + 1][horizontal] == " S " or above_water_cpu[vertical + 2][horizontal] == " S ":
            return False
        else:
            pass

    if placement == 0 and board == 1: # Check if there is a submarine present on the places
        if under_water_cpu[vertical][horizontal] == " S " or under_water_cpu[vertical][horizontal +1] == " S " or under_water_cpu[vertical][horizontal + 2] == " S ":
            return False
        else:
            pass

    if placement == 1 and board == 1: 
        if under_water_cpu[vertical][horizontal] == " S " or under_water_cpu[vertical + 1][horizontal] == " S " or under_water_cpu[vertical + 2][horizontal] == " S ":
            return False
        else:
            pass       

def place_ships_cpu(vertical, horizontal, placement):
    if placement == 0: # Place the ship either horizontal or vertical according to user input
        above_water_cpu[vertical][horizontal] = " D "
        above_water_cpu[vertical][horizontal + 1] = " D "
        above_water_cpu[vertical][horizontal + 2] = " D "
    else:
        above_water_cpu[vertical][horizontal] = " D "
        above_water_cpu[vertical + 1][horizontal] = " D "
        above_water_cpu[vertical + 2][horizontal] = " D "

def place_subm_cpu(vertical, horizontal, placement, board):
    if placement == 0 and board == 0:
        above_water_cpu[vertical][horizontal] = " S "
        above_water_cpu[vertical][horizontal + 1] = " S "
        above_water_cpu[vertical][horizontal + 2] = " S "
    elif placement == 1 and board == 0:
        above_water_cpu[vertical][horizontal] = " S "
        above_water_cpu[vertical + 1][horizontal] = " S "
        above_water_cpu[vertical + 2][horizontal] = " S "
    elif placement == 0 and board == 1:
        under_water_cpu[vertical][horizontal] = " S "
        under_water_cpu[vertical][horizontal + 1] = " S "
        under_water_cpu[vertical][horizontal + 2] = " S "
    else:
        under_water_cpu[vertical][horizontal] = " S "
        under_water_cpu[vertical + 1][horizontal] = " S "
        under_water_cpu[vertical + 2][horizontal] = " S "

def ship_placement_cpu():
    global cpu_ships
    global total_cpu_ships
    
    clean_screen()
    print("\nThe opponent, {}, is currently placing the ships...".format(opponent))
    
    while cpu_ships < total_cpu_ships:
        vertical = random.randint(1,field_size) # Select random integers for the placement
        horizontal = random.randint(1,field_size)
        placement = random.randint(0,1)

        while ship_placement_cpu_check(vertical, horizontal, placement) == False:
            vertical = random.randint(1,field_size) # Select random integers for the placement
            horizontal = random.randint(1,field_size)
            placement = random.randint(0,1)
        else:
            pass
    
        place_ships_cpu(vertical, horizontal, placement)
        cpu_ships += 1 # Add count

    else:
        pass

def subm_placement_cpu():
    global cpu_subm
    global total_cpu_subm
    
    while cpu_subm < total_cpu_subm:
        vertical = random.randint(1,field_size) # Select random integers for the placement
        horizontal = random.randint(1,field_size)
        placement = random.randint(0,1)
        board = random.randint(0,1)

        while subm_placement_cpu_check(vertical, horizontal, placement, board) == False:
            vertical = random.randint(1,field_size) # Select random integers for the placement
            horizontal = random.randint(1,field_size)
            placement = random.randint(0,1)
            board = random.randint(0,1)
        else: pass
    
        place_subm_cpu(vertical, horizontal, placement, board)
        cpu_subm += 1 # Add count

    else:
        print("\n{} placed the ships. Get ready to fight!".format(opponent)) # Inform user that the boats by the CPU are placed


# The following functions are made for the game play
def hit_boat(horizontal, vertical, board, attack_range):
    """ Function that checks if a boat is hit. """

    attack_list = gen_attack_field(horizontal, vertical, attack_range)
    global total_cpu_hits

    for pos in attack_list:
        if (pos[0] >= 1 and pos[1] >= 1) and (pos[1] <= field_size and pos[0] <= field_size):
            if board == 0:
                if above_water_cpu[pos[0]][pos[1]] == " D " or above_water_cpu[pos[0]][pos[1]] == " S ":
                    print("\nBOOM!")
                    above_water_cpu[pos[0]][pos[1]] = " H "
                    above_water_hits[pos[0]][pos[1]] = " H "
                    total_cpu_hits -= 1
                elif above_water_cpu[pos[0]][pos[1]] == " H ":
                    pass
                else:
                    above_water_cpu[pos[0]][pos[1]] = " X "
                    above_water_hits[pos[0]][pos[1]] = " X "
            elif board == 1:
                if under_water_cpu[pos[0]][pos[1]] == " D " or under_water_cpu[pos[0]][pos[1]] == " S ":
                    print("\nBOOM!")
                    under_water_cpu[pos[0]][pos[1]] = " H "
                    under_water_hits[pos[0]][pos[1]] = " H "
                    total_cpu_hits -= 1
                elif under_water_cpu[pos[0]][pos[1]] == " H ":
                    pass
                else:
                    under_water_cpu[pos[0]][pos[1]] = " X "
                    under_water_hits[pos[0]][pos[1]] = " X "

def hit_boat_cpu(horizontal, vertical, board, attack_range):
    """ Checks if a boat is hit. """
    
    attack_list = gen_attack_field(horizontal, vertical, attack_range)
    global total_hits

    for pos in attack_list:
        if (pos[0] >= 1 and pos[1] >= 1) and (pos[1] <= field_size and pos[0] <= field_size):
            if board == 0:
                if above_water[pos[0]][pos[1]] == " D " or above_water[pos[0]][pos[1]] == " S ":
                    print("\nYour were hit!")
                    above_water[pos[0]][pos[1]] = " H "
                    total_hits -= 1
                elif above_water[pos[0]][pos[1]] == " H ":
                    pass
                else:
                    above_water[pos[0]][pos[1]] = " X "
            elif board == 1:
                if under_water[pos[0]][pos[1]] == " D " or under_water[pos[0]][pos[1]] == " S ":
                    print("\nYour were hit!")
                    under_water[pos[0]][pos[1]] = " H "
                    total_hits -= 1
                elif under_water[pos[0]][pos[1]] == " H ":
                    pass
                else:
                    under_water[pos[0]][pos[1]] = " X "

def gen_attack_field(horizontal, vertical, attack_range):
    """ Generates the attack range field. """
    attack_list = []
    rowoffset = horizontal - attack_range
    coloffset = vertical - attack_range

    for x in range(2 * attack_range + 1):
        for y in range(2 * attack_range + 1):
            attack_list.append([x + rowoffset, y + coloffset])

    return attack_list


def ship_hit_check(vertical, horizontal):
    """ Function for the placement of the ships. """

    if (vertical < 1 or vertical > field_size) or (horizontal < 1 or horizontal > field_size): # Check input of coordinates
        return False
    else:
        pass

def game_play():
    """ The actual shooting of ships. """
    while total_hits > 0 or total_cpu_hits > 0:

        # USER
        print_user_hit_boards() # Print the enemy fields

        print("\nInsert attack coordinates to fire a missle on {}.".format(opponent))
        vertical = int(input("\nProvide vertical missle coordinate: "))
        horizontal = int(input("Provide horizontal missle coordinate: "))
        board = int(input("Above [0] or under water [1]: "))

        while ship_hit_check(vertical, horizontal) == False:
            print("\nThe placement is incorrect. Please provide new coordinates.")
            vertical = int(input("\nProvide vertical missle coordinate: "))
            horizontal = int(input("Provide horizontal missle coordinate: "))
            board = int(input("Above [0] or under water [1]: "))

        hit_boat(vertical, horizontal, board, attack_range)
        print_user_hit_boards() # Print the enemy fields

        if total_cpu_hits == 0:
            print("\nVICTORY IS YOURS, {}!".format(str.upper(username)))
            break

        print("\nEnemy fields left:", total_cpu_hits)
        
        input("\nPress [Enter] for the next turn...")
        clean_screen()
        
        # CPU
        vertical = random.randint(1,field_size)
        horizontal = random.randint(1,field_size)
        board = random.randint(0,1)

        while ship_hit_check(vertical, horizontal) == False:
            vertical = random.randint(1,field_size)
            horizontal = random.randint(1,field_size)
            board = random.randint(0,1)

        hit_boat_cpu(vertical, horizontal, board, attack_range)

        print_user_boards()
        
        if total_hits == 0:
            print("\nYOU LOST {}!".format(username))
            break

        # Share the board being attacked by the CPU
        if board == 1:
            show_board = "Subsea"
        else:
            show_board = "Surface"

        print("") # Needed since variable below otherwise creates a blankspace before printing
        print("{} fired a missle on the following coordinates:".format(opponent))
        print("\nVertical: [{}] Horizontal: [{}] Location: [{}]".format(vertical, horizontal,show_board))
        print("\nFields left:", total_hits)
        
        input("\nPress [Enter] for the next turn...")
        clean_screen()

def play_game():
    start_game() # Welcomes user and asks for instructions
    game_instructions(game_info) # When requested, provide instructions
    get_username() # Request the username from the user
    create_boards() # Create the playing fields of the user
    print_user_boards() # Print the boards for the user reference

    # Placement of the ships
    ship_placement()
    subm_placement()
    ship_placement_cpu()
    subm_placement_cpu()

    # Playing the game
    game_play()
    
play_game()
