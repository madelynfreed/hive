import unittest
import main

class TestHive(unittest.TestCase):
	b = Position(0,0)
	assert((1,0,-1) in b.adjacent_spots)

if __name__ == '__main__':
	unittest.main()

