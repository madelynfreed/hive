import unittest
from main import Position
import main

class TestHive(unittest.TestCase):
	def test_adjacent_spots(self):
		b = Position(0,0,0)
		self.assertTrue((1,0,-1) in b.adjacent_spots())
	def test_non_adjacent_spots(self):
		b = Position(0,0,0)
		self.assertFalse((21,0,-1) in b.adjacent_spots())
	def test_positions_are_adjacent(self):
		a = Position(0,3,-3)
		b = Position(-1, 4, -3)
		self.assertTrue(main.are_adjacent(a, b))
		
if __name__ == '__main__':
	unittest.main()

