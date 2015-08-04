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
def scale(points, scale):
	return [x*scale for x in points]

def move(points, x, y):
	xy= [x,y]*(len(points)//2)
	return [xy+coord for xy, coord in zip(xy,points)]

def translate(obj, x, y, zoom):
	p = scale(obj.points, obj.size)
	p = move(p, obj.x, obj.y)
	p = scale(p, zoom)
	return move(p, x, y)

def draw(obj, c, x=0, y=0, zoom=1):
	p = translate(obj, x, y, zoom)
	if obj.obj=='line':
		c.create_line(p, fill=obj.fill, width=obj.width, arrow=obj.arrow)
	elif obj.obj=='polygon':
		c.create_polygon(p, fill=obj.fill, outline=obj.outline, width=obj.width, smooth=obj.smooth)

class Shape(object):
	size = 1
	x = y = 0
	def __init__(self, **kwds):
		self.__dict__.update(kwds)
	def __call__(self, *args, **kwds):
		for key in self.__dict__:
			kwds[key] = self.__dict__[key]
		return self.__class__(*args, **kwds)
	def draw(self, c, x=0, y=0, scale=1.0):
		draw(self, c, x, y, scale)
polygon = Shape(obj='polygon', fill='grey', outline='black', 
		width = 0, points=[0,0], smooth='false')
hexagon = polygon(points=getregpoly(6))

line = Shape(obj='line', arrow='none', fill='black', smooth='false', width=1, points=[0,0,1,0])
if __name__ == '__main__':
	root = Tk.Tk()
	root.title('Resizable Shapes')
	c = Tk.Canvas(root)

	line(width=3, fill='darkgrey', arrow='both').draw(c,20,205,336)
	hexagon(width=10).draw(c,20,205,336)
	c.pack()
	root.mainloop()

