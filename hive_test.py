#TEST
import unittest
import hive_canvas as hcan
from board import Board
from piece import Piece
from Tkinter import Tk, Canvas

def create_canvas():
	window = Tk()
	can = Canvas(window, width=500, height=500)
	can.pack()
	return can

nice_hive = [(3,-6,3),(2,-6,4),(2,-7,5),
	     (4,-8,4),(3,-9,6),(3,-9,6),
	     (3,-8,5),(2,-5,3)]

def create_nice_board_and_hive():
	e = Board(20,20,10)
	p = Piece('exists')
	for position in nice_hive:
		e.place_piece(position, p)
	return e

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

	def test_translate_hex_to_sq_and_back(self):
		hex_pos = (4,-9,5)
		sq = hcan.translate_hex_position_to_pixels(hex_pos, 10)
		self.assertTrue(hcan.translate_pixels_to_hex_position(sq, 10) == hex_pos)
	
	def test_is_valid_move(self):
		e = Board(4,4,100)
		start_hex_coords = (1,-2,1)
		end_hex_coords = (1,-1,0)
		p = Piece('exists')
		
		e.place_piece(start_hex_coords,p)
		self.assertTrue(e.is_valid_move(start_hex_coords,
				end_hex_coords,
				p.piece_type))

	def test_is_valid_move_because_of_hive_adjacency(self):
		e = create_nice_board_and_hive()

		pass
		
	def test_is_adjacent_to_the_hive(self):
		e = create_nice_board_and_hive()
		spot = (2,-8,6)
		self.assertTrue(e.is_adjacent_to_the_hive(spot))

	def test_is_not_adjacent_to_the_hive(self):
		e = create_nice_board_and_hive()
		spot = (6,-20,14)
		self.assertFalse(e.is_adjacent_to_the_hive(spot))
			
		
	#@unittest.skip('dont want to always print')
	def test_find_closest_hexagon(self):
		e = Board(20,20,10)
		pd = e.empty_grid
		p = Piece('-')
		e.place_piece((10,-20,10),p)
		empty = hcan.generate_sq_coords_and_types(pd,e.radius)
		pieces = hcan.generate_sq_coords_and_types(e.pieces_dict,e.radius)
		can = create_canvas()	
		h = hcan.HexGrid(e,e.radius,can)
		x_click = 156
		y_click = 265	
		self.assertTrue(h.find_closest_space(x_click,y_click) == (hcan.translate_hex_position_to_pixels((10,-20,10),10), None))

	#@unittest.skip('dont want to always print')
	def test_printing_board(self):
		e = Board(100,100,20)
		p = Piece('exists')
		pd = e.empty_grid
		p = Piece('-')
		e.place_piece((24,-48,24),p)
		e.place_piece((14,-28,14),p)
		placed = e.pieces_dict
		
		hcan.main(e, e.radius)
	
if __name__ == '__main__':
	unittest.main()
