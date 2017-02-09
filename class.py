import random
class Game:
	def __init__(self):
		pass

		
class Field:
	def __init__(self, file = None):
		self.dots = []
		self.ships = []
		if file is not None:
			self._read_field(file)
			return
		self.allowed_coords = [(x, y) for x in range(10) for y in range(10)]
		self._generate_field()
		
		
	
	def all_ships(self):
		res = ""
		for ship in self.ships:
			res += str(ship.healthy_coords) + " " + str(ship.damaged_coords) + "\n"
		return res	
		
		
	
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
	
	

	
	
class Player:
	def __init__(self):
		pass
		
		
class Ship:
	def __init__(self, field, coords = None):
		self.healthy_coords = []
		self.damaged_coords = []
		if coords is not None:
			self.healthy_coords = field._find_all_ship_coords(coords)
		self.length = len(self.healthy_coords)
	
		
f1 = Field("field")
print(f1)
print(f1.all_ships())