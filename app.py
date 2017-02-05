"""
Created by Roman Vey
Starter file
05.02.2017

ships - array with coords of all ships
data - array with coords, where we can locate ships
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__)))
import field
import ship

ships = field.read_field("field")
#ships = field.generate_field()
print("Is valid:", field.is_valid(ships))
field.show_field(ships)