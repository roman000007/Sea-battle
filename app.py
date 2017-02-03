import random

def get_direction(crds, size, data):
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
    while True:
        choosed = random.randint(0, len(data) - 1)
        coords = data[choosed]
        increase = get_direction(coords, size, data)
        if increase is not None:
            break
    for i in range(size):
        ships.append((coords[0] + increase[0] * i, coords[1] + increase[1] * i))
    # delete surrounded data
    for i in range(size):
        data.remove((coords[0] + increase[0] * i, coords[1] + increase[1] * i))
    print(data)
    # Not worked!
    print(ships)
    print(coords, increase)

def generate_field():
    ships = []
    coords = [(x, y) for x in range(10) for y in range(10)]
    setup_ship(4, coords, ships)



generate_field()


def read_field(file):
    res = []
    with open(file + ".txt", "r") as fl:
        text = fl.read().split("\n")
    for row in text:
        tmp = []
        for ch in row:
            tmp.append(ch)
        res.append(tmp)
    return res

field = read_field("field")

#print(field)

def has_ship(field, coords):
    """
    :param field:
    :param coords: which row, which elem
    :return: is ship there
    """
    ind_1 = ord(coords[0]) - ord('A')
    ind_2 = int(coords[1]) - 1
    return field[ind_1][ind_2] == "*"

#print(has_ship(field, ('A','1')))
