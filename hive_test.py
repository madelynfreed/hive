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
	def test_space_has_a_piece_in_it(self):
		b = Board(5,5,60)
		p = Piece('_')
		b.pieces_dict[(1,-2,1)] = p
		self.assertTrue(b.space_has_piece_in_it((1,-2,1)))
		
	def test_place_piece(self):
		b = Board(5,5,60)
		place = (2,-4,2)
		piece = Piece('some')
		b.place_piece(place,piece)
		self.assertTrue(b.pieces_dict[place] == piece)

	def test_move_piece(self):
		b = Board(5,5,'_')
		
		start_place = (0,0,0)
		end_place = (0,1,-1)
		p = Piece('_')
		b.place_piece(start_place, p)
		b.move_piece(start_place, end_place)
		self.assertTrue(b.pieces_dict[end_place] == p 
				and start_place not in b.pieces_dict)
		
	def test_translate_wh_into_hex_coords(self):
		e = Board(4,4,100)
		self.assertTrue((3,-6,3) in e.translate_wh_into_hex_coords())

	def test_find_closest_hexagon(self):
		e = Board(20,20,10)
		pd = e.empty_grid
		p = Piece('-')
		e.place_piece((10,-20,10),p)
		hcan.main(pd, e.pieces_dict, e.radius)
	#@unittest.skip('dont want to always print')
	def test_printing_board(self):
		e = Board(100,100,10)
		p = Piece('exists')
		posses = [(coord, None) for coord in e.positions]
		posses.append(((1,-2,1),p.piece_type))
		posses.append(((25,-50,25),p.piece_type))
		
		hcan.main(posses, e.radius)
	
if __name__ == '__main__':
	unittest.main()
