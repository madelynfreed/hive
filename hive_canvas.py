from Tkinter import Tk, Canvas
import math
from main import Position
from board import Board
class HexGrid(object):
	def __init__(self, coord_list, radius, canvas):
		self.radius = radius	
		self.coord_list = coord_list
		self.canvas = canvas
		for coord in self.coord_list:
			self.draw_polygon(coord[0], coord[1], coord[2])
		
	def draw_polygon(self,a_coo,b_coo,piece_type):
		point_reference = [a_coo+0.5*self.radius, b_coo-(math.sqrt(3)*0.5*self.radius),
			 a_coo+self.radius, b_coo,
			 a_coo+.5*self.radius, b_coo+(math.sqrt(3)*0.5*self.radius),
			 a_coo-.5*self.radius, b_coo+(math.sqrt(3)*0.5*self.radius),
			 a_coo-self.radius, b_coo,
			 a_coo-.5*self.radius, b_coo-(math.sqrt(3)*0.5*self.radius)]
		self.canvas.create_polygon(point_reference, outline='gray',fill='',width=1)


def main(positions_and_type, board):
	window = Tk()
	can = Canvas(window, width=500, height=500)
	can.pack()
	radius = board.radius
	n_positions = [position.translate_position_to_pixels() for position in positions_and_type]
	hex = HexGrid(n_positions,radius, can)

	window.mainloop()

if __name__ == '__main__':
	main()
	
