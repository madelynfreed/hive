#CANVAS
from Tkinter import Tk, Canvas
import math
from board import Board

class HexGrid(object):
	def __init__(self, sq_coord_list_and_type, radius, canvas):
		self.radius = radius	
		self.sq_coord_list_and_type = sq_coord_list_and_type
		self.canvas = canvas
		for sq_coord in self.sq_coord_list_and_type:
			self.draw_polygon(sq_coord[0][0], sq_coord[0][1], sq_coord[1])
		
	def draw_polygon(self,a_coo,b_coo,piece_type):
		point_reference = [a_coo+0.5*self.radius, b_coo-(math.sqrt(3)*0.5*self.radius),
			 a_coo+self.radius, b_coo,
			 a_coo+.5*self.radius, b_coo+(math.sqrt(3)*0.5*self.radius),
			 a_coo-.5*self.radius, b_coo+(math.sqrt(3)*0.5*self.radius),
			 a_coo-self.radius, b_coo,
			 a_coo-.5*self.radius, b_coo-(math.sqrt(3)*0.5*self.radius)]
		if piece_type == None:
			self.canvas.create_polygon(point_reference, outline='gray',fill='',width=1)
		else:
			self.canvas.create_polygon(point_reference, outline='gray',fill='red',width=1)

def translate_hex_position_to_pixels(hex_position, radius):
	x_coord = hex_position[0]
	z_coord = hex_position[2]
	a_coord = (3.0/2.0)*radius*z_coord
	b_coord = math.sqrt(3)*radius*(z_coord/2.0 + x_coord)
	return (a_coord, b_coord)

def main(hex_positions_and_type, radius):
	window = Tk()
	can = Canvas(window, width=500, height=500)
	can.pack()
	square_positions_and_type = [(translate_hex_position_to_pixels(pos[0],radius),pos[1]) for pos in hex_positions_and_type]
	hex = HexGrid(square_positions_and_type,radius, can)

	window.mainloop()

if __name__ == '__main__':
	main()
	
