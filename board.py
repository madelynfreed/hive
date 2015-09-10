#BOARD
import math
from piece import Piece
from location_and_piece import LocationPiece as lp
from move_validator import MoveValidator


nice_hive = [(3,-6,3),(2,-6,4),(2,-7,5),
	     (4,-8,4),(3,-9,6),(3,-10,7),
	     (3,-8,5),(2,-5,3)]
nice_hive_types = ['exists','grasshopper','ant','beetle','queen','spider','grasshopper','ant']

def create_nice_board_and_hive(radius):
	e = Board(20,20,radius)
	p = Piece('exists')
	g = Piece('grasshopper')
	map(lambda loc_type: e.place_piece(lp(Piece(loc_type[1]),loc_type[0],radius)), zip(nice_hive, nice_hive_types))
	for position in nice_hive:
		e.place_piece(lp(p, position,radius))
	e.place_piece(lp(g, (5,-8,3),radius))
	return e

class Board(object):
	def __init__(self, width, height, radius, validator=MoveValidator()):
		self.width = width
		self.height = height
		self.radius = radius
		self.validator = validator
		self.positions = self.translate_wh_into_hex_coords()
		self.empty_grid = {hex_coord:lp(Piece("blank"),hex_coord,self.radius) for hex_coord in self.positions}
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
		 
	
	def place_piece(self,locpiece):
		if locpiece.hex_coordinates in self.pieces_dict:
			print "you can't place a piece there!"
		else:
			self.pieces_dict[locpiece.hex_coordinates] = locpiece.piece_object
			self.refresh_lp()
		
	def move_piece(self, hex_coord, end_hex_coord):
		if self.validator.is_valid_move(hex_coord, end_hex_coord, self.pieces_dict):
			self.pieces_dict[end_hex_coord] = self.pieces_dict[hex_coord] 
			self.pieces_dict.pop(hex_coord)
			self.refresh_lp()
		

