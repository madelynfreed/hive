from Tkinter import Tk, Canvas
import math
from main import Position

class HexGrid(object):
	def __init__(self, a_coord, b_coord, postion_object, canvas):
		self.a_coord = a_coord
		self.b_coord = b_coord
		self.P = postion_object
		self.canvas = canvas

def main():
	window = Tk()
	can = Canvas(window, width=500, height=500)
	Pos = Position(0,0,0,60)
	hex = HexGrid(100,100,Pos,can)
	
	window.mainloop()

if __name__ == '__main__':
	main()
	
