import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__)))
import ship


def field_to_str(ships):
    """
    (arr of tuples) -> (string)
    Convert battle field with ships to string
    Return: string
    """
    field_str = ""
    for i in range(10):
        for j in range(10):
            if (i, j) in ships:
                field_str += "*"
            else:
                field_str += " "
        field_str += "\n"
    return field_str


def show_field(ships):
    """
    (arr of tuples) -> None
    Print battle field with ships to string
    Return: None
    """
    print(field_to_str(ships))


def generate_field():
    """
    () -> None
    Fuction, which start generate field algorithm 
    Return: None
    """
    ships = []
    data = [(x, y) for x in range(10) for y in range(10)]
    ships = ship.setup_ships(data, ships)
    return ships


def read_field(file):
    """
    (string) -> (array of tuples) 
    Get field from file
    Return: field
    """
    ships = []
    with open(file + ".txt", "r") as fl:
        text = fl.read().split("\n")
    for i1, row in enumerate(text):
        for i2, ch in enumerate(row):
            if ch == '*':
                ships.append((i1, i2))
    return ships


def delete_not_empty_fields(coords, increase, data, size):
    """
    (tuple, tuple, arr of tuples, int) -> (arr of tuples) 
    Get coords and direction, size to increase and delete all surrounded elems from data
    Return: updated field
    """
    for i in range(-1, size + 1):
        for j in range(-1, 2):
            col_1 = j if increase[1] else 0
            col_2 = j if increase[0] else 0
            x = coords[0] + increase[0] * i + col_1
            y = coords[1] + increase[1] * i + col_2
            if (x, y) in data:
                data.remove((x, y))
    return data


def is_valid(ships):
    """
    (arr of tuples) -> bool
    Check is field is valid
    Return: is field is valid
    """
    lens = {1: 0, 2: 0, 3: 0, 4: 0}
    for sh in ships:
        if sh[0] > 9 or sh[0] < 0 or sh[1] > 9 or sh[1] < 0:
            return False
        if(sh[0] + 1, sh[1] + 1) in ships or \
        (sh[0] + 1, sh[1] - 1) in ships or \
        (sh[0] - 1, sh[1] + 1) in ships or \
        (sh[0] - 1, sh[1] - 1) in ships:
            return False
        l = ship.ship_size(ships, sh)
        if l not in lens:
            return False
        else:
            lens[l] += 1
    if lens[1] == 4 and lens[2] == 6 and \
    lens[3] == 6 and lens[4] == 4:
        return True
    else:
        return False
    