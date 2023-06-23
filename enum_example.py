from enum import Enum

class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4

def get_direction_name(value):
    for direction in Direction:
        if direction.value == value:
            return direction.name

# Main program
value = int(input("Enter an integer value representing a direction: "))
name = get_direction_name(value)
print("The corresponding direction name is:", name)