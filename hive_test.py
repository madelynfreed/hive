#TEST
import unittest
import hive_canvas as hcan
from board import Board
from piece import Piece

class TestHive(unittest.TestCase):
	def test_adjacent_spots(self):
		b = Board(3,3,0)
		self.assertTrue((1,0,-1) in b.adjacent_spots((0,0,0)))
	def test_non_adjacent_spots(self):
		b = Board(0,0,0)
		self.assertFalse((21,0,-1) in b.adjacent_spots((0,0,0)))
	def test_positions_are_adjacent(self):
		a = Board(0,0,0)
		m = (0,3,-3)
		n = (-1,4,-3)
		self.assertTrue(a.are_adjacent(m, n))
	def test_empty_board(self):
		empty = Board(5,5,60)
		self.assertFalse(empty.space_has_piece_in_it((2,-2,0)))	
	def test_place_piece(self):
		b = Board(5,5,60)
		place = (2,-4,2)
		piece = Piece('some')
		b.place_piece(place,piece.piece_type)
		
		self.assertIn((place,piece.piece_type), b.positions)
	def test_translate_wh_into_hex_coords(self):
		e = Board(4,4,100)
		self.assertTrue((3,-6,3) in e.translate_wh_into_hex_coords())

	@unittest.skip('dont want to always print')
	def test_printing_board(self):
		e = Board(100,100,4)
		p = Piece('exists')
		posses = [(coord, None) for coord in e.positions]
		posses.append(((1,-2,1),p.piece_type))
		posses.append(((25,-50,25),p.piece_type))
		
		hcan.main(posses, e.radius)
	
if __name__ == '__main__':
	unittest.main()
