import unittest
from main import Position

class TestHive(unittest.TestCase):
	def test_adjacent_spots(self):
		b = Position(0,0,0)
		self.assertTrue((1,0,-1) in b.adjacent_spots())

if __name__ == '__main__':
	unittest.main()

