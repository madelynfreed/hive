import math
from board import Board
import text
import hive_test
from location_and_piece import LocationPiece as lp

def hex_at_square_coords(location_piece):
	if location_piece.piece_object != None: 
		return '<img src="http://www.iconsdb.com/icons/preview/red/hexagon-xxl.png" style="left:%dpx; top:%dpx" width="400">' % (location_piece.a, location_piece.b)
	else:
		return '<img src="http://www.fontsaddict.com/images/icons/png/22865.png" style="left:%dpx; top:%dpx" width="400">' % (location_piece.a, location_piece.b)

radius = 153
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
