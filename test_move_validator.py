import unittest
from board import Board
from move_validator import MoveValidator
from piece import Piece
from location_and_piece import LocationPiece as lp

class TestMoveValidator(unittest.TestCase):
	def test_is_valid_move(self):
		mv = MoveValidator()
		e = Board(4,4,100,mv)
		start_hex_coords = (1,-2,1)
		end_hex_coords = (1,-1,0)
		p = Piece('exists')
		
		e.place_piece(lp(p,start_hex_coords,100))

		self.assertTrue(mv.is_valid_move(start_hex_coords,
				end_hex_coords,
				e.pieces_dict))

	def test_move_does_not_work_because_invalid(self):

		mv = MoveValidator()
		e = Board(4,4,100)
		start_hex_coords = (1,-2,1)
		end_hex_coords = (1,-8,7)
		p = Piece('exists')
		
		e.place_piece(lp(p,start_hex_coords,100))

		self.assertFalse(mv.is_valid_move(start_hex_coords,
				end_hex_coords,
				e.pieces_dict))

if __name__ == '__main__':
	unittest.main()
