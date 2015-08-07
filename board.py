#BOARD
import math
class Board(object):
	def __init__(self, width, height, radius):
		self.width = width
		self.height = height
		self.radius = radius
		self.positions = self.translate_wh_into_hex_coords()
	
	def translate_wh_into_hex_coords(self):
		return [(x,-x-z,z) for x in range(self.width) for z in range(self.height)]
		 
	def space_has_piece_in_it(self, x_coord,y_coord,z_coord):
		return False
	
	def adjacent_spots(self, hex_position):
		x_coord = hex_position[0]
		y_coord = hex_position[1]
		z_coord = hex_position[2]
		adj_spot_formulae = [(x_coord + 1, y_coord, z_coord - 1),
				     (x_coord + 1, y_coord -1, z_coord),
				     (x_coord, y_coord -1, z_coord + 1),
				     (x_coord - 1, y_coord, z_coord + 1),
				     (x_coord - 1, y_coord + 1, z_coord),
				     (x_coord, y_coord + 1, z_coord - 1)]
		return [formula for formula in adj_spot_formulae]
	
	@staticmethod
	def translate_hex_position_to_pixels(hex_position, radius):
		x_coord = hex_position[0]
		z_coord = hex_position[2]
		a_coord = (3.0/2.0)*radius*z_coord
		b_coord = math.sqrt(3)*radius*(z_coord/2.0 + x_coord)
		return (a_coord, b_coord)
	@staticmethod
	def square_coord_and_type(square_coord, piece_type):
		return (square_coord[0], square_coord[1], piece_type)
		

	def are_adjacent(self,hexposition1,hexposition2):
		return hexposition1 in self.adjacent_spots(hexposition2) 
