import math
from board import Board
import text
import hive_test
from piece import Piece
from location_and_piece import LocationPiece as lp

class WebHive(object):
	def __init__(self):
		self.e = hive_test.create_nice_board_and_hive()
		self.radius = 200

		self.location_pieces_dict = [
			lp(piece, hex_coords, self.radius) 
			for hex_coords, piece in self.e.pieces_dict.items()]
		self.location_pieces_empty_grid_dict = [
			lp(piece, hex_coords, self.radius) 
			for hex_coords, piece in self.e.empty_grid.items()]

	def template_to_draw_hexes(self, location_pieces):
		img_string = ''
		for locpie in location_pieces:
			#(a,b) = translate_hex_position_to_pixels(key, radius)
			img_string += self.hex_at_square_coords(locpie)
		return img_string

	def build_string(self):
		return text.header() + self.template_to_draw_hexes(self.location_pieces_empty_grid_dict) + self.template_to_draw_hexes(self.location_pieces_dict) + text.footer()

	def place_piece(self,x,y,z):
		self.e.place_piece(lp(Piece('exists'), (x,y,z), self.radius))
		self.location_pieces_dict = [
			lp(piece, hex_coords, self.radius) 
			for hex_coords, piece in self.e.pieces_dict.items()]

	@staticmethod
	def hex_at_square_coords(location_piece):
		piece_image = "/piece_image.png" 
		blank_image = "/blank_image.png"
		return '<a href="/click/%d/%d/%d"><img src="%s" class="drawn_hexagons" id="%s" style="left:%dpx; top:%dpx" width="400"></a>' % (
			location_piece.x,
			location_piece.y,
			location_piece.z,
			piece_image if location_piece.piece_object != None else blank_image,
			location_piece.id_from_hex,
			location_piece.a, 
			location_piece.b)

	#radius = 153
	#this specific radius is special for the image source



