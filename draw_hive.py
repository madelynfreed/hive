import Tkinter as Tk
import math

def getregpoly(sides):
	points = []
	ang = 2*math.pi/sides
	for i in range(sides):
		deg = (i+.5)*ang
		points.append(math.sin(deg)/2.0+.5)
		points.append(math.cos(deg)/2.0+.5)
	return points

class Shape(object):
	size = 1
	x = y = 0
	def __init__(self, **kwds):
		self.__dict__.update(kdws)
	def __call__(self, *args, **kwds):
		for key in self.__dict__:
			kwds[key] = self.__dict__[key]
		return self.__class__(*args, **kwds)
	def draw(self, c, x=0, y=0, scale=1.0):
		draw(self, c, x, y, scale)
polygon = Shape(obj='polygon', fill='white', outline='black', 
		width = 0, points=[0,0], smooth='false')
hexagon = polygon(points=getregpoly(6))
"""def hiveboard():

    window=Tk()
    can = Canvas(window, width=500,height=500)
    can.grid(row=0,column=0)
    window.update_idletasks()

    w=can.winfo_width()
    h=can.winfo_height()
    hexagoncoordx = w/2
    hexagoncoordy = h/2
    window.mainloop()
"""


