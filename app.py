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


#some_stupid_code