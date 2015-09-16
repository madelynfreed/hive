import unittest
import board
from board import Board
from move_validator import MoveValidator as mv
from piece import Piece
from location_and_piece import LocationPiece as lp
from board import Board
import numpy as np

class TestMoveValidator(unittest.TestCase):
	def test_empty_spots_adjacent_to_hive(self):
		hive_spots = [(2, -5, 3), (2, -3, 1), (3, -5, 2), (1, -3, 2), (1, -4, 3), (3, -4, 1)]
		empty_spots = [(3, -6, 3), (2, -6, 4), (4, -6, 2), (2, -4, 2), (4, -5, 1), (2, -2, 0), (3, -3, 0), (4, -4, 0), (1, -2, 1), (0, -2, 2), (0, -3, 3), (1, -5, 4), (0, -4, 4)]
		v = mv()
		e = Board(20,20,10)
		p = Piece('exists')
		map(lambda hive_spots: e.place_piece(lp(p,hive_spots,10)), hive_spots)
		self.assertItemsEqual(v.empty_spots_adjacent_to_hive(e.pieces_dict), empty_spots)
		
	def test_complicated_empty_spots_adjacent_to_hive(self):
		v = mv()
		hive_spots = [(10,-18,8),(11,-18,7),(12,-18,6),
			      (12,-17,5),(11,-16,5),(10,-15,5),
			      (9,-15,6),(9,-16,7)]
		adjacent_spots = [(9,-17,8),(8,-16,8),(8,-15,7),(8,-14,6),
				  (9,-14,5),(10,-14,4),(11,-15,4),(12,-16,4),
				  (13,-17,4),(13,-18,5),(13,-19,6),(12,-19,7),
				  (11,-19,8),(10,-19,9),(9,-18,9),
				  (10,-17,7),(11,-17,6),(10,-16,6)]
		e = Board(20,20,10)
		p = Piece('exists')
		map(lambda hive_spots: e.place_piece(lp(p,hive_spots,10)), hive_spots)
		self.assertItemsEqual(v.empty_spots_adjacent_to_hive(e.pieces_dict), adjacent_spots)

        def test_has_empty_shared_neighbor(self):
		v = mv()
		e = Board(20,20,10)
                piece1 = (5,-16,11)
                piece2 = (6,-16,10)
		self.assertTrue(v.has_empty_shared_neighbor(piece1, piece2, e.pieces_dict))
        def test_no_empty_shared_neighbor(self):
		v = mv()
		e = Board(20,20,10)
		p = Piece('exists')
                piece1 = (5,-16,11)
                piece2 = (6,-16,10)
                neigh_spots = [(5,-15,10),(6,-17,11)]
		map(lambda neigh_spots: e.place_piece(lp(p,neigh_spots,10)), neigh_spots)
		self.assertFalse(v.has_empty_shared_neighbor(piece1, piece2, e.pieces_dict))
	def test_find_unstuck_empty_spots(self):
		v = mv()
		e = Board(20,20,10)
		p = Piece('exists')
		adjacent_spots = set([(1, -3, 2), (4, -6, 2), (2, -3, 1), (4, -5, 1), (2, -5, 3), (1, -4, 3), (3, -4, 1)])
                hive_spots = [(3,-5,2),(2,-4,2)]
                ant_spot = (3,-6,3)
		map(lambda hive_spots: e.place_piece(lp(p,hive_spots,10)), hive_spots)
                self.assertEqual(v.find_unstuck_empty_spots(ant_spot, adjacent_spots, set(), e.pieces_dict), adjacent_spots)

	def test_find_unstuck_empty_with_inaccesible_spots(self):
		v = mv()
		e = Board(20,20,10)
		p = Piece('exists')
		hive_spots = [(5, -10, 5), (6, -13, 7), (5, -13, 8), (8, -12, 4), 
			      (7, -15, 8), (5, -11, 6), (4, -11, 7), (7, -11, 4), 
			      (6, -11, 5), (8, -15, 7), (7, -12, 5), (4, -12, 8), 
			      (5, -12, 7), (8, -14, 6), (4, -10, 6), (7, -14, 7), 
			      (8, -13, 5), (9, -14, 5), (6, -10, 4), (9, -15, 6), 
			      (9, -13, 4)]
		adjacent_spots = [(3, -9, 6), (7, -10, 3), (8, -16, 8), (10, -14, 4), 
				(9, -12, 3), (7, -16, 9), (3, -12, 9), (6, -9, 3), 
				(6, -15, 9), (5, -14, 9), (5, -9, 4), (10, -13, 3), 
				(3, -10, 7), (10, -16, 6), (10, -15, 5), (4, -13, 9), 
				(3, -11, 8), (4, -9, 5), (8, -11, 3), (9, -16, 7),
				(6,-12,6),(7,-13,6)]
		unstuck_spots = set([(3, -9, 6), (7, -10, 3), (8, -16, 8), (10, -14, 4), 
				(9, -12, 3), (7, -16, 9), (3, -12, 9), (6, -9, 3), 
				(6, -15, 9), (5, -14, 9), (5, -9, 4), (10, -13, 3), 
				(3, -10, 7), (10, -16, 6), (10, -15, 5), (4, -13, 9), 
				(3, -11, 8), (4, -9, 5), (8, -11, 3), (9, -16, 7)])
		map(lambda hive_spots: e.place_piece(lp(p,hive_spots,10)), hive_spots)
		start_spot = (6,-14,8)
                self.assertEqual(v.find_unstuck_empty_spots(start_spot, adjacent_spots, set(), e.pieces_dict), unstuck_spots)
		
		
	def test_find_unstuck_empty_with_blocked_spot(self):
		v = mv()
		e = Board(20,20,10)
		p = Piece('exists')
		hive_spots = [(8, -12, 4), (6, -13, 7), (5, -10, 5), (8, -14, 6), 
				(6, -10, 4), (8, -13, 5), (7, -11, 4), (5, -11, 6), 
				(5, -12, 7)]
		adjacent_spots = [(6, -12, 6), (7, -14, 7), (7, -13, 6), (4, -12, 8), 
				(9, -14, 5), (7, -10, 3), (9, -15, 6), (9, -12, 3), 
				(6, -14, 8), (6, -9, 3), (5, -13, 8), (4, -11, 7), 
				(4, -9, 5), (4, -10, 6), (9, -13, 4), (6, -11, 5), 
				(8, -11, 3), (7, -12, 5), (5, -9, 4)]
		unstuck_spots = set([(7, -14, 7), (4, -12, 8), (9, -14, 5), (7, -10, 3), 
				(9, -15, 6), (9, -12, 3), (6, -14, 8), (6, -9, 3), 
				(5, -13, 8), (4, -11, 7), (4, -9, 5), (4, -10, 6), 
				(9, -13, 4), (8, -11, 3), (5, -9, 4)])
		map(lambda hive_spots: e.place_piece(lp(p,hive_spots,10)), hive_spots)
		start_spot = (8,-15,7)
                self.assertEqual(v.find_unstuck_empty_spots(start_spot, adjacent_spots, set(), e.pieces_dict), unstuck_spots)
		
		
	
	def test_ant_path(self):
		v = mv()
		ant_spot = (11,-19,8)
		hive_spots = [(11,-19,8),(10,-18,8),(11,-18,7),(12,-18,6),(12,-17,5),(11,-16,5),(10,-15,5),(9,-15,6),(9,-16,7)]
		adjacent_spots = [(9,-17,8),(8,-16,8),(8,-15,7),(8,-14,6),
				  (9,-14,5),(10,-14,4),(11,-15,4),(12,-16,4),
				  (13,-17,4),(13,-18,5),(13,-19,6),(12,-19,7),
				  (12,-20,8),(11,-20,9),(10,-19,9),(9,-18,9),
				  (10,-17,7),(10,-16,6),(11,-17,6)]

		ant_path = [(9,-17,8),(8,-16,8),(8,-15,7),(8,-14,6),
				  (9,-14,5),(10,-14,4),(11,-15,4),(12,-16,4),
				  (13,-17,4),(13,-18,5),(13,-19,6),(12,-19,7),
				  (10,-19,9),(9,-18,9)]
		e = Board(20,20,10)
		p = Piece('exists')
		map(lambda hive_spots: e.place_piece(lp(p,hive_spots,10)), hive_spots)
		self.assertItemsEqual(v.spots_in_ant_path(ant_spot, e.pieces_dict), ant_path)

	def test_simple_ant_path(self):
		v = mv()
		hive_spots = [(6, -9, 3), (5, -8, 3)]
		adjacent_spots = [(4, -8, 4), (5, -7, 2), (4, -7, 3), (6, -8, 2), (5, -9, 4)]
		ant_spot = (6,-9,3)
		e = Board(20,20,10)
		p = Piece('exists')
		e.place_piece(lp(p,hive_spots[0],10))
		e.place_piece(lp(p,hive_spots[1],10))
		self.assertItemsEqual(v.spots_in_ant_path(ant_spot, e.pieces_dict), adjacent_spots)
		
	def test_empty_neighbors(self):
		v = mv()
		hex_spot = (7,-10,3)
		spots = [(6,-9,3),(8,-10,2),(7,-11,4)]
		empty_spots = [(6,-10,4),(8,-11,3),(7,-9,2)]
		e = Board(20,20,10)
		p = Piece('exists')
		map(lambda spot: e.place_piece(lp(p,spot,10)), spots)
		self.assertItemsEqual(v.empty_neighbors(hex_spot, e.pieces_dict),empty_spots)

		
	def test_is_stuck(self):
		v = mv()
		hex_spot = (7,-10,3)
		spots = [(6,-9,3),(8,-10,2),(7,-11,4)]
		e = Board(20,20,10)
		p = Piece('exists')
		map(lambda spot: e.place_piece(lp(p,spot,10)), spots)
		self.assertTrue(v.is_stuck(hex_spot, e.pieces_dict))

	def test_is_stuck_with_many_neighbors(self):
		v = mv()
		hex_spot = (7,-10,3)
		spots = [(6,-9,3),(8,-10,2),(7,-11,4),(7,-9,2),(8,-11,3)]
		e = Board(20,20,10)
		p = Piece('exists')
		map(lambda spot: e.place_piece(lp(p,spot,10)), spots)
		self.assertTrue(v.is_stuck(hex_spot, e.pieces_dict))

	def test_is_not_stuck(self):
		v = mv()
		hex_spot = (7,-10,3)
		spots = [(6,-9,3),(8,-10,2),(7,-9,2),(8,-11,3)]
		e = Board(20,20,10)
		p = Piece('exists')
		map(lambda spot: e.place_piece(lp(p,spot,10)), spots)
		self.assertFalse(v.is_stuck(hex_spot, e.pieces_dict))

	def test_is_valid_move_for_queen(self):
		v = mv()
		e = board.create_nice_board_and_hive(10)
		start_hex_coords = (1,-5,4)
		end_hex_coords = (1,-6,5)
		p = Piece('queen')
		
		e.place_piece(lp(p,start_hex_coords,100))

		self.assertTrue(v.is_valid_move(start_hex_coords,
				end_hex_coords,
				e.pieces_dict))

	def test_move_does_not_work_because_invalid_for_queen(self):
		v = mv()
		e = board.create_nice_board_and_hive(10)
		start_hex_coords = (4,-9,5)
		end_hex_coords = (1,-4,3)
		p = Piece('queen')
		
		e.place_piece(lp(p,start_hex_coords,10))
		
		self.assertFalse(v.is_valid_move(start_hex_coords,
				end_hex_coords,
				e.pieces_dict))

	def test_queen_valid_move(self):
		v = mv()
		e = Board(4,4,10)
		
		start_hex_coords = (2,-2,0)
		end_hex_coords = (2,-1,-1)
		self.assertTrue(v.queen_valid_move(start_hex_coords, end_hex_coords, e.pieces_dict))
	def test_is_valid_move_for_grasshopper(self):
		v = mv()
		e = board.create_nice_board_and_hive(10)
		start_hex_coords = (5,-8,3) 
		#start coords for the grasshopper on the nice board
		end_hex_coords = (2,-8,6)
		
		self.assertTrue(v.grasshopper_valid_move(start_hex_coords, end_hex_coords, e.pieces_dict))
		
	def test_all_spots_between_two_inline_spots(self):
		v = mv()
		all_spots = [[5,-8,3],[4,-8,4],[3,-8,5]]
		self.assertItemsEqual(v.all_spots_between_two_inline_spots((6,-8,2),(2,-8,6)), all_spots)
		
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
	
if __name__ == '__main__':
	unittest.main()
