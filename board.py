from main import Position

class Board(object):
	def __init__(self, width, height, radius):
		self.width = width
		self.height = height
		self.radius = radius

	def translate_wh_into_hex_coords(self):
		return [(x,-x-z,z) for x in range(self.width) for z in range(self.height)]
		 
	def space_has_piece_in_it(self, x_coord,y_coord,z_coord):
		return False
