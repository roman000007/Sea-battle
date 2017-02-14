import random
import os
clear = lambda: os.system('cls')

# * - ship
# X - hitted
# O - missed
#   - Empty
# docs, wait(good), field, player info, readme.md, commit
      
class Field:
    def __init__(self, file = None):
        self.dots = []
        self.ships = []
        if file is not None:
            self._read_field(file)
            return
        self.allowed_coords = [(x, y) for x in range(10) for y in range(10)]
        self._generate_field()
        
        
    def get_ship_by_coords(self, coords):
        for ship in self.ships:
            if coords in ship.healthy_coords or coords in ship.damaged_coords:
                return ship
        return None
        
        
    def is_valid(self):
        """
        (arr of tuples) -> bool
        Check is field is valid
        Return: is field is valid
        """
        lens = {1: 0, 2: 0, 3: 0, 4: 0}
        for sh in self.dots:
            if sh[0] > 9 or sh[0] < 0 or sh[1] > 9 or sh[1] < 0:
                return False
            if(sh[0] + 1, sh[1] + 1) in self.dots or \
            (sh[0] + 1, sh[1] - 1) in self.dots or \
            (sh[0] - 1, sh[1] + 1) in self.dots or \
            (sh[0] - 1, sh[1] - 1) in self.dots:
                return False
            l = self.get_ship_by_coords(sh).length
            if l not in lens:
                return False
            else:
                lens[l] += 1
        if lens[1] == 4 and lens[2] == 6 and \
        lens[3] == 6 and lens[4] == 4:
            return True
        else:
            return False
            
        
        
        
    
    def show_all_ships(self):
        res = ""
        for ship in self.ships:
            print(ship)
        
        
    
    def _generate_field(self):
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

        
    def _read_field(self, file):
        """
        (string) -> (array of tuples) 
        Get field from file
        Return: field
        """
        self.ships = []
        with open(file + ".txt", "r") as fl:
            text = fl.read().split("\n")
        for i1, row in enumerate(text):
            for i2, ch in enumerate(row):
                if ch == '*':
                    self.dots.append((i1, i2))
        for dot in self.dots:
            already = False
            for ship in self.ships:
                if dot in ship.healthy_coords:
                    already = True
            if not already:
                s = Ship(self, dot)
                self.ships.append(s)

        
        
        
    def _find_all_ship_coords(self, coords):
        """
        (array of tuples, tuple) -> int
        Return: length of ship which is in selected position 
        """
        ship_coords = []
        if coords not in self.dots:
            return []
        ship_coords.append((coords[0], coords[1]))
        for i in range(1, 4):
            if(coords[0] + i, coords[1]) in self.dots:
                ship_coords.append((coords[0] + i, coords[1]))
            else:
                break
        for i in range(1, 4):
            if(coords[0] - i, coords[1]) in self.dots:
                ship_coords.append((coords[0] - i, coords[1]))
            else:
                break
        for i in range(1, 4):
            if(coords[0], coords[1] + i) in self.dots:
                ship_coords.append((coords[0], coords[1] + i))
            else:
                break
        for i in range(1, 4):
            if(coords[0], coords[1] - i) in self.dots:
                ship_coords.append((coords[0], coords[1] - i))
            else:
                break
        return ship_coords
        
        
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
        s = Ship(self)
        for i in range(size):
            s.healthy_coords.append((coords[0] + increase[0] * i, coords[1] + increase[1] * i))
            self.dots.append((coords[0] + increase[0] * i, coords[1] + increase[1] * i))
        self._delete_not_empty_fields(coords, increase, size)
        self.ships.append(s)
    
    
    def _delete_not_empty_fields(self, coords, increase, size):
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

    
    
    def __repr__(self):
        return self.field_to_str()
    
    
    
    def field_to_str(self):
        """
        (arr of tuples) -> (string)
        Convert battle field with ships to string
        Return: string
        """
        field_str = ""
        for i in range(10):
            for j in range(10):
                if (i, j) in self.dots:
                    field_str += "*"
                else:
                    field_str += " "
            field_str += "\n"
        return field_str

    
    
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
    
    

    
    
class Ship:
    def __init__(self, field, coords = None):
        self.healthy_coords = []
        self.damaged_coords = []
        self.killed = False
        if coords is not None:
            self.healthy_coords = field._find_all_ship_coords(coords)
        self.length = len(self.healthy_coords)
        
    def __repr__(self):
        res = "About Ship:" + "-" * 10
        res += "\nHealty coords: "
        for el in self.healthy_coords:
            res += str(el) + "; "
        res += "\nDamaged coords: "
        for el in self.damaged_coords:
            res += str(el) + "; "
        res += "\nLength: " + str(self.length)
        return res
        

class Player:
    def __init__(self, name, field):
        self.name = name
        self.field = field
        self.shoots = []
    
    def shoot_at(self, coords, player):
        self.shoots.append(coords)
        if coords in player.field.dots:
            ship = player.field.get_ship_by_coords(coords) 
            ship.healthy_coords.remove(coords)
            ship.damaged_coords.append(coords)
            print("You hit ship!")
            if ship.length == len(ship.damaged_coords):
                print("You destroy ship!")
                player.update_coords(ship.damaged_coords)
                ship.killed = True
            return True
        else:
            print("You missed.. Sorry")
            return False
    
    
    def update_coords(self, coords):
        vert = True if len(coords) == 1 or coords[0][0] == coords[1][0] else False
        if vert:
            min_v = coords[0][1]
            max_v = coords[0][1]
            for coord in coords:
                min_v = min(min_v, coord[1])
                max_v = max(max_v, coord[1])
                self.shoots.append((coord[0] - 1, coord[1]))
                self.shoots.append((coord[0] + 1, coord[1]))
            self.shoots.append((coords[0][0] - 1, min_v - 1))
            self.shoots.append((coords[0][0], min_v - 1))
            self.shoots.append((coords[0][0] + 1, min_v - 1))
            self.shoots.append((coords[0][0] - 1, max_v + 1))
            self.shoots.append((coords[0][0], max_v + 1))
            self.shoots.append((coords[0][0] + 1, max_v + 1))
        else:
            min_v = coords[0][0]
            max_v = coords[0][0]
            for coord in coords:
                min_v = min(min_v, coord[0])
                max_v = max(max_v, coord[0])
                self.shoots.append((coord[0], coord[1] - 1))
                self.shoots.append((coord[0], coord[1] + 1))
            self.shoots.append((min_v - 1, coords[0][1] - 1))
            self.shoots.append((min_v - 1, coords[0][1]))
            self.shoots.append((min_v - 1, coords[0][1] + 1))
            self.shoots.append((max_v + 1, coords[0][1] - 1))
            self.shoots.append((max_v + 1, coords[0][1]))
            self.shoots.append((max_v + 1, coords[0][1] + 1))
    
    def show_shoots(self, ships):
        res = ""
        for i in range(10):
            for j in range(10):
                if (i, j) in self.shoots and (i, j) not in ships:
                    res += "O"
                elif (i, j) in self.shoots and (i, j) in ships:
                    res += "X"
                else:
                    res += " "
            res += "\n"
        return res
    
    
    def read_position(self, player):
        while True:
            s = input()
            try:
                i1 = int(ord(s[:1]) - ord('A'))
                i2 = int(s[1:]) - 1
            except:
                print("Invalid syntax, use 'A1'-'J10'")
                self.read_position(player)
            if i1 > 9 or i2 > 9 or i1 < 0 or i2 < 0:
                print("Field is too small, use 'A1'-'J10'")
                self.read_position(player)
            elif (i1, i2) in player.shoots:
                print("You already hit this, choose another one")
                self.read_position(player)
            else:
                break
        return i1, i2 
        
        
class Game:
    def __init__(self):
        print("=============================================")
        print("       Game Battleship")
        print("=============================================")
        name1 = input("Player ONE name: ")
        name1 = name1 if name1 != "" else "Player ONE"
        fl1 = input("Enter your TXT file name(or ignore): ")
        f1 = Field() if fl1 == "" else Field(fl1)
        
        name2 = input("Player TWO name: ")
        name2 = name2 if name2 != "" else "Player TWO"
        fl2 = input("Enter your TXT file name(or ignore): ")
        f2 = Field() if fl2 == "" else Field(fl2)
        
        pl1 = Player(name1, f1)
        pl2 = Player(name2, f2)
        self.pl1 = pl1
        self.pl2 = pl2
        self.current_player = True
        
        self.player_turn()
        
        
    def player_turn(self):
        clear()  
        if self.current_player:
            print(self.pl1.name, "turn:")
            print(self.pl2.show_shoots(self.pl2.field.dots))
            coords = self.pl1.read_position(self.pl2)
            self.current_player = not self.current_player if self.pl2.shoot_at(coords, self.pl2) else self.current_player 
        else:
            print(self.pl2.name, "turn:")
            print(self.pl1.show_shoots(self.pl1.field.dots))
            coords = self.pl2.read_position(self.pl1)
            self.current_player = not self.current_player if self.pl1.shoot_at(coords, self.pl1) else self.current_player
        input()
        self.current_player = not self.current_player 
        if self.check_winner(self.pl1):
            self.show_winner(self.pl2)
        elif self.check_winner(self.pl2):
            self.show_winner(self.pl1)
        else:
            self.player_turn()
    
    
    def check_winner(self, player):
        yes = True
        for ship in player.field.ships:
            if not ship.killed:
                yes = False
                break
        return yes
            
    
    
    def show_winner(self, player):
        print(player.name, "wins!!! CONGRATULATIONS!")
        


game = Game()
