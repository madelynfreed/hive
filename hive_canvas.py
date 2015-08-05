from Tkinter import Tk, Canvas
import math
from main import Position

class HexGrid(object):
	def __init__(self, a_coord, b_coord, postion_object, canvas):
		self.a_coord = a_coord
		self.b_coord = b_coord
		self.P = postion_object
		self.canvas = canvas
		self.draw_polygon(self.a_coord, self.b_coord)
	def translate_adj_spots(self):
		adjacent_spots = self.P.adjacent_spots()
		spots = [(spot[0]-x, spot[1]-y, spot[2]-z) for spot in adjacent_spots]
		adj_coordinates = []
		for spot in spots:
			if spot == (0,1,-1):
				adj_coordinates.append((0,math.sqrt(3)*r))
			elif spot == (1,0,-1):
				adj_coordinates.append((1.5*r,(math.sqrt(3)/2)*r))
			elif spot == (1,-1,0):
				adj_coordinates.append((1.5*r,-(math.sqrt(3)/2)*r))
			elif spot == (0,-1,1):
				adj_coordinates.append((0,-math.sqrt(3)*r))
			elif spot == (-1,0,1):
				adj_coordinates.append((-1.5*r,-(math.sqrt(3)/2)*r))
			elif spot == (-1,1,0):
				adj_coordinates.append((-1.5*r,(math.sqrt(3)/2)*r))
		return adj_coordinates
		
	def draw_polygon(self,a_coo,b_coo):
		point_reference = [a_coo+0.5*self.P.r, b_coo-(math.sqrt(3)*0.5*self.P.r),
			 a_coo+self.P.r, b_coo,
			 a_coo+.5*self.P.r, b_coo+(math.sqrt(3)*0.5*self.P.r),
			 a_coo-.5*self.P.r, b_coo+(math.sqrt(3)*0.5*self.P.r),
			 a_coo-self.P.r, b_coo,
			 a_coo-.5*self.P.r, b_coo-(math.sqrt(3)*0.5*self.P.r)]
		self.canvas.create_polygon(point_reference, outline='red',fill='green',width=2)
	def draw_neighbors(self):

		tuples_to_add_to_center =  self.translate_adj_spots()
		centers = [(self.a_coord+t[0],self.b_coord+t[1]) for t in tuples_to_add_to_center]
		for center in centers:
			self.draw_polygon(center[0],center[1])




def main():
	window = Tk()
	can = Canvas(window, width=500, height=500)
	can.pack()
	Pos = Position(0,0,0,60)
	hex = HexGrid(100,100,Pos,can)
	
	window.mainloop()

if __name__ == '__main__':
	main()
	
