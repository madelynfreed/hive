#BOARD
import math
from piece import Piece
class Board(object):
	def __init__(self, width, height, radius):
		self.width = width
		self.height = height
		self.radius = radius
		self.positions = self.translate_wh_into_hex_coords()
		self.pos_dict = {hex_coord:[] for hex_coord in self.positions}
	
	def translate_wh_into_hex_coords(self):
		return [(x,-x-z,z) for x in range(self.width) for z in range(self.height)]
		 
	def space_has_piece_in_it(self, hex_coord):
		return self.pos_dict[hex_coord] != [] 
	
	def place_piece(self,hex_position, piece_object):
		self.pos_dict[hex_position].append(piece_object) 
		
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
	
	def are_adjacent(self,hexposition1,hexposition2):
		return hexposition1 in self.adjacent_spots(hexposition2) 

	def move_piece(self, hex_coord, end_hex_coord):
		if self.pos_dict[hex_coord] != [] and self.are_adjacent(hex_coord, end_hex_coord) and self.pos_dict[end_hex_coord] ==[]:
			p = self.pos_dict[hex_coord] 
			self.pos_dict[hex_coord] = []
			self.pos_dict[end_hex_coord] = p
			
