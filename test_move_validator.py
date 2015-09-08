import unittest
from board import Board
from move_validator import MoveValidator as mv
from piece import Piece
from location_and_piece import LocationPiece as lp
from board import Board

class TestMoveValidator(unittest.TestCase):
	def test_is_valid_move(self):
		v = mv()
		e = Board(4,4,100,v)
		start_hex_coords = (1,-2,1)
		end_hex_coords = (1,-1,0)
		p = Piece('exists')
		
		e.place_piece(lp(p,start_hex_coords,100))

		self.assertTrue(v.is_valid_move(start_hex_coords,
				end_hex_coords,
				e.pieces_dict))

	def test_move_does_not_work_because_invalid(self):

		v = mv()
		e = Board(4,4,100)
		start_hex_coords = (1,-2,1)
		end_hex_coords = (1,-8,7)
		p = Piece('exists')
		
		e.place_piece(lp(p,start_hex_coords,100))

		self.assertFalse(v.is_valid_move(start_hex_coords,
				end_hex_coords,
				e.pieces_dict))

	def test_adjacent_spots(self):
		#b = Board(3,3,0)
		v = mv()
		self.assertTrue((1,0,-1) in v.adjacent_spots((0,0,0)))

	def test_non_adjacent_spots(self):
		#b = Board(0,0,0)
		v = mv()
		self.assertFalse((21,0,-1) in v.adjacent_spots((0,0,0)))

	def test_positions_are_adjacent(self):
		v = mv()
		m = (0,3,-3)
		n = (-1,4,-3)
		self.assertTrue(v.are_adjacent(m, n))

	def test_empty_board(self):
		empty = Board(5,5,60)
		v = mv()
		self.assertFalse(v.space_has_piece_in_it((2,-2,0),empty.pieces_dict))	
	def test_space_has_a_piece_in_it(self):
		b = Board(5,5,60)
		p = Piece('_')
		b.pieces_dict[(1,-2,1)] = p
		v = mv()
		self.assertTrue(v.space_has_piece_in_it((1,-2,1),b.pieces_dict))
	
if __name__ == '__main__':
	unittest.main()
