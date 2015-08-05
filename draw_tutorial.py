
from Tkinter import Tk, Canvas, Frame, BOTH
import math
from main import Position

class HexGrid(Frame):
     
    def translate_adj_spots(self):
	adjacent_spots = self.Pos.adjacent_spots()
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


    def __init__(self, parent, position_object):
        Frame.__init__(self, parent)   
        self.Pos = position_object
        self.parent = parent        
        self.initUI()

        
    def draw_polygons(self,x_coord,y_coord,canvas):
	
	point_reference = [x_coord+0.5*self.Pos.r, y_coord-(math.sqrt(3)*0.5*self.Pos.r), x_coord+self.Pos.r, y_coord, x_coord+.5*self.Pos.r, y_coord+(math.sqrt(3)*0.5*self.Pos.r), x_coord-.5*self.Pos.r, y_coord+(math.sqrt(3)*0.5*self.Pos.r), x_coord-self.Pos.r, y_coord, x_coord-.5*self.Pos.r, y_coord-(math.sqrt(3)*0.5*self.Pos.r)]
	canvas.create_polygon(point_reference, outline='red',fill='green',width=2)
	
    def initUI(self):
      
        self.parent.title("Shapes")        
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
            
	x = 400
	y = 400
	r = 90

	self.draw_polygons(x,y,r,canvas)

	tuples_to_add_to_center =  self.translate_adj_spots(0,0,0,r)
	centers = [(x+t[0],y+t[1]) for t in tuples_to_add_to_center]
	for center in centers:
		self.draw_polygons(center[0],center[1],r,canvas)
        
        canvas.pack(fill=BOTH, expand=1)


def main():
  
    window = Tk()
<<<<<<< HEAD
    ex = HexGrid(window)
    window.geometry("1000x1000+300+300")
=======
    hex = HexGrid(window,Position(0,0,0,60)
    #window.geometry("1000x1000+300+300")
>>>>>>> checkpoint
    window.mainloop()  


if __name__ == '__main__':
    main()  
