#BOARD
import math
from piece import Piece
from location_and_piece import LocationPiece as lp

class Board(object):
	def __init__(self, width, height, radius):
		self.width = width
		self.height = height
		self.radius = radius
		self.positions = self.translate_wh_into_hex_coords()
		self.empty_grid = {hex_coord:None for hex_coord in self.positions}
		self.pieces_dict = {}

		self.location_pieces = [
			lp(piece, hex_coords, self.radius) 
			for hex_coords, piece in self.pieces_dict.items()]
		self.location_pieces_empty_grid = [
			lp(piece, hex_coords, self.radius) 
			for hex_coords, piece in self.empty_grid.items()]

	def translate_wh_into_hex_coords(self):
		return [(x,-x-z,z)
			for x in range(self.width) 
			for z in range(self.height)]
	def refresh_lp(self):
		self.location_pieces = [
			lp(piece, hex_coords, self.radius) 
			for hex_coords, piece in self.pieces_dict.items()]
	def location_in_lp(self, spot):
		return any(lp.hex_coordinates == spot for lp in self.location_pieces)
		 
	def space_has_piece_in_it(self, hex_coord):
		return hex_coord in self.pieces_dict
	
	def place_piece(self,locpiece):
		if locpiece.hex_coordinates in self.pieces_dict:
			print "you can't place a piece there!"
		else:
			self.pieces_dict[locpiece.hex_coordinates] = locpiece.piece_object
			self.refresh_lp()
		
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

	def is_valid_move(self, start_hex_coord, end_hex_coord, piece_type):
		return (self.are_adjacent(start_hex_coord,
					 end_hex_coord) 
		        and not 
			self.space_has_piece_in_it(end_hex_coord)
			and
			self.is_adjacent_to_the_hive(end_hex_coord))		

	def move_piece(self, hex_coord, end_hex_coord):
		self.pieces_dict[end_hex_coord] = self.pieces_dict[hex_coord] 
		self.pieces_dict.pop(hex_coord)
		self.refresh_lp()
			
	def is_adjacent_to_the_hive(self, hex_coord):
		l = [self.adjacent_spots(hex_coo) for hex_coo in self.pieces_dict.keys()]
		flat_list = reduce(lambda x,y: x+y, l)
		return  hex_coord in flat_list 






