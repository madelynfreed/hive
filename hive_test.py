#TEST
import unittest
import board
from board import Board
from piece import Piece
from location_and_piece import LocationPiece as lp
import webbrowser
import tempfile
import time
import webhive
from fake_move_validator import FakeMoveValidator as fmv
from move_validator import MoveValidator as mv

class TestHive(unittest.TestCase):
	
	def test_place_piece(self):
		b = Board(5,5,60)
		place = (2,-4,2)
		piece = Piece('some')
		b.place_piece(lp(piece,place,60))
		self.assertTrue(b.pieces_dict[place] == piece)

	def test_board_moves_when_move_validator_allows_it(self):
		move_validator = fmv()

		b = Board(5,5,'0',move_validator)
		
		start_place = (0,0,0)
		end_place = (0,1,-1)
		p = Piece('_')

		move_validator.allow_move(start_place, end_place, b.pieces_dict)

		b.place_piece(lp(p, start_place,0))
		b.move_piece(start_place, end_place)
		self.assertTrue(b.pieces_dict[end_place] == p 
				and start_place not in b.pieces_dict)
		
	def test_board_does_not_move_when_move_validator_disallows_it(self):
		move_validator = fmv()
		b = Board(5,5,'0',move_validator)
		
		start_place = (0,0,0)
		end_place = (0,1,-1)
		p = Piece('_')

		b.place_piece(lp(p, start_place,0))
		b.move_piece(start_place, end_place)
		self.assertTrue(b.pieces_dict[start_place] == p 
				and end_place not in b.pieces_dict)

	def test_translate_wh_into_hex_coords(self):
		e = Board(4,4,100)
		self.assertTrue((3,-6,3) in e.translate_wh_into_hex_coords())

	#def test_translate_hex_to_sq_and_back(self):
		#hex_pos = (4,-9,5)
		#sq = hcan.translate_hex_position_to_pixels(hex_pos, 10)
		#self.assertTrue(hcan.translate_pixels_to_hex_position(sq, 10) == hex_pos)
	
	#def test_is_valid_move_because_of_hive_adjacency(self):
		#e = create_nice_board_and_hive()

		#pass
	
	
	def test_location_in_lp(self):
		e = board.create_nice_board_and_hive(10)
		spot = (3,-10,7)
		self.assertTrue(e.location_in_lp(spot))

	def test_location_not_in_lp(self):
		e = board.create_nice_board_and_hive(10)
		spot = (100,100,100)
		self.assertFalse(e.location_in_lp(spot))

	def test_refresh_lp(self):
		e = Board(10,10,100)
		spot = (3,-3,0)
		self.assertFalse(e.location_in_lp(spot))
		p = Piece('exists')
		locpie = lp(p,spot,100)
		e.pieces_dict[locpie.hex_coordinates] = locpie.piece_object
		e.refresh_lp()
		self.assertTrue(e.location_in_lp(spot))
		
if __name__ == '__main__':
	unittest.main()
