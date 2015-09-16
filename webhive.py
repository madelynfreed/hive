import math
import text
import board
from piece import Piece
from location_and_piece import LocationPiece as lp

class WebHive(object):
	def __init__(self):
		self.radius = 35
		#self.e = board.create_nice_board_and_hive(self.radius)
		self.e = board.Board(20,20,self.radius)
		#self.e = board.create_complicated_board_and_hive(self.radius)

	def template_to_draw_hexes(self, location_pieces):
		img_string = ''
		for locpie in location_pieces:
			img_string += self.hex_at_square_coords(locpie)
		return img_string

	def build_string(self):
	#	return text.header() + '<a href="/click/0/0/0"> <div class="blankhexagon" id="0_0_0" style="left:0px; top:0px"></div></a>' + text.footer() 
		return text.header() + self.template_to_draw_hexes(self.e.location_pieces_empty_grid) + self.template_to_draw_hexes(self.e.location_pieces) + text.footer()

	def place_piece(self,piece_type,x,y,z):
		print "PLACE PIECE"
		print x, y, z
		locpie = lp(Piece(piece_type), (x,y,z), self.radius)
		self.e.place_piece(locpie)

	def move_piece(self, x1, y1, z1, x2, y2, z2):
		self.e.move_piece((x1, y1, z1),(x2, y2, z2))
			
	@staticmethod
	def hex_at_square_coords(location_piece):
		piece_image = "/piece_image.png" 
		blank_image = "/blank_image.png"

		return '<a href="/click/%d/%d/%d"> <div class="hex_container" id="%s" style="left:%dpx; top:%dpx"> <div class="blankhexagon" id="%s"></div> </div></a>' % (
			location_piece.x,
			location_piece.y,
			location_piece.z,
			location_piece.id_from_hex,
			location_piece.a, 
			location_piece.b,
			location_piece.piece_type
			)

	#radius = 153
	#this specific radius is special for the image source

