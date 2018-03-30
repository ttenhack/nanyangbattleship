import random

field_size = 8
cpu_ships = 0
cpu_subm = 0

# Creating the fields for the computer's ships

above_water_cpu = []             
under_water_cpu = []
row = 0

# Defining the fields
s = "  "
e = " "
for x in range(field_size):
    if x > 9:
        e += str(x+1) + "  "
    else:
        s += " " + str(x+1) + "  "

above_water_cpu.append([s])
under_water_cpu.append([s]) # Print the playing field   

for x in range(field_size):
    above_water_cpu.append([str(x+1)] + ([" ~ "] * field_size)) # Prints the playing field
    
for x in range(field_size):
    under_water_cpu.append([str(x+1)] + ([" ~ "] * field_size))

def print_above_water_cpu(): 
    for row in above_water_cpu:
        print (" ".join(row)) # Connects the row values
        
def print_below_water_cpu():
    for row in under_water_cpu:
        print (" ".join(row))

def ship_placement_cpu(vertical, horizontal, placement): # Function that checks placement of the ship
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

def place_ships_cpu(placement):
    if placement == 0: # Place the ship either horizontal or vertical according to user input
        above_water_cpu[vertical][horizontal] = " D "
        above_water_cpu[vertical][horizontal + 1] = " D "
        above_water_cpu[vertical][horizontal + 2] = " D "
    else:
        above_water_cpu[vertical][horizontal] = " D "
        above_water_cpu[vertical + 1][horizontal] = " D "
        above_water_cpu[vertical + 2][horizontal] = " D "

def subm_placement_cpu(vertical, horizontal, placement, board):
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
        

def place_subm_cpu(placement, board):
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

# Actual placing of the submarines   

while cpu_ships < 3:
    vertical = random.randint(1,field_size) # Select random integers for the placement
    horizontal = random.randint(1,field_size)
    placement = random.randint(0,1)

    while ship_placement_cpu(vertical, horizontal, placement) == False:
        vertical = random.randint(1,field_size) # Select random integers for the placement
        horizontal = random.randint(1,field_size)
        placement = random.randint(0,1)
    else: pass
    
    place_ships_cpu(placement)
    
    cpu_ships += 1 # Add count

    print("") # Print field for user reference
    print("ABOVE WATER") 
    print_above_water_cpu()
    print("")
    print("")
    print("UNDER WATER")
    print_below_water_cpu()
else:
    pass

while cpu_subm < 3:
    vertical = random.randint(1,field_size) # Select random integers for the placement
    horizontal = random.randint(1,field_size)
    placement = random.randint(0,1)
    board = random.randint(0,1)

    while subm_placement_cpu(vertical, horizontal, placement, board) == False:
        vertical = random.randint(1,field_size) # Select random integers for the placement
        horizontal = random.randint(1,field_size)
        placement = random.randint(0,1)
        board = random.randint(0,1)
    else: pass
    
    place_subm_cpu(placement, board)
    
    cpu_subm += 1 # Add count

    print("") # Print field for user reference
    print("ABOVE WATER") 
    print_above_water_cpu()
    print("")
    print("")
    print("UNDER WATER")
    print_below_water_cpu()
else:
    pass
