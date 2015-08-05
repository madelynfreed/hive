from Tkinter import Tk, Canvas
import math
from main import Position

class HexGrid(object):
	def __init__(self, coord_list, radius, canvas):
		self.radius = radius	
		self.coord_list = coord_list
		self.canvas = canvas
		for coord in self.coord_list:
			print "coord!!!!"
			print coord
			self.draw_polygon(coord[0], coord[1])
	#def translate_adj_spots(self):
		#adjacent_spots = self.P.adjacent_spots()
		#spots = [(spot[0]-x, spot[1]-y, spot[2]-z) for spot in adjacent_spots]
		#adj_coordinates = []
		#for spot in spots:
			#if spot == (0,1,-1):
				#adj_coordinates.append((0,math.sqrt(3)*r))
			#elif spot == (1,0,-1):
				#adj_coordinates.append((1.5*r,(math.sqrt(3)/2)*r))
			#elif spot == (1,-1,0):
				#adj_coordinates.append((1.5*r,-(math.sqrt(3)/2)*r))
			#elif spot == (0,-1,1):
				#adj_coordinates.append((0,-math.sqrt(3)*r))
			#elif spot == (-1,0,1):
				#adj_coordinates.append((-1.5*r,-(math.sqrt(3)/2)*r))
			#elif spot == (-1,1,0):
				#adj_coordinates.append((-1.5*r,(math.sqrt(3)/2)*r))
		#return adj_coordinates
		
	def draw_polygon(self,a_coo,b_coo):
		print a_coo, b_coo
		point_reference = [a_coo+0.5*self.radius, b_coo-(math.sqrt(3)*0.5*self.radius),
			 a_coo+self.radius, b_coo,
			 a_coo+.5*self.radius, b_coo+(math.sqrt(3)*0.5*self.radius),
			 a_coo-.5*self.radius, b_coo+(math.sqrt(3)*0.5*self.radius),
			 a_coo-self.radius, b_coo,
			 a_coo-.5*self.radius, b_coo-(math.sqrt(3)*0.5*self.radius)]
		self.canvas.create_polygon(point_reference, outline='red',fill='green',width=2)
	def draw_n_polygons(postions):
		for position in positions:
			self.draw_polygon(position[0],position[1])
	def draw_neighbors(self):

		tuples_to_add_to_center =  self.translate_adj_spots()
		centers = [(self.a_coord+t[0],self.b_coord+t[1]) for t in tuples_to_add_to_center]
		for center in centers:
			self.draw_polygon(center[0],center[1])




def main(position_objects):
	window = Tk()
	can = Canvas(window, width=500, height=500)
	can.pack()
	radius = position_objects[0].r
	n_positions = [position.translate_position_to_pixels() for position in position_objects]
	hex = HexGrid(n_positions,radius, can)

	window.mainloop()

if __name__ == '__main__':
	main()
	
