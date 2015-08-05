import unittest
from main import Position
import main
import hive_canvas
class TestHive(unittest.TestCase):
	def test_adjacent_spots(self):
		b = Position(0,0,0,10)
		self.assertTrue((1,0,-1) in b.adjacent_spots())
	def test_non_adjacent_spots(self):
		b = Position(0,0,0,10)
		self.assertFalse((21,0,-1) in b.adjacent_spots())
	def test_positions_are_adjacent(self):
		a = Position(0,3,-3,10)
		b = Position(-1, 4, -3,10)
		self.assertTrue(main.are_adjacent(a, b))
	def test_translate_position_to_pixels(self):
		hive_canvas.main([Position(1,2,-3,10)])
		self.assertTrue(False)
		
if __name__ == '__main__':
	unittest.main()

