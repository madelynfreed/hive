#BOARD
import math
from piece import Piece
class Board(object):
	def __init__(self, width, height, radius):
		self.width = width
		self.height = height
		self.radius = radius
		self.positions = self.translate_wh_into_hex_coords()
		self.empty_grid = {hex_coord:None for hex_coord in self.positions}
		self.pieces_dict = {}

	#def existing_pieces(self):
		#return [(hex_position, pieces) 
			#for hex_position, pieces in self.pieces_dict.items() 
			#if pieces]
	
	def translate_wh_into_hex_coords(self):
		return [(x,-x-z,z)
			for x in range(self.width) 
			for z in range(self.height)]
		 
	def space_has_piece_in_it(self, hex_coord):
		return hex_coord in self.pieces_dict
	
	def place_piece(self,hex_position, piece_object):
		if hex_position in self.pieces_dict:
			self.pieces_dict[hex_position].append(piece_object) 
		else:
			self.pieces_dict[hex_position] = piece_object
		
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
		return self.are_adjacent(start_hex_coord, end_hex_coord) and not self.space_has_piece_in_it(end_hex_coord)		

	def move_piece(self, hex_coord, end_hex_coord):
		if (self.are_adjacent(hex_coord, end_hex_coord) 
			and self.space_has_piece_in_it(end_hex_coord) == False):

			print "BOARDS verson of hex coord and end coord"
			print hex_coord, end_hex_coord
			print "BOARD's version @move"
			print self.pieces_dict
			print self.pieces_dict[hex_coord]
			self.pieces_dict[end_hex_coord] = self.pieces_dict[hex_coord] 
			self.pieces_dict.pop(hex_coord)
		else:
			print "YOUUUU can only move to empty, adjacent spots!"
			
