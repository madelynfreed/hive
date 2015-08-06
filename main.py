#MAIN
import math
from board import Board
class Position(object):
	def __init__(self, x_coord, y_coord, z_coord):	
		self.x_coord = x_coord
		self.y_coord = y_coord		
		self.z_coord = z_coord		
	
	def adjacent_spots(self):
		adj_spot_formulae = [(self.x_coord + 1, self.y_coord, self.z_coord - 1),
				     (self.x_coord + 1, self.y_coord -1, self.z_coord),
				     (self.x_coord, self.y_coord -1, self.z_coord + 1),
				     (self.x_coord - 1, self.y_coord, self.z_coord + 1),
				     (self.x_coord - 1, self.y_coord + 1, self.z_coord),
				     (self.x_coord, self.y_coord + 1, self.z_coord - 1)]
		return [formula for formula in adj_spot_formulae]

	def translate_position_to_pixels(self):
		a_coord = (3.0/2.0)*Board.radius*self.z_coord
		b_coord = math.sqrt(3)*Board.radius*(self.z_coord/2.0 + self.x_coord)
		return (a_coord, b_coord)
def are_adjacent(position1, position2):
	return (position1.x_coord, position1.y_coord, position1.z_coord) in position2.adjacent_spots()
