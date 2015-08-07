#TEST
import unittest
import hive_canvas
from board import Board
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
		self.assertFalse(empty.space_has_piece_in_it(2,-2,0))	
	def test_translate_wh_into_hex_coords(self):
		e = Board(4,4,100)
		self.assertTrue((3,-6,3) in e.translate_wh_into_hex_coords())

	#@unittest.skip('dont want to always print')
	def test_printing_board(self):
		e = Board(100,100,4)
		posses = [coord for coord in e.translate_wh_into_hex_coords()]
		hive_canvas.main(posses, e.radius)
	
	def test_square_coord_and_type(self):
		coords = (0,0)
		ptype = None
		self.assertTrue(Board.square_coord_and_type(coords, ptype) == (0,0,None))

if __name__ == '__main__':
	unittest.main()
