import random
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__)))
import field


def setup_ships(field, ships):
    """
    (arr of tuples, arr of tuples) -> (arr of tuples, arr of tuples)
    Setup all ships into field
    return: return updated arrays of field and ships
    """
    field, ships = setup_ship(4, field, ships)
    field, ships = setup_ship(3, field, ships)
    field, ships = setup_ship(3, field, ships)
    field, ships = setup_ship(2, field, ships)
    field, ships = setup_ship(2, field, ships)
    field, ships = setup_ship(2, field, ships)
    field, ships = setup_ship(1, field, ships)
    field, ships = setup_ship(1, field, ships)
    field, ships = setup_ship(1, field, ships)
    field, ships = setup_ship(1, field, ships)
    return field, ships


def get_direction(crds, size, data):
    """
    (tuple, int, arr of tuples) -> tuple 
    Get coords, search in which direction we can increase ship and return random one
    Return: random direction for increasing ship length
    """
    directions = []
    d1 = True
    d2 = True
    d3 = True
    d4 = True
    for i in range(1, size):
        if(crds[0] - i < 0 or (crds[0] - i, crds[1]) not in data):
            d1 = False
        if(crds[0] + i > 9 or (crds[0] + i, crds[1]) not in data):
            d2 = False
        if(crds[1] - i < 0 or (crds[0], crds[1] - 1) not in data):
            d3 = False
        if(crds[1] + i > 9 or (crds[0], crds[1] + 1) not in data):
            d4 = False
    if d1:
        directions.append((-1, 0))
    if d2:
        directions.append((1, 0))
    if d3:
        directions.append((0, -1))
    if d4:
        directions.append((0, 1))
    if len(directions) == 0:
        return None
    random.shuffle(directions)
    return directions[0]


def setup_ship(size, data, ships):
    """
    (int, array of tuples, array of tuples) -> (array of tuples, array of tuples) 
    get size of ship, aloowed coords and setup ship in random position 
    Return: updated field and array of ships
    """
    while True:
        choosed = random.randint(0, len(data) - 1)
        coords = data[choosed]
        increase = get_direction(coords, size, data)
        if increase is not None:
            break
    for i in range(size):
        ships.append((coords[0] + increase[0] * i, coords[1] + increase[1] * i))
    data = field.delete_not_empty_fields(coords, increase, data, size)
    return data, ships


def has_ship(ships, coords):
    """
    (array ) -> 
    Descr
    Return: 
    """
    ind_1 = ord(coords[0]) - ord('A')
    ind_2 = int(coords[1]) - 1
    return (ind1, ind2) in ships
