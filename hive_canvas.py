#CANVAS
from Tkinter import Tk, Canvas
import math
from board import Board

class HexGrid(object):
	def __init__(self, blank_grid_coords, coord_of_pieces, radius, canvas):
		self.radius = radius	
		self.canvas = canvas
		
		self.canvas.bind('<Button-1>', self.callback)
		self.coord_of_pieces = coord_of_pieces
		self.blank_grid_coords = blank_grid_coords
	def print_to_canvas(self,sq_coord_list_and_type):
		for sq_coord in sq_coord_list_and_type:
			self.draw_polygon(sq_coord[0][0], sq_coord[0][1], 
			sq_coord[1])
		
	def draw_polygon(self,a_coo,b_coo,piece_type):
		point_reference = [a_coo+0.5*self.radius, b_coo-(math.sqrt(3)*0.5*self.radius),
			 a_coo+self.radius, b_coo,
			 a_coo+.5*self.radius, b_coo+(math.sqrt(3)*0.5*self.radius),
			 a_coo-.5*self.radius, b_coo+(math.sqrt(3)*0.5*self.radius),
			 a_coo-self.radius, b_coo,
			 a_coo-.5*self.radius, b_coo-(math.sqrt(3)*0.5*self.radius)]
		if piece_type == None:
			blank_hexagon = self.canvas.create_polygon(point_reference, 
						outline='gray',
						activeoutline='black',
						fill='',width=1)
		else:
			piece = self.canvas.create_polygon(point_reference, 
						outline='gray',
						activefill='pink',
						#tags=piece_type.piece_type,
						fill='red',width=1)

	def find_closest_hexagon(self, x_click, y_click):
		def dist(hex_and_type):
			return (abs(hex_and_type[0][0]-x_click) 
				+ abs(hex_and_type[0][1]-y_click))
		return min(self.blank_grid_coords,
			 key=dist)
		
	def callback(self, event):
		x = self.find_closest_hexagon(event.x, event.y)
		a,b = x[0] 
		self.draw_polygon(a,b,'exists')
		print event.x, event.y
def translate_hex_position_to_pixels(hex_position, radius):
	x_coord = hex_position[0]
	z_coord = hex_position[2]
	a_coord = (3.0/2.0)*radius*z_coord
	b_coord = math.sqrt(3)*radius*(z_coord/2.0 + x_coord)
	return (a_coord, b_coord)

def generate_sq_coords_and_types(hex_dict, radius):
	return [(translate_hex_position_to_pixels(hex_position, radius),
				hex_dict[hex_position])
				for hex_position in hex_dict]
	
#when click, find nearest hexagon and place a piece there
def main(hex_grid, hex_positions_and_type, radius):
	window = Tk()

	can = Canvas(window, width=500, height=500)
	can.pack()

	grid_positions = generate_sq_coords_and_types(hex_grid, radius) 
	square_positions_and_type = generate_sq_coords_and_types(hex_positions_and_type, radius) 

	h = HexGrid(grid_positions, square_positions_and_type,radius, can)
	h.print_to_canvas(grid_positions)
	h.print_to_canvas(square_positions_and_type)

	window.mainloop()

if __name__ == '__main__':
	main()
	
