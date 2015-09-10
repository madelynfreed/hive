import unittest
import board
from board import Board
from move_validator import MoveValidator as mv
from piece import Piece
from location_and_piece import LocationPiece as lp
from board import Board

class TestMoveValidator(unittest.TestCase):
	def test_is_valid_move(self):
		v = mv()
		e = board.create_nice_board_and_hive(10)
		start_hex_coords = (5,-8,3)
		end_hex_coords = (4,-7,3)
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

	def test_find_all_new_neighbors_of_new_neighbors(self):
		v= mv()
		e = board.create_nice_board_and_hive(10)
		spot = (2,-6,4)
		all_neighbors = v.find_all_new_neighs(spot, e.pieces_dict, [])
		self.assertItemsEqual(all_neighbors, e.pieces_dict.keys())

	def test_find_all_neighs_for_broken_hive(self):
		v = mv()
		e = board.create_nice_board_and_hive(10)
		e.pieces_dict.pop((3,-8,5),None)
		spot = (2,-7,5)
		all_neighbors = v.find_all_new_neighs(spot, e.pieces_dict, [])
		self.assertItemsEqual(all_neighbors, [(2,-6,4),(2,-5,3),(3,-6,3),(2,-7,5)])

	def test_flood_catches_valid_pickup(self):
		v = mv()
		e = board.create_nice_board_and_hive(10)
		p = Piece('exists')
		elpe = lp(p,(4,-7,3),10)
		e.place_piece(elpe)
		spot = (2,-6,4)
		self.assertTrue(v.flood(spot,e.pieces_dict))
	def test_flood_catches_invalid_pickup(self):
		v = mv()
		e = board.create_nice_board_and_hive(10)
		spot = (2,-6,4)
		self.assertFalse(v.flood(spot,e.pieces_dict))
	
#	def test_path_found_when_piece_is_moved(self):
#		v = mv()
#		e = board.create_nice_board_and_hive(10)
#		spot = (3,-6,3)
#		self.assertTrue(v.path_found_when_piece_is_moved(spot,e.pieces_dict))
#
#	def test_path_not_found_when_piece_is_moved(self):
#		v = mv()
#		e = board.create_nice_board_and_hive(10)
#		spot = (3,-9,6)
#		self.assertFalse(v.path_found_when_piece_is_moved(spot, e.pieces_dict))
#
#	def test_path_from_piece_to_piece(self):
#		v = mv()
#		e = board.create_nice_board_and_hive(10)
#		spot1 = (3,-9,6)
#		spot2 = (2,-9,7)
#		visited_pieces = [(3,-10,7)]
#		self.assertEqual(v.path_from_piece_to_piece(spot1,spot2,visited_pieces,e.pieces_dict), (False, [(3,-10,7),(3,-9,6)]))
#		
#	def test_path_from_piece_finds_target(self):
#		v = mv()
#		e = board.create_nice_board_and_hive(10)
#		spot1 = (3,-9,6)
#		spot2 = (3,-8,5)
#		visited_pieces = [spot1]
#		self.assertEqual(v.path_from_piece_to_piece(spot1,spot2,visited_pieces,e.pieces_dict), (True, (3,-8,5)))
		
	def test_neighbors(self):
		v = mv()
		b = board.create_nice_board_and_hive(10)
		spot = (3,-9,6)
		self.assertItemsEqual(v.neighbors(spot, b.pieces_dict), [(3,-8,5), (3,-10,7)])
		
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
		
	def test_is_adjacent_to_the_hive(self):
		e = board.create_nice_board_and_hive(10)
		spot = (2,-8,6)
		v = mv()
		self.assertTrue(v.is_adjacent_to_the_hive(spot,e.pieces_dict))

	def test_is_not_adjacent_to_the_hive(self):
		e = board.create_nice_board_and_hive(10)
		spot = (6,-20,14)
		v = mv()
		self.assertFalse(v.is_adjacent_to_the_hive(spot, e.pieces_dict))
if __name__ == '__main__':
	unittest.main()
