import random
class Game:
    def __init__(self):
        pass

        
class Field:
    def __init__(self):
        self.ships = []
        self.allowed_coords = [(x, y) for x in range(10) for y in range(10)]
        
    
    def generate_field(self):
        """
        () -> None
        Fuction, which start generate field algorithm 
        Return: None
        """
        self.setup_ship(4)
        self.setup_ship(3)
        self.setup_ship(3)
        self.setup_ship(2)
        self.setup_ship(2)
        self.setup_ship(2)
        self.setup_ship(1)
        self.setup_ship(1)
        self.setup_ship(1)
        self.setup_ship(1)

        
    def setup_ship(self, size):
        """
        (int, array of tuples, array of tuples) -> (array of tuples, array of tuples) 
        Get size of ship, aloowed coords and setup ship in random position 
        Return: updated field and array of ships
        """
        while True:
            choosed = random.randint(0, len(self.allowed_coords) - 1)
            coords = self.allowed_coords[choosed]
            increase = self.get_direction(coords, size)
            if increase is not None:
                break
        for i in range(size):
            self.ships.append((coords[0] + increase[0] * i, coords[1] + increase[1] * i))
        self.delete_not_empty_fields(coords, increase, size)
    
    
    def delete_not_empty_fields(self, coords, increase, size):
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
                if (x, y) in self.allowed_coords:
                    self.allowed_coords.remove((x, y))

    
    def field_to_str(self):
        """
        (arr of tuples) -> (string)
        Convert battle field with ships to string
        Return: string
        """
        field_str = ""
        for i in range(10):
            for j in range(10):
                if (i, j) in self.ships:
                    field_str += "*"
                else:
                    field_str += " "
            field_str += "\n"
        return field_str


    def show_field(self):
        """
        (arr of tuples) -> None
        Print battle field with ships to string
        Return: None
        """
        print(self.field_to_str())
    
    
    def get_direction(self, coords, size):
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
            if(coords[0] - i < 0 or (coords[0] - i, coords[1]) not in self.allowed_coords):
                d1 = False
            if(coords[0] + i > 9 or (coords[0] + i, coords[1]) not in self.allowed_coords):
                d2 = False
            if(coords[1] - i < 0 or (coords[0], coords[1] - 1) not in self.allowed_coords):
                d3 = False
            if(coords[1] + i > 9 or (coords[0], coords[1] + 1) not in self.allowed_coords):
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
    
    
    
    
class Player:
    def __init__(self):
        pass
        
        
class Ship:
    def __init__(self, coords, id):
        self.healthy_coords = coords
        self.damaged_coords = []
        self.length = len(coords)
        self.id = id
        
        
f1 = Field()
f1.generate_field()
f1.show_field()
print("-" * 10)
f2 = Field()
f2.generate_field()
f2.show_field()
print("-" * 10)
f1.show_field()