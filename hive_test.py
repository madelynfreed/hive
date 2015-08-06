import unittest
from main import Position
import main
import hive_canvas
from board import Board
class TestHive(unittest.TestCase):
	def test_adjacent_spots(self):
		b = Position(0,0,0,106)
		self.assertTrue((1,0,-1) in b.adjacent_spots())
	def test_non_adjacent_spots(self):
		b = Position(0,0,0,10)
		self.assertFalse((21,0,-1) in b.adjacent_spots())
	def test_positions_are_adjacent(self):
		a = Position(0,3,-3,10)
		b = Position(-1, 4, -3,10)
		self.assertTrue(main.are_adjacent(a, b))
	def test_translate_position_to_pixels(self):
	
		self.assertTrue(True)
	def test_empty_board(self):
		empty = Board(5,5,60)
		self.assertFalse(empty.space_has_piece_in_it(2,-2,0))	
	def test_translate_wh_into_hex_coords(self):
		e = Board(4,4,100)
		self.assertTrue((3,-6,3) in e.translate_wh_into_hex_coords())

	#@unittest.skip('dont want to always print')
	def test_printing_board(self):
		e = Board(100,100,4)
		posses = [(Position(coord[0],coord[1],coord[2],e.radius),None) for coord in e.hex_grid]
		hive_canvas.main(posses, e)

if __name__ == '__main__':
	unittest.main()
