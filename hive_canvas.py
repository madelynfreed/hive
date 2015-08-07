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
			self.draw_polygon(sq_coord[0], sq_coord[1], sq_coord[2])
		
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
			self.canvas.create_polygon(point_reference, outline='',fill='red',width=1)


def main(positions_and_type, radius):
	window = Tk()
	can = Canvas(window, width=500, height=500)
	can.pack()
	n_positions = [Board.square_coord_and_type(Board.translate_hex_position_to_pixels(position, radius), None) for position in positions_and_type]
	hex = HexGrid(n_positions,radius, can)

	window.mainloop()

if __name__ == '__main__':
	main()
	
