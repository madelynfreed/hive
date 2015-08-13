#CANVAS
from Tkinter import Tk, Canvas
import math
from board import Board
from piece import Piece

class HexGrid(object):
	def __init__(self, board_object, radius, canvas):

		self.canvas = canvas
		self.board = board_object
		self.radius = board_object.radius	

		self.empty_grid_dict = self.board.empty_grid	
		self.blank_grid_coords = generate_sq_coords_and_types(self.empty_grid_dict, radius) 

		self.pieces_dict = self.board.pieces_dict 
		self.coord_of_pieces = generate_sq_coords_and_types(self.pieces_dict, radius) 

		self.canvas.tag_bind('empty','<Button-1>', self.place_piece_on_canvas)
		self.canvas.tag_bind('exists','<ButtonPress-1>', self.OnTagButtonPress)
		self.canvas.tag_bind('exists','<ButtonRelease-1>', self.OnTagButtonRelease)
		self.canvas.tag_bind('exists','<B1-Motion>', self.OnTagMotion)
		self.canvas.bind('Double-Button-1', self.move_piece_on_canvas)
		self.blank_grid_coords = generate_sq_coords_and_types(self.empty_grid_dict, radius) 
		
		self._drag_data = {"x": 0, "y": 0, "item" : None}
	def print_tagged_to_canvas(self,sq_coord_list_and_type):
		for sq_coord in sq_coord_list_and_type:
			self.draw_polygon(sq_coord[0][0], sq_coord[0][1], 
			sq_coord[1])

	def hex_points_reference(self,a_coo,b_coo):
		return  [a_coo+0.5*self.radius, b_coo-(math.sqrt(3)*0.5*self.radius),
			 a_coo+self.radius, b_coo,
			 a_coo+.5*self.radius, b_coo+(math.sqrt(3)*0.5*self.radius),
			 a_coo-.5*self.radius, b_coo+(math.sqrt(3)*0.5*self.radius),
			 a_coo-self.radius, b_coo,
			 a_coo-.5*self.radius, b_coo-(math.sqrt(3)*0.5*self.radius)]
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
						fill='',width=1,
						tags="empty")
		else:
			piece = self.canvas.create_polygon(point_reference, 
						outline='gray',
						activefill='pink',
						fill='red',width=1,
						tags=piece_type)

	def find_closest_space(self, x_click, y_click):
		def dist(hex_and_type):
			return (abs(hex_and_type[0][0]-x_click) 
				+ abs(hex_and_type[0][1]-y_click))
		return min(self.blank_grid_coords,
			 key=dist)
		
	def find_closest_piece(self,x_click,y_click):
		close_pieces = self.canvas.find_closest(x_click,y_click, halo=self.radius)
		return close_pieces[0]
		
	def OnTagButtonPress(self, event):
		self._drag_data["item"] = self.find_closest_piece(event.x, event.y)
		self._drag_data['x'] = event.x
		self._drag_data['y'] = event.y
	
	def OnTagButtonRelease(self, event):
		x = self.find_closest_space(event.x, event.y)
		points = self.hex_points_reference(x[0][0],x[0][1])
		print points
		self.canvas.coords(self._drag_data["item"],points[0],points[1],points[2],points[3],points[4],points[5],points[6],points[7],points[8],points[9],points[10],points[11],)
		self._drag_data["item"] = None
		
		self._drag_data['x'] = 0
		self._drag_data['y'] = 0

	def OnTagMotion(self, event):
		delta_x = event.x - self._drag_data['x']
		delta_y = event.y - self._drag_data['y']
		self.canvas.move(self._drag_data["item"], delta_x, delta_y)
		
		self._drag_data['x'] = event.x
		self._drag_data['y'] = event.y
	def drop_piece_on_canvas(self, event):
		x = self.find_closest_space(event.x, event.y)
		

	def place_piece_on_canvas(self, event):
		x = self.find_closest_space(event.x, event.y)
		a,b = x[0] 
		self.draw_polygon(a,b,'exists')
		hexes = translate_pixels_to_hex_position(x[0],self.radius)
		p = Piece('exists')
		self.board.place_piece(hexes,p)
		print event.x, event.y
		print self.pieces_dict

	def move_piece_on_canvas(self, event):
		x = self.find_closest_space(event.x, event.y)
		hexes = translate_pixels_to_hex_position(x[0],self.radius)
		self.board.move_piece(hexes,(3,-6,3))
		print event.x, event.y
		print self.pieces_dict

def translate_hex_position_to_pixels(hex_position, radius):
	x_coord = hex_position[0]
	z_coord = hex_position[2]
	a_coord = (3.0/2.0)*radius*z_coord
	b_coord = math.sqrt(3)*radius*(z_coord/2.0 + x_coord)
	return (a_coord, b_coord)
def translate_pixels_to_hex_position(sq_coord, radius):
	a_coord = sq_coord[0]
	b_coord = sq_coord[1]
	z_coord = a_coord/((3.0/2.0)*radius)
	x_coord = (b_coord/(math.sqrt(3)*radius)) - z_coord/2.0
	y_coord = -x_coord-z_coord
	return (x_coord,y_coord,z_coord)
	
def generate_sq_coords_and_types(hex_dict, radius):
	return [(translate_hex_position_to_pixels(hex_position, radius),
				hex_dict[hex_position])
				for hex_position in hex_dict]
	
def main(board_object, radius):
	window = Tk()

	can = Canvas(window, width=500, height=500)
	can.pack(fill="both", expand=True)

	h = HexGrid(board_object,radius, can)
	h.print_tagged_to_canvas(h.blank_grid_coords)
	h.print_tagged_to_canvas(h.coord_of_pieces)

	window.mainloop()

if __name__ == '__main__':
	main()
	
