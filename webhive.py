import math
from board import Board
import text
import hive_test
from location_and_piece import LocationPiece as lp

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

radius = 200
#radius = 153
#this specific radius is special for the image source

e = hive_test.create_nice_board_and_hive()

location_pieces_dict = [lp(piece, hex_coords, radius) for hex_coords, piece in e.pieces_dict.items()]
location_pieces_empty_grid_dict = [lp(piece, hex_coords, radius) for hex_coords, piece in e.empty_grid.items()]

def template_to_draw_hexes(location_pieces):
	img_string = ''
	for locpie in location_pieces:
		#(a,b) = translate_hex_position_to_pixels(key, radius)
		img_string += hex_at_square_coords(locpie)
	return img_string

def build_string():
	return text.header() + template_to_draw_hexes(location_pieces_empty_grid_dict) + template_to_draw_hexes(location_pieces_dict) + text.footer()
