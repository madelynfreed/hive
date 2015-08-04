
from Tkinter import Tk, Canvas, Frame, BOTH
import math

class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Shapes")        
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
            
	x = 100
	y = 100
	r = 90

	point_reference = [x+0.5*r, y-(math.sqrt(3)*0.5*r), x+r, y, x+.5*r, y+(math.sqrt(3)*0.5*r), x-.5*r, y+(math.sqrt(3)*0.5*r), x-r, y, x-.5*r, y-(math.sqrt(3)*0.5*r)]
	points = [reference for reference in point_reference]

        canvas.create_polygon(points, outline='red', 
            fill='green', width=2)
        
        canvas.pack(fill=BOTH, expand=1)


def main():
  
    root = Tk()
    ex = Example(root)
    root.geometry("500x500+300+300")
    root.mainloop()  


if __name__ == '__main__':
    main()  
