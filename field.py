import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__)))
import ship


def show_table(ships):
    """
    (arr of tuples) -> None 
    Print battle field with ships 
    Return: None
    """
    for i in range(10):
        for j in range(10):
            if (i, j) in ships:
                print("*", end="")
            else:
                print(" ", end="")
        print("")


def generate_field():
    """
    () -> None
    Fuction, which start generate field algorithm 
    Return: None
    """
    ships = []
    field = [(x, y) for x in range(10) for y in range(10)]
    field, ships = ship.setup_ships(field, ships)
    show_table(ships)


def read_field(file):
    """
    (string) -> (array of arrays of chars) 
    get field from file
    Return: field
    """
    res = []
    with open(file + ".txt", "r") as fl:
        text = fl.read().split("\n")
    for row in text:
        tmp = []
        for ch in row:
            tmp.append(ch)
        res.append(tmp)
    return res


def delete_not_empty_fields(coords, increase, data, size):
    for i in range(-1, size + 1):
        for j in range(-1, 2):
            col_1 = j if increase[1] else 0
            col_2 = j if increase[0] else 0
            x = coords[0] + increase[0] * i + col_1
            y = coords[1] + increase[1] * i + col_2
            if (x, y) in data:
                data.remove((x, y))
    return data
